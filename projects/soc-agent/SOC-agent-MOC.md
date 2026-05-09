# SOC Agent — Map of Content

AI-powered SOC alert triage system. Automatically investigates FortiSOAR alerts using Gemma4-26B-A4B via OpenHarness. Philosophy: **intelligence in the tool layer, not the model.** → [[llm-vs-code-driven]]

## Status
- Core alert investigation loop: **In production** (100+ alerts triaged)
- Lacework CNAPP integration: **Complete**
- Escalation tool (SMTP): **Ready to implement** — blocked on SMTP credentials
- Netbox IP enrichment: **Ready to implement** — blocked on API token
- Cron-driven autonomous mode: **Planned**

## Documents

### Architecture
- [[soc-system-design]] — master spec: tools, workflow, design principles, production results
- [[soc-cmdb-and-fine-tuning-decision]] — why CMDB over fine-tuning; 7 conditions before fine-tuning is considered
- [[agent-design-comparison]] — red-agent vs soc-agent design philosophy (shared principle)

### Configuration
- [[soc-config-tenant-source]] — FORTISOAR_TENANT and FORTISOAR_SOURCE scoping
- [[soc-analyst-prompt]] — full system prompt (reference)
- [[soc-analyst-prompt-min]] — minimal system prompt (production)

### Features (planned/in-progress)
- [[soc-escalation-design]] — escalate_alert tool spec (SMTP + FortiSOAR status transition)
- [[soc-escalation-experiment-plan]] — testing protocol; code-level action gate; temperature A/B
- [[soc-netbox-integration-plan]] — IP ownership lookup via Netbox

### Operations
- [[SOC-agent-execution-log]] — runbook: setup, run command, example execution, env vars
- [[soc-weekly-report]] — bin/soc-report: 7-day triage summary with metrics

## Related
- [[llm-vs-code-driven]] — the design principle this project is built on
- [[Gemma4_Deployment]] — the model powering this agent (same GB10 hardware)
- [[GB10-MOC]] — GB10 project that serves the model
