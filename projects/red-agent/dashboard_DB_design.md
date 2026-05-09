# BIS CTEM Dashboard — Design Document

> Part of [[red-agent-MOC]]. Test plan: [[test_plan]].

## Overview

Add a persistence and visibility layer on top of the existing headless `bis-red-agent` probing pipeline.
The probing logic stays unchanged — this project adds a database, a REST API, and a single-page dashboard.

---

## Goals

1. Store Nessus vulnerability scan results (high and critical only)
2. Store application probing results from `bis-red-agent`
3. Display findings in a single-page dashboard for SOC analysts

---

## Architecture

```
bis-red-agent (existing)          New components
─────────────────────────         ──────────────────────────────
cron_run_redteam.sh               PostgreSQL 16
  └── main.py                       └── schema (via Alembic)
        └── probe_http             FastAPI backend
        └── probe_ssh                └── SQLAlchemy (async)
        └── probe_rdp/vnc            └── asyncpg driver
        └── log_asset()  ──────────→  └── writes to DB
                                   React 18 + Ant Design 5 frontend
Nessus scanner (external)            └── react-grid-layout (widgets)
  └── import script ─────────────→  └── Axios (API calls)
```

---

## Database: PostgreSQL 16

### Schema

```sql
-- Subnets
subnets (id, cidr, netbox_owner, created_at)

-- Hosts
hosts (id, subnet_id, ip, hostname, last_seen)

-- Ports
ports (id, host_id, port, protocol, service, last_seen)

-- Nessus vulnerability findings (high + critical only)
nessus_vulns (
    id, port_id,
    plugin_id, cve, cvss, severity,
    name, synopsis, solution,
    scanned_at
)

-- bis-red-agent application probe results
probe_assets (
    id, port_id,
    application, version,
    has_auth, auth_type,
    confidence, evidence,
    verified_url, http_status,
    escalated,
    probed_at
)

-- SSH / RDP / VNC credential findings
remote_access_findings (
    id, port_id,
    protocol,           -- ssh / rdp / vnc
    password_auth,
    cracked_user, cracked_pass,
    escalation_note,
    probed_at
)

-- Escalations (HTTP probe LLM decisions)
escalations (
    id, port_id,
    source,             -- http_probe / ssh / rdp / vnc
    application,
    escalation_note,
    auth_status,
    target_url,
    asset_owner,
    alerted_at,
    resolved_at         -- null = open
)

-- Probe run history
probe_runs (
    id, subnet_id,
    started_at, finished_at,
    hosts_scanned, ports_found,
    escalations_raised
)
```

### Key design decisions
- `nessus_vulns` stores only CVSS >= 7.0 (high and critical)
- `probe_assets` replaces `assets.jsonl` — one row per probed port
- Same IP/port re-probed → UPDATE existing row, do not INSERT duplicate
- `escalations` tracks open/resolved state for SOC workflow
- All timestamps in UTC

---

## Authentication: SAML SSO

All dashboard access is protected by SAML 2.0 SSO. No local username/password.

### Flow
```
Browser → FastAPI /auth/login → Redirect to IdP (SAML Request)
IdP authenticates user → POST /auth/saml/callback (SAML Response)
FastAPI validates assertion → issues signed session cookie → redirect to dashboard
```

### Implementation
- **Library**: `python3-saml` (OneLogin) — battle-tested SAML 2.0 SP implementation
- **Session**: signed `httpOnly` cookie (JWT or server-side session in Redis)
- **SP metadata**: `GET /auth/saml/metadata` — auto-generated, register with IdP

### FastAPI auth endpoints
```
GET  /auth/login              # initiates SAML redirect to IdP
POST /auth/saml/callback      # receives SAML assertion from IdP
GET  /auth/logout             # SLO (single logout) to IdP
GET  /auth/saml/metadata      # SP metadata XML for IdP registration
```

### Config (environment variables)
```
SAML_IDP_METADATA_URL   # IdP metadata URL or file path
SAML_SP_ENTITY_ID       # this app's entity ID
SAML_SP_ACS_URL         # assertion consumer service URL
SAML_SP_SLS_URL         # single logout service URL
SAML_CERT_FILE          # SP signing certificate
SAML_KEY_FILE           # SP private key
```

### Authorization
- All `/api/*` endpoints require a valid session (return 401 if not authenticated)
- Session includes: `user_email`, `user_name`, `groups` (from SAML attributes)
- Read-only by default — no write endpoints exposed in v1

---

## Backend: FastAPI + SQLAlchemy (async) + asyncpg

### API endpoints

```
GET /api/stats                  # summary counts for top bar
GET /api/vulnerabilities        # Tab 1 — Nessus high/critical
GET /api/assets                 # Tab 2 — app inventory
GET /api/escalations            # Tab 3a — unauthenticated exposures
GET /api/remote-access          # Tab 3b — SSH/RDP/VNC findings
GET /api/interesting            # Tab 3c — LLM escalations
```

All endpoints support: `?subnet=`, `?severity=`, `?search=`, `?page=`, `?page_size=`
All endpoints require a valid SAML session cookie — return 401 if unauthenticated.

---

## Frontend: React 18 + Ant Design 5

### Widget-based architecture

Each panel is a self-contained widget with its own data query, layout, and config.
New widgets can be added by creating one React component + one FastAPI endpoint.

```
Dashboard
  └── WidgetGrid (react-grid-layout — drag, resize, persist layout)
        ├── SummaryStatsWidget       # top bar counts
        ├── VulnTableWidget          # Tab 1
        ├── AppInventoryWidget       # Tab 2
        ├── ExposedServicesWidget    # Tab 3a
        ├── CredentialFindingsWidget # Tab 3b
        └── EscalationsWidget        # Tab 3c
```

Widget interface:
```typescript
interface Widget {
  id: string
  title: string
  dataUrl: string       // FastAPI endpoint
  component: ReactNode  // visual component
  size: { w, h, x, y } // grid position
}
```

### Dashboard tabs

**Tab 1 — Vulnerabilities (Nessus)**
- Only high (CVSS 7.0–8.9) and critical (CVSS 9.0+)
- Columns: IP, port, CVSS, CVE, plugin name, owner, first seen
- Filters: severity, subnet, CVE

**Tab 2 — App Inventory (Probe)**
- All identified services regardless of auth status
- Columns: IP, port, application, version, auth type, last probed
- Side panel: breakdown by application type

**Tab 3 — App Security (Red Team)**
- 3a Unauthenticated Exposures: IP, port, application, exposure type
- 3b Credential Findings: IP, port, protocol, credentials found, finding type
- 3c Interesting Assets: IP, port, application, escalation note (LLM output)

### Correlated findings badge
When the same IP/port has both a critical Nessus vuln AND an unauthenticated
exposure, show a `CORRELATED` badge — these are the highest-priority findings.

---

## Integration with existing pipeline

Single change to `log_asset()` in `redteam/asset_db.py`:

```python
# Before: writes to assets.jsonl
# After:  writes to assets.jsonl AND PostgreSQL (backward compatible)
```

Escalations from `consolidate_and_alert()` write to `escalations` table.
SSH/RDP/VNC results from `alert_ssh()` / `alert_remote_access()` write to
`remote_access_findings` table.

---

## Test Plan

See `test_plan.md` for the full test plan including API, security, SAML, and integration tests.

---

## Build order

1. PostgreSQL schema + Alembic migrations
2. SAML SSO integration + session management
3. Update `log_asset()` and alert functions to write to DB
4. FastAPI read-only API endpoints (all protected by SAML session)
5. React dashboard — summary stats + Tab 1 (Vulnerabilities)
6. Tab 2 (App Inventory) + application breakdown panel
7. Tab 3 (App Security) — all three sub-sections
8. Widget grid (drag/resize/persist)
9. Correlated findings badge
10. Nessus import script
