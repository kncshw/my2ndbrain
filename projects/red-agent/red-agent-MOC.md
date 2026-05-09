# Red Agent — Map of Content

Continuous Threat Exposure Management (CTEM) platform. Two components:
1. **bis-red-agent** — headless probing engine (Python discovery + LLM reasoning)
2. **BIS CTEM Dashboard** — PostgreSQL + FastAPI + React visibility layer

Design principle: **Python drives discovery, LLM synthesizes results.** → [[llm-vs-code-driven]]

## Status
- bis-red-agent core probing engine: **In production**
- App identification pipeline (Steps 1–4): **Planned** → [[app_identification_design]]
- Dashboard (DB + API + React): **Done** → [[dashboard_DB_design]]
- Test plan: **Defined, execution pending** → [[test_plan]]

## Documents

### Architecture
- [[agent-design-comparison]] — bis-red-agent vs oh-soc-agent: why Python drives discovery, not the LLM
- [[app_identification_design]] — 5-step deterministic app ID pipeline; LLM only for auth + escalation

### Dashboard
- [[dashboard_DB_design]] — PostgreSQL schema, FastAPI endpoints, React frontend, SAML SSO
- [[test_plan]] — 172 tests across DB, API, SAML, security, frontend, E2E

## Related
- [[llm-vs-code-driven]] — the design principle both red-agent and soc-agent are built on
- [[SOC-agent-MOC]] — sister project; same model, same hardware, shared philosophy
- [[Gemma4_Deployment]] — Gemma4-26B-A4B running on GB10; powers both agents
- [[GB10-MOC]] — GB10 project that serves the model
