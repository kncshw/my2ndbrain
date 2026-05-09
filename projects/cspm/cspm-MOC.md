# CSPM — Map of Content

Vulnerability management platform for public IP subnets. Orchestrates Nessus scans, streams findings through Kafka, creates FortiSOAR tickets, and distributes reports.

## Status
- Core scan pipeline (email path): **In production**
- Kafka streaming pipeline: **In production**
- Scan discovery (NetBox → scan system): **In production**
- Weekly analytics report: **In production**
- Dashboard: **Not built** (see [[red-agent-MOC]] — red-agent has a CTEM dashboard that could serve this data)

## Documents
- [[cspm-system-design]] — architecture, integrations, data flow, project layout
- [[cspm-workflows]] — all 9 workflows: what triggers them, step-by-step, outputs
- [[cspm-execution]] — setup, CLI commands, cron schedule, .env template, artifact structure

## Architecture in one line

```
NetBox subnets → Nessus scans → Kafka events → FortiSOAR tickets + email reports
```

Two parallel paths:
- **Legacy email path** (`run-daily-report`): Nessus emails CSV → parse → filter → ticket → report
- **Kafka streaming path** (`run-daily-scan-ingest` → `run-daily-scan-consume`): Nessus API → Kafka → ticket → report

## Key Design Decisions
- **Filter list** (`filter_list.csv`) — human-curated suppressions. Never written by automation.
- **Subnet categorization** — NetBox description keywords map to internal asset groups (see `subnet_processor.py`)
- **Kafka topic per /24** — each subnet gets its own topic; IP as message key for partition locality
- **No LLM** — purely deterministic pipeline; no AI reasoning component

## Related
- [[red-agent-MOC]] — shares NetBox integration; red-agent dashboard could visualize CSPM data
- [[SOC-agent-MOC]] — FortiSOAR tickets created here feed into SOC triage
