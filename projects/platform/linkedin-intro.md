# BIS Platform — LinkedIn Introduction

> Ready-to-paste profile copy (Featured project / Experience entry). LinkedIn does not
> render markdown — paste as plain text; the `**bold**` markers and `•` bullets are for
> readability here.

---

**BIS Platform — AI-Driven Security Operations on Kubernetes**

Designed and built an end-to-end, self-hosted security platform powered by locally-hosted LLMs, unifying autonomous AI agents that automate high-toil security workflows. All model inference runs on an internal vLLM/Gemma stack — zero external API cost and zero data egress, a hard requirement for sensitive security data.

**The agents:**

• **CSPM engine (exposure management)** — Drives the full exposure lifecycle as a set of independent, scheduled workflows: discovers unscanned subnets from IPAM, runs Nessus/Nmap scans, and ingests/filters/analyzes vulnerabilities over a Kafka pipeline — auto-generating daily reports, open-port and brute-force tickets, and weekly analytics.

• **Red-team agent (active validation)** — Turns passively discovered exposure into actively validated findings: consumes live-subnet findings, runs service-specific probes (HTTP/SSH/RDP) from a sandboxed Kali container, and escalates confirmed exposures as tickets. The HTTP probe uses a two-step LLM workflow to identify the app and its auth status before flagging unauthenticated services. Both surface through a FastAPI + React/TypeScript operations dashboard.

• **SOC agent (alert triage)** — An AI SOC analyst that pulls open Critical/High alerts and triages each one in an isolated LLM conversation, correlating evidence across multiple log and detection sources before auto-resolving or escalating — with whitelist auto-close, fail-closed scoping, and a full audit trail on every action.

• **Threat-intel agent (daily briefing)** — Collects trending posts and recon findings, classifies and enriches them with an LLM (breaches, leaks, vulnerabilities), and emails a clean HTML intelligence briefing on a daily/weekly cadence.

A defining design principle across all agents: **intelligence lives in the deterministic tool layer, not the model** — authentication, IP/CIDR classification, log correlation, and audit-trail generation run in tested Python, keeping a small local model reliable enough for production and every automated action auditable.

**Deployment (Kubernetes / Helm):**

• Packaged the whole platform as a single Helm umbrella chart (five sub-charts) deployed to a single-binary k3s cluster.

• Long-running services run as Deployments behind an Ingress; scheduled agents run as CronJobs; shared PostgreSQL and Redis back all services.

• Container images built locally and pushed to an in-cluster registry; secrets templated out of git and injected at deploy time.

• Built-in observability — Loki/Promtail/Grafana plus an LLM-based log observer that triages anomalies and escalates to on-call.

**Stack:** Kubernetes (k3s), Helm, Docker, Python, FastAPI, React/TypeScript, Kafka, PostgreSQL, Redis, vLLM/Gemma, Loki/Promtail/Grafana.
