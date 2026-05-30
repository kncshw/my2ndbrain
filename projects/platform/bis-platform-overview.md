# BIS Platform — AI-Driven Security Operations on Kubernetes

> Umbrella project bundling three locally-hosted, LLM-powered security services —
> exposure management, SOC alert triage, and threat-intel briefing — deployed as a
> single Helm-managed application onto a k3s Kubernetes cluster. All AI inference
> runs against an internal vLLM-hosted Gemma model, so **no security data ever
> leaves the network**.

---

## Formal Introduction (LinkedIn / Résumé)

**BIS Platform** is a self-hosted, AI-native security operations platform I designed and
built end-to-end, unifying three autonomous LLM agents behind a single Kubernetes
deployment. It applies large language models to three high-toil security workflows —
**Continuous Threat Exposure Management (CTEM)**, **SOC alert triage**, and
**cyber-threat-intelligence briefing** — while keeping every byte of sensitive data
inside the corporate network by running all inference on a locally-hosted **Gemma model
served through vLLM** (zero external API cost, zero data egress).

The platform is delivered as an **umbrella Helm chart** composed of five sub-charts
(three application services, shared infrastructure, and an observability stack) and runs
on a single-binary **k3s** cluster. Container images are built locally and pushed to an
in-cluster registry; long-running services run as Kubernetes **Deployments** behind an
**Ingress**, while scheduled agents run as **CronJobs**. Shared **PostgreSQL** and
**Redis** back the services, and a built-in observability layer (**Loki + Promtail +
Grafana**) is paired with an **LLM-based log observer** that triages anomalies and emails
on-call alerts.

A defining engineering principle across all three agents is that **intelligence lives in
the deterministic tool layer, not in the model**. The LLM is given a small, well-scoped
job — pick a tool, fill in JSON arguments, summarize results — while authentication,
CIDR/IP classification, log aggregation, whitelist matching, and audit-trail generation
run in tested Python. This makes the system reliable even with a small, locally-hosted
model, and keeps every automated action auditable.

**Key technologies:** Kubernetes (k3s), Helm, Docker, Python 3.12, FastAPI, React +
TypeScript (Ant Design), Apache Kafka, PostgreSQL, Redis, vLLM / Gemma, Loki/Promtail/
Grafana, Nessus, Nmap, Kali, FortiSOAR, FortiAnalyzer, FortiSIEM, FortiRecon, NetBox.

**Highlights:**
- Three production-style AI security agents unified under one Helm umbrella chart on k3s.
- 100%-local LLM inference (vLLM/Gemma) — no third-party API, no data egress.
- Tool-layer-centric agent design that keeps a small model reliable and auditable.
- Event-driven exposure-management pipeline built on Kafka, with a FastAPI + React
  operations dashboard.
- Self-monitoring: an LLM observer reads aggregated logs and escalates anomalies.

---

## Architecture at a Glance

```
                      ┌──────────────────────────────────────────────┐
                      │            bis-platform (k3s cluster)          │
                      ├──────────────┬──────────────┬─────────────────┤
   Web / dashboard ──▶│   bis-ctem   │ bis-soc-agent│ bis-intel-agent │
                      │  (API + UI)  │  (CronJob)   │   (CronJob)     │
                      ├──────────────┴──────────────┴─────────────────┤
                      │  infrastructure: PostgreSQL · Redis            │
                      ├──────────────────────────────────────────────-┤
                      │  observability: Loki · Promtail · Grafana      │
                      │                 connectivity-checker           │
                      │                 LLM observer / daily report    │
                      └──────────────────────────────────────────────-┘
                                          │
                                          ▼
                       external: Kafka · Nessus · Nmap · Kali · vLLM
                                  FortiAnalyzer · FortiSOAR · FortiSIEM
                                  FortiRecon · NetBox · Reddit · NVD · SMTP
```

| Service | K8s workload | Purpose |
|---|---|---|
| **bis-ctem** | Deployment (API+UI) + CronJobs | Continuous Threat Exposure Management — vulnerability scanning, exposure analytics, and an autonomous red-team agent |
| **bis-soc-agent** | CronJob (every ~2h) | AI SOC analyst — triages FortiSOAR alerts by correlating FortiAnalyzer / FortiSIEM / Lacework evidence |
| **bis-intel-agent** | CronJob (daily 06:00 PDT) | Cyber-intel briefing — Reddit + FortiRecon + NVD → LLM classification → HTML report → email |
| **infrastructure** | StatefulSet + Deployment | Shared PostgreSQL 16 and Redis 7 |
| **observability** | Deployment + DaemonSet + CronJobs | Loki/Promtail/Grafana, connectivity checks, LLM-based anomaly triage |

---

## Agent 1 — bis-ctem (Continuous Threat Exposure Management)

`bis-ctem` is the largest service and is itself made of several cooperating components.
It runs a **FastAPI** backend serving a **React + TypeScript (Ant Design)** dashboard,
backed by PostgreSQL, and orchestrates work over an **Apache Kafka** event pipeline. It
has two AI/automation halves: the **CSPM engine** (scanning + exposure management
workflows) and the **Red Team agent** (autonomous active probing).

### 1a. CSPM Engine — *built from several discrete tasks*

The CSPM engine (`bis-ctem/cspm/`) is the exposure-management core. Rather than one
monolith, it is a collection of independent **workflow tasks**, each exposed as a CLI
subcommand (`cspm/cli.py`) and scheduled as its own cron/CronJob. They share a common
event bus (Kafka), scanner integrations (Nessus, Nmap), and asset context (NetBox IPAM),
and every run writes an audit row to the `workflow_runs` table.

| Task (CLI command) | What it does |
|---|---|
| **Scan discovery** (`run-scan-discovery`) | Pulls /24 subnets from NetBox IPAM, finds ranges not yet covered by a Nessus scan, and reports the gaps — keeps scan coverage complete as the network changes. |
| **Vulnerability ingest** (`run-daily-scan-ingest`) | Pulls daily Nessus results, filters/normalizes vulnerabilities, groups ports by IP, extracts CVEs, and **produces events to Kafka** (per-subnet topics). |
| **Vulnerability consume** (`run-daily-scan-consume`) | Consumes the per-subnet vulnerability events from Kafka, enriches with NetBox ownership, and generates/distributes the daily vulnerability summary (email + tickets). |
| **Open-port check** (`run-open-port-check`) | Runs targeted Nessus plugins against public IPs to detect newly exposed ports, then reports/tickets them. |
| **Daily brute-force ticket** (`run-bruteforce-ticket`) | Consumes `bruteforce-vulnerable` confirmation events from Kafka and opens **FortiSOAR tickets** automatically. |
| **Scanner-statistics ingest** (`run-scanner-statistics-ingest`) | Computes scan + weekly-vulnerability statistics and publishes them to the `scanner-analytics` Kafka topic. |
| **Report-data preparation** (part of `run-weekly-report`) | Consumes analytics topics from Kafka and materializes CSV datasets for reporting. |
| **Analytic report** (part of `run-weekly-report`) | Renders the weekly vulnerability analytics report (HTML template) from the prepared CSV data. |
| **Daily scan report** (`run-daily-report`) | Parses scan-result emails, merges/filters data, enriches with NetBox, and distributes the daily report + tickets. |
| **Health check** (`run-health-check`) | Checks Nessus scanner status/health and emails a health report. |
| **Daily routine** (`run-daily-routine`) | Convenience composite that chains the daily report, health check, open-port check, and scan ingest into one morning run. |

Supporting layers under `cspm/`: `scanners/` (Nessus + Nmap implementations and a
vendored `py_nessus_pro` client), `integrations/` (NetBox, IPAM, FortiSOAR, Redis cache),
`reporting/` (email, tickets, statistics, HTML analytics), `data/` (filtering, merging,
subnet processing), and `cron/` (shell wrappers for each scheduled task).

### 1b. Red Team Agent — autonomous active probing

`bis-ctem/redteam/` is an autonomous offensive-security agent that turns passively
discovered exposure into actively validated findings. Its flow:

1. **Phase 1 — discover:** consume active-subnet findings from Kafka (high concurrency)
   and enrich each IP with NetBox ownership context.
2. **Phase 2 — probe:** for each subnet, run **service-specific probes** (HTTP, SSH,
   RDP/VNC) that execute against a sandboxed **Kali** container. The HTTP probe uses a
   two-step LLM workflow — identify the app and its auth status, then, if unauthenticated,
   write an escalation note and alert a human.
3. **Escalate:** confirmed exposures are scored against `escalation_rules.yaml`, raised
   as **FortiSOAR tickets**, and notified.

A legacy `--mode agent` path runs a full Gemma tool-calling loop (the model drives Kali
tool calls until the investigation is complete); the default modern path uses the
structured per-service probes. Redis caches findings (48h TTL) so probing can be re-run
without re-consuming Kafka.

### 1c. Dashboard API + UI

A FastAPI backend (`api/`) exposes routers for assets, vulnerabilities, scans, tickets,
escalations, analytics, agent sessions, Kafka feed, subnets, and remote access, fronted
by a React/Ant Design SPA with Overview, Assets, Vulnerabilities, Red Team, Tickets, and
Analytics views. Rate-limited (slowapi), CORS-aware, and serving the built frontend as
static assets.

---

## Agent 2 — bis-soc-agent (AI SOC Analyst)

`bis-soc-agent` (a.k.a. **OpenHarness SOC**) is an AI SOC analyst that automatically
triages security alerts. It pulls open Critical/High alerts from **FortiSOAR**, then —
**one alert per fresh LLM conversation** to prevent constraint drift — correlates
evidence from **FortiAnalyzer**, **FortiSIEM**, and **Lacework**, and either resolves or
escalates each alert. Inference runs locally on **Gemma via vLLM**, harnessed through
structured JSON tool calling.

Design highlights:
- **Intelligence in the tool layer** — HMAC auth, CIDR/IP classification, log
  aggregation, whitelist matching, and audit-trail generation are deterministic Python;
  the LLM only picks tools and summarizes.
- **Whitelist auto-close** — human-curated YAML of IPs/CIDRs closes known-benign alerts
  in code (bypassing the LLM), with a git-SHA audit trail.
- **Safety guardrails** — tenant/source scoping (fail-closed), a closure-reason
  allowlist, a `[Triaged by BIS-AI Analyst]` marker on every closure, and tool filtering
  (44 framework tools → 7 SOC tools) to cut token waste and model confusion.
- **Observability** — full session logging, enforced `[LOG]` citations, and honest
  "sampled N of M" reporting.

Runs as a Kubernetes CronJob (~every 2h); also ships a CLI (`bin/bis-soc`,
`bin/soc-report`) and Docker Compose for local use. See `bis-soc-agent/README.md` and
`bis-soc-agent/docs/` for the full design.

---

## Agent 3 — bis-intel-agent (Cyber-Intel Briefing)

`bis-intel-agent` is an automated threat-intelligence briefing agent. Daily it:

1. **Collects** trending posts from Reddit (PRAW, e.g. `r/cybersecurity`) and pulls
   **FortiRecon** findings; weekly it also assembles a top-posts digest.
2. **Classifies & enriches** posts with an LLM (Breaches, Leaks, Vulnerabilities, …),
   optionally scraping/summarizing linked articles, with Redis-backed dedup so the same
   post isn't processed twice.
3. **Reports** a clean **HTML daily briefing** (and weekly report) and emails it.

Originally derived from the open-source `reddit-ai-trends` project, trimmed to a focused
personal/team intel feed. Runs as a Kubernetes CronJob (daily 06:00 PDT); also runnable
via Docker Compose / cron. See `bis-intel-agent/README.md`.

---

## Cross-Cutting: Observability

The observability sub-chart provides:
- **Loki + Promtail + Grafana** — centralized log aggregation, shipping, and dashboards.
- **Connectivity checker** — periodic liveness checks of external dependencies, logged
  with `log_type="connectivity"` status fields.
- **LLM observer** (`observability/llm_observer.py`) — every ~10 minutes queries Loki for
  anomalies, sends them to Gemma for triage, and emails on `ALERT` with a per-service
  2-hour cooldown to prevent flooding.
- **LLM daily report** — a daily roll-up of platform health/activity.

---

## Tech Stack

- **Orchestration:** k3s (single-binary Kubernetes — control plane, kubelet, flannel CNI,
  containerd in one process), Helm umbrella chart (5 sub-charts), in-cluster Docker
  registry (`bis-ptmgmt:5000`).
- **Backends:** Python 3.12, FastAPI, SQLAlchemy + Alembic, Apache Kafka, PostgreSQL 16,
  Redis 7.
- **Frontend:** React + TypeScript, Vite, Ant Design.
- **AI:** vLLM serving an internal Gemma model — all inference local, no data egress.
- **Security tooling:** Nessus, Nmap, Kali (sandboxed container), FortiSOAR,
  FortiAnalyzer, FortiSIEM, FortiRecon, Lacework, NetBox.
- **Observability:** Loki, Promtail, Grafana.

## Repository Layout

```
bis-platform/
├── bis-ctem/              # CTEM service: FastAPI + React, CSPM engine, Red Team agent, Kafka pipeline, observability
│   ├── api/               # FastAPI backend (routers, models, schemas)
│   ├── cspm/              # CSPM engine — workflows/, scanners/, integrations/, reporting/, data/, cron/
│   ├── redteam/           # Autonomous red-team agent — probes/, tools/ (Kali, Kafka, NetBox, FortiSOAR)
│   ├── pipeline/          # Kafka producer/consumer
│   ├── observability/     # LLM observer, connectivity checker, daily report
│   ├── frontend/          # React + TS dashboard
│   └── kali-sandbox/      # Sandboxed Kali exec server
├── bis-soc-agent/         # AI SOC analyst (OpenHarness SOC)
├── bis-intel-agent/       # Reddit/FortiRecon/CVE intel briefing agent
├── deploy/
│   ├── k8s/               # Raw manifests (namespaces, secret templates)
│   └── helm/bis-platform/ # Umbrella Helm chart + 5 sub-charts
├── Makefile               # build-*, deploy, namespaces, logs-*
├── DEPLOY.md              # Deploy + secret-handling walkthrough
└── README.md              # Deployment-focused readme
```

## Deployment & Secrets

Deployed via `helm upgrade --install bis-platform` against a values file; images built
with `make build-*`. Real credentials never enter git — the repo holds only `*.example`
templates with `CHANGE_ME` placeholders, filled locally from the team password manager.
The full local-mock and production walkthroughs (including the one manual
`fortisoar-keys` secret) are in [`DEPLOY.md`](DEPLOY.md).
```bash
make build-bis-ctem build-bis-soc-agent build-bis-intel-agent VERSION=stable
make namespaces
helm upgrade --install bis-platform deploy/helm/bis-platform \
  -f deploy/helm/bis-platform/values.yaml \
  -f deploy/helm/bis-platform/values.mock.yaml
```
