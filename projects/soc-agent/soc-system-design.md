# OpenHarness SOC — AI-Powered Security Alert Triage System

## Executive Summary

OpenHarness SOC is an AI-driven Security Operations Center agent that automates the triage of security alerts at enterprise scale. It leverages a locally-hosted open-source large language model (Gemma4-26B-A4B) as the reasoning engine, harnessed by a structured tool-calling framework that integrates with Fortinet's security ecosystem — FortiSOAR, FortiAnalyzer, and FortiSIEM — to investigate, correlate, and resolve security incidents autonomously.

The system's core design philosophy is **"intelligence in the tool layer, not in the model."** Rather than relying on the LLM's raw reasoning capabilities, the system encodes domain expertise into deterministic Python tools that perform CIDR classification, log aggregation, IP whitelisting, HMAC authentication, escalation detection, and audit trail generation. The LLM's role is deliberately constrained to tool selection, argument filling, evidence interpretation, and natural language summarization — tasks that even smaller, cost-efficient models handle reliably when the surrounding harness is well-designed.

In production testing, the system has successfully triaged **100+ real security alerts** across both FortiAnalyzer and FortiSIEM sources, correctly auto-closing benign alerts, detecting suspicious patterns like P2P/BitTorrent traffic on unusual ports, and escalating genuinely suspicious cases to the SOC team via email and Microsoft Teams notifications with full investigation context.

## System Architecture

### The Fortinet Security Ecosystem

The system operates within Fortinet's integrated security platform:

**FortiSOAR** serves as the central orchestration and ticketing platform. It aggregates security alerts from multiple detection sources — FortiAnalyzer and FortiSIEM — into a unified queue. When a FortiGate firewall, an IPS engine, or a SIEM correlation rule identifies suspicious activity, the resulting alert flows into FortiSOAR regardless of which detection system originated it. FortiSOAR provides the alert lifecycle management — creation, assignment, investigation tracking, and closure — that the SOC team operates against daily. The agent transitions alerts through the lifecycle: Open → Closed (resolved) or Open → Investigating (escalated).

**FortiAnalyzer (FAZ)** is the centralized log aggregation and analysis platform. Every FortiGate firewall in the network forwards its traffic logs, security event logs, and application control logs to FortiAnalyzer. When the AI agent investigates a FAZ-originated alert, it runs four correlation queries: security events in the 10-minute window after detection, source IP traffic before and after, and destination IP traffic after. FortiAnalyzer holds the forensic evidence — the raw network data that determines whether an alert represents a real threat or a benign event.

**FortiSIEM** serves a parallel role as a Security Information and Event Management platform. It aggregates logs and events from a broader set of sources (servers, applications, infrastructure) and provides its own detection and correlation capabilities. When the agent investigates a FortiSIEM-originated alert, it retrieves the raw triggering events — the actual syslog lines that caused the incident to fire — and analyzes the event patterns (login failures, timing, users, authentication methods) to determine if the activity is malicious. The tool layer automatically dispatches to the correct log backend based on the alert's source: FortiSIEM alerts query FortiSIEM; FAZ alerts query FAZ. The LLM follows the same investigation workflow regardless.

**Netbox** provides the IP address management and asset ownership database. When the agent resolves or escalates an alert, it automatically enriches the closure notes and escalation findings with ownership information from Netbox — querying across the prefix hierarchy from /24 up to /16 to find the most specific and most informative descriptions (e.g., "100.65.208.0/20: Frankfurt | 100.65.0.0/16: SASE"). This ownership context accelerates incident response by identifying the responsible team without manual lookup.

### The OpenHarness Framework

OpenHarness is an open-source Python framework that provides the structured tool-calling loop between the LLM and the external systems. On every interaction turn, the framework:

1. **Serializes available tools** into the OpenAI-compatible function-calling format. The SOC wrapper (`bis-soc`) filters the registry from 44+ built-in tools down to only the 8 tools relevant to security triage, reducing token consumption and eliminating model confusion.

2. **Receives structured tool calls** from the LLM as JSON objects — not free-text that requires parsing, but typed, schema-validated function calls with exact parameter names and values. This eliminates an entire class of parsing failures.

3. **Validates arguments** through Pydantic models before any tool code executes. Type errors, missing required fields, and out-of-range values are caught at this boundary and surfaced as clear error messages the LLM can self-correct from.

4. **Executes the tool** in the Python runtime, where the actual domain logic runs — HMAC signature computation for FortiSOAR authentication, asynchronous two-step log searches on FortiAnalyzer, RFC1918 IP classification, whitelist CIDR matching, Netbox prefix hierarchy lookups, and structured result formatting.

5. **Returns compact results** to the LLM as structured tool_result blocks, carefully formatted to maximize information density while minimizing token consumption. The LLM receives aggregated statistics, labeled data, escalation warnings, and pre-computed correlation query suggestions rather than raw API responses.

6. **Logs the complete session** — every tool call, every result, every LLM response, and the full tool definition array — to a JSON session file for audit and debugging.

### The LLM Layer

The system uses **Gemma4-26B-A4B**, a Mixture-of-Experts model with 26 billion total parameters but only approximately 4 billion active parameters per inference pass. It runs locally on a vLLM server, eliminating cloud API costs and data sovereignty concerns — no alert data or log content ever leaves the organization's network.

The model communicates with the harness through the OpenAI-compatible chat completion API with non-streaming mode (`OH_STREAM=false`), which prevents tool-call parsing failures caused by network equipment re-chunking SSE streams across network hops. The model's temperature is set to 0.2 for production batch operations, prioritizing consistency over creativity.

A critical design decision is the **tool filtering** mechanism. The OpenHarness framework ships with 44+ built-in tools. The SOC wrapper filters this down to only the 8 tools relevant to security triage before any API call is made: `fortisoar_list_alerts`, `fortisoar_get_alert`, `fortisoar_resolve_alert`, `fortisoar_escalate_alert`, `faz_query_logs`, `faz_query_security_events`, `fortisiem_get_triggering_events`, and `netbox_lookup_ip`. This reduces token consumption on every turn and eliminates the possibility of the model accidentally invoking irrelevant tools.

### The SOC Tool Layer

This is where the system's actual intelligence resides. Each tool encodes specific domain expertise that would otherwise require the LLM to reason from first principles — a task that small models handle unreliably.

**FortiSOAR Tools:**

- **List Alerts** queries FortiSOAR for open Critical and High severity alerts across all configured sources. The query is pre-scoped by environment variables to the configured tenant and source set (e.g., `IS_FAZ_MIS_Cloud,FortiCloud FortiSIEM`) — a fail-closed design that prevents cross-tenant data leakage on shared FortiSOAR instances. Supports multiple alert sources via comma-separated `FORTISOAR_SOURCE` configuration.

- **Get Alert** fetches the full details of a specific alert and transforms the raw FortiSOAR response into a compact summary optimized for LLM consumption. The summary places **correlation hints** first — pre-extracted structured fields (source/destination IPs with INTERNAL/EXTERNAL labels computed by Python's `ipaddress` module, detection timestamp, FortiGate action) followed by copy-pasteable suggested correlation queries. For FortiSIEM-originated alerts, the hints include the FortiSIEM incident ID, MITRE ATT&CK tactic/technique, and a `fortisiem_get_triggering_events` query instead of the FAZ 4-query pattern. This tool also performs the **whitelist auto-close** check: if the alert's source IP matches a human-curated whitelist, the tool closes the alert immediately via the FortiSOAR API and returns a data-starved stop message that prevents the LLM from investigating further.

- **Resolve Alert** closes an alert in FortiSOAR with a closure reason and detailed closure notes. The tool enforces a closure reason allowlist (preventing the model from using deprecated reasons like "False Positive"), silently substitutes a safe default ("Tasks Completed") when the model picks an invalid reason, prepends a `[Triaged by BIS-AI Analyst — Gemma4-26B-A4B]` identification marker to every closure note, and automatically appends Netbox asset ownership context. Source-specific closure notes templates ensure consistent factual tone across FAZ and FortiSIEM alerts.

- **Escalate Alert** transitions an alert from "Open" to "Investigating" status when the agent determines that human review is required. Before changing the status, the tool sends an **HTML-formatted escalation email** to the SOC team via SMTP — delivering the full investigation findings, FortiSOAR link, severity badge, and suggested actions directly to a Microsoft Teams channel and the SOC inbox. This ensures the human analyst is actively notified, not just passively waiting to check a queue. The tool also appends Netbox asset context to the escalation findings.

**FortiAnalyzer Tools:**

- **Query Logs** performs asynchronous two-step log searches against FortiAnalyzer (create search task, poll for completion, fetch results). The tool internally fetches up to 500 log entries for statistical aggregation but presents only 50 sample entries to the LLM, along with computed summary statistics: top source/destination IPs, top destination ports, action breakdown, byte counts, and application distribution. The SUMMARY header honestly reports "aggregated over N of M entries" so the model (and the human auditor) knows the analysis is based on a representative sample, not the full dataset. When the query results contain **escalation-triggering patterns** — inbound or outbound accepted traffic, or suspicious ports (P2P/BitTorrent 6881-6999, IRC, Tor) — the tool appends a prominent `⚠ ESCALATION REQUIRED` warning at the closest possible position to where the LLM makes its decision.

- **Query Security Events** aggregates IPS attack events, antivirus detections, web filter blocks, DLP incidents, application control events, and anomaly detections within a specified time window. Results are presented as counts per event type with top event names and source IPs.

**FortiSIEM Tools:**

- **Get Triggering Events** fetches the raw syslog events that triggered a FortiSIEM incident via the REST JSON API (start → poll `progressPct` → fetch results). This is the FortiSIEM equivalent of `faz_query_logs` — it gives the LLM the actual evidence to analyze. The tool presents the events in the same compact format: SUMMARY stats (event types, severities, source/dest IPs, users, actions, reporting devices) followed by SAMPLE EVENTS with raw syslog lines. The LLM reads the raw logs, identifies behavioral patterns (e.g., "10 Postponed publickey events followed by 40 Accepted publickey — SSH pre-auth, not brute force"), and makes an informed triage decision based on the actual evidence rather than the alert's label.

**Netbox Tool:**

- **Lookup IP** queries the Netbox IPAM for IP ownership information. The lookup first attempts an exact IP match, then walks up the prefix hierarchy from /24 → /20 → /16, collecting descriptions and roles at each level. This multi-level approach captures both specific location context (e.g., "100.65.208.0/20: Frankfurt") and broader service context (e.g., "100.65.0.0/16: SASE") that would be missed by a single-level query. The tool is available as a standalone tool the LLM can call explicitly, AND is called automatically by the resolve and escalate tools to append asset context to closure notes and escalation findings.

**Whitelist Engine:**

The IP/CIDR whitelist is a human-curated YAML file, reviewed and version-controlled through git, that identifies IP addresses whose traffic patterns are known to trigger security alerts but represent authorized activity. When an alert's source IP matches a whitelist entry, the system bypasses the LLM entirely — the tool layer closes the alert directly with a deterministic audit trail that includes the whitelist entry's justification, the author who added it, the date it was added, and the git blob SHA of the whitelist file at the time of closure. CIDR matching uses Python's `ipaddress` module with a safety floor of /16 (preventing accidental auto-close of millions of alerts from a typo'd broad CIDR).

## Alert Processing Workflow

Each alert is processed in a **fresh, isolated LLM conversation** to prevent cross-alert context contamination. The **bis-soc** wrapper script orchestrates this by invoking the OpenHarness framework once per alert — either for a specific alert ID (`bis-soc Alert-NNN`) or in drain mode (`bis-soc`) processing every open alert sequentially.

**Step 1 — Alert Retrieval:** The LLM calls the Get Alert tool with the alert identifier. The tool fetches the alert from FortiSOAR, applies tenant and source authorization checks, performs the whitelist lookup, classifies all IP addresses as INTERNAL or EXTERNAL using RFC1918 range checks, detects whether the alert originated from FortiAnalyzer or FortiSIEM, and returns the compact summary with source-appropriate correlation hints.

**Step 2 — Whitelist Check:** If the alert's source IP matches the whitelist, the tool has already closed it. The LLM receives a data-starved stop message containing no IP addresses, no timestamps, no ADOM names — nothing it could use to call follow-up tools. The LLM outputs a one-sentence confirmation and the conversation ends. This path completes in approximately 3 seconds.

**Step 3 — Evidence Correlation:**
- **FAZ-originated alerts:** The LLM executes exactly four correlation queries suggested by the Get Alert tool's correlation hints: (1) all security events in the 10-minute window after detection, (2) source IP traffic in the 10-minute window after detection, (3) source IP traffic in the 10-minute window before detection, and (4) destination IP traffic in the 10-minute window after detection.
- **FortiSIEM-originated alerts:** The LLM executes one query — `fortisiem_get_triggering_events` — which returns the raw syslog events behind the incident. The LLM analyzes the event patterns: login success/failure sequences, authentication methods, timing, source IPs, and users.

**Step 4 — Verdict (escalation triggers checked FIRST):**
The system prompt instructs the model to check escalation triggers before considering resolution:
- **Suspicious accepted traffic** on unusual ports (P2P/BitTorrent 6881-6999, IRC, Tor) triggers mandatory escalation
- **EXTERNAL → INTERNAL** with `action=accept` and data transfer triggers escalation
- **INTERNAL → EXTERNAL** with `action=accept` and data transfer triggers escalation (possible C2/exfiltration)
- **EXTERNAL → EXTERNAL** with `action=accept` to suspicious destinations triggers escalation
- If no escalation triggers match AND the evidence shows the threat was blocked or benign → resolve with detailed closure notes

The FAZ tool output reinforces these rules with prominent `⚠ ESCALATION REQUIRED` warnings at the decision point, countering the instruction-fade problem inherent in small-model multi-turn conversations.

**Step 5 — Resolution or Escalation:**
- **Resolve:** The tool prepends the BIS-AI triage marker, appends Netbox asset context, and writes the closure notes to FortiSOAR. The alert transitions to Closed.
- **Escalate:** The tool sends an HTML-formatted email to the SOC Teams channel and inbox with full investigation findings, then transitions the alert to Investigating in FortiSOAR. The alert leaves the automated processing queue.

## Escalation Notification System

When the AI agent determines an alert requires human review, the escalation tool sends a structured notification via SMTP to the configured Microsoft Teams channel and SOC email inbox. The email includes:

- **Alert details** in a formatted table: alert ID, name, severity (color-coded badge), and a clickable FortiSOAR link
- **AI investigation summary** in a monospace code block: the full findings with [LOG] citations, event counts, IP addresses, and behavioral analysis
- **Suggested actions** as a numbered checklist: open FortiSOAR, review findings, examine raw logs, determine true/false positive, update status
- **Netbox asset context** appended automatically by code

The notification is sent BEFORE the FortiSOAR status change — if the email fails, the alert still transitions to Investigating (recoverable: a missed notification is less dangerous than a missed status change). The sender address is derived from the SMTP username with a hard `@fortinet.com` suffix to prevent spoofing.

## Design Principles

**Intelligence lives in the tool layer, not in the model.** Every safety-critical decision is enforced in Python code, not in the system prompt. IP classification uses the stdlib `ipaddress` module. Closure reason validation uses an allowlist with deterministic substitution. Whitelist matching uses exact IP comparison and CIDR containment checks. Escalation warnings are injected by the FAZ tool based on deterministic port and action analysis. The system prompt serves as a behavioral guide for the average case; the code serves as an inviolable guardrail for every case.

**One alert per conversation.** Each alert is processed in a completely isolated LLM session with a fresh context window. This eliminates constraint drift (where the model gradually relaxes its rules over multiple alerts), cross-alert state contamination, and context window exhaustion.

**Non-streaming API calls.** The system uses `OH_STREAM=false` to prevent tool-call parsing failures caused by network equipment (routers, proxies) re-chunking SSE streams across network hops. Each API call returns the complete response in a single JSON body — no chunking sensitivity, no parser fragility.

**Compact tool output with honest reporting.** FortiAnalyzer can return thousands of log entries for a single query. The tool layer aggregates these into summary statistics computed over 500 entries and presents 50 representative samples to the LLM. The summary includes honesty markers ("aggregated over 500 of 6,045 entries") that the system prompt requires the model to propagate into its closure notes as "sampled N of M."

**Fail-closed on authorization, fail-open on enrichment.** FortiSOAR tenant scoping, source scoping, and alert status checks are fail-closed — the tool refuses to operate if any authorization check fails. Netbox ownership lookups are fail-open — if the enrichment source is unavailable, alert processing continues without it.

**Multi-source dispatch.** The `FORTISOAR_SOURCE` configuration supports comma-separated values for multiple alert sources. The correlation hints in `fortisoar_get_alert` automatically dispatch to the correct tool set based on the alert's `sourceType`: FAZ alerts get 4 FAZ queries; FortiSIEM alerts get 1 triggering-events query. The LLM follows the suggested queries without needing to understand the dispatch logic.

**Audit trail as a first-class feature.** Every AI-triaged closure carries a `[Triaged by BIS-AI Analyst — Gemma4-26B-A4B]` marker. Every whitelist auto-closure includes the git blob SHA of the whitelist file. Every session is logged as a JSON file containing the full conversation, all tool calls and results, and the complete tool definition array. Reopened alerts do not show stale closure notes to the LLM — preventing the model from parroting previous verdicts.

## Production Results

In production testing against real FortiSOAR alerts from multiple sources:

| Metric | Result |
|--------|--------|
| Total alerts triaged | 100+ |
| Alert sources | FortiAnalyzer + FortiSIEM |
| Whitelist auto-close accuracy | 100% (0 false negatives) |
| Avg time per alert (FAZ, with correlation) | 30–60 seconds |
| Avg time per alert (FortiSIEM, triggering events) | 15–30 seconds |
| Avg time per alert (whitelist hit) | ~3 seconds |
| Escalation on suspicious accepted traffic | Correctly triggered (P2P, C2 patterns) |
| FortiSIEM behavioral analysis | Correct (SSH publickey pre-auth identified as non-brute-force) |
| Duplicate detection | Working (skips redundant queries) |
| Escalation email delivery | Working (SMTP → Teams channel + SOC inbox) |
| [LOG] citation compliance | Working via tool-output reminder |
| IP classification accuracy | 100% (code-based, not LLM-based) |
| Netbox asset enrichment | Working (multi-level prefix hierarchy /24→/20→/16) |

### Notable Investigation Examples

**FortiSIEM Brute-Force False Positive:** Alert "Brute force logon success from 10.243.5.146" — the agent fetched 50 raw syslog events, identified that all 10 "failed" logins were `Postponed publickey [preauth]` (normal SSH pre-authentication behavior, not password failures), all 40 successful logins used the same RSA key fingerprint, and correctly concluded this was automated SSH key-based administration, not a brute-force attack. Resolved with detailed evidence.

**P2P Traffic Escalation:** Alert "Compromised host 10.125.19.31" — the agent detected BitTorrent traffic on ports 6881/6998 with `action=accept` from an internal host (Netbox: OpenStack server) to multiple external destinations. The tool-output escalation warning fired on both the suspicious port pattern and the INTERNAL→EXTERNAL accept pattern. The agent escalated with full findings delivered to the Teams channel.

**C2 Traffic Detection:** Alert involving traffic to a known C&C IP — the agent identified extensive PING sweep activity (149,350+ entries in a 10-minute window) from an internal host, including large data transfers (425MB received). Escalated with behavioral analysis noting the pattern as "consistent with reconnaissance or C2 heartbeats."

## Technology Stack

| Component | Technology | Role |
|-----------|-----------|------|
| LLM | Gemma4-26B-A4B via vLLM | Reasoning engine, tool selection, evidence interpretation |
| Framework | OpenHarness (Python) | Tool-calling loop, permission gating, session logging |
| Alert Platform | FortiSOAR | Alert lifecycle management, multi-source orchestration |
| Log Analytics | FortiAnalyzer | Traffic logs, security events (FAZ-originated alerts) |
| SIEM | FortiSIEM | Triggering events, raw syslogs (FortiSIEM-originated alerts) |
| Asset Management | Netbox | IP ownership lookup, prefix hierarchy enrichment |
| Notification | SMTP → Microsoft Teams | Escalation email delivery (HTML formatted) |
| Whitelist | YAML + Pydantic + ipaddress | Deterministic auto-close for known-benign sources |
| Deployment | Docker (optional) | Container-ready with Dockerfile and docker-compose |
| Version Control | Git | Whitelist SHA audit trail, session logging |

## Roadmap

**Completed:**
- [x] FortiSOAR integration (list, get, resolve, escalate with multi-source support)
- [x] FortiAnalyzer integration (async log search, security events, 500-entry aggregation)
- [x] FortiSIEM integration (triggering events via REST API, raw syslog analysis)
- [x] IP/CIDR whitelist with auto-close and data starvation
- [x] Netbox IP ownership lookup (multi-level prefix hierarchy /24→/20→/16)
- [x] Escalation email notifications (HTML formatted, SMTP → Teams + SOC inbox)
- [x] Batch processing wrapper (bis-soc, single + drain modes)
- [x] Tool filtering (44+ → 8 SOC tools)
- [x] IP classification labels (INTERNAL/EXTERNAL via ipaddress module)
- [x] [LOG] citation enforcement via tool-output reminders
- [x] Escalation warnings in FAZ tool output (P2P, outbound accept, suspicious ports)
- [x] BIS-AI triage marker on all closures
- [x] Session logging with full tool array
- [x] Non-streaming API mode (OH_STREAM=false)
- [x] Source-specific closure notes templates (FAZ factual, FortiSIEM factual, unknown flexible)
- [x] Stale closure notes hidden from reopened alerts

**Planned:**
- [ ] Code-level action gate in resolve tool (deterministic refuse-to-close on suspicious patterns)
- [ ] Interactive TUI mode for analyst-driven investigation of escalated cases
- [ ] CMDB-driven asset context enrichment beyond Netbox
- [ ] Daily digest email summarizing bot activity
- [ ] Multi-vendor support (Palo Alto, Cisco) via the existing tool architecture
- [ ] Confidence-gated escalation with structured verdict output
