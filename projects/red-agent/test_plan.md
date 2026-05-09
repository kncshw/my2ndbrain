# BIS CTEM Dashboard — Test Plan

> Validates everything specified in [[dashboard_DB_design]]. Part of [[red-agent-MOC]].

---

## 1. Database Layer

| # | Test | Expected |
|---|------|----------|
| DB-01 | Run Alembic migrations on fresh PostgreSQL instance | All tables created, no errors |
| DB-02 | Run migrations twice (idempotency) | No error, no duplicate tables |
| DB-03 | `log_asset()` writes correct record to `probe_assets` | Row exists with correct IP, port, application, has_auth |
| DB-04 | Re-probe same IP/port | Existing row updated, no duplicate inserted |
| DB-05 | Nessus import with CVSS 9.8 finding | Row appears in `nessus_vulns` |
| DB-06 | Nessus import with CVSS 5.0 finding (medium) | Row NOT inserted — filtered out |
| DB-07 | Escalation from `consolidate_and_alert()` | Row appears in `escalations` with correct fields |
| DB-08 | SSH cracked credential | Row appears in `remote_access_findings` |
| DB-09 | Query `probe_assets` with 10,000 rows | Response < 200ms |
| DB-10 | Query `nessus_vulns` joined with `hosts` on 10,000 rows | Response < 500ms |

---

## 2. API Endpoints

### Authentication
| # | Test | Expected |
|---|------|----------|
| AUTH-01 | `GET /api/stats` without session cookie | `401 Unauthorized` |
| AUTH-02 | `GET /api/vulnerabilities` without session cookie | `401 Unauthorized` |
| AUTH-03 | `GET /api/assets` without session cookie | `401 Unauthorized` |
| AUTH-04 | `GET /api/escalations` without session cookie | `401 Unauthorized` |
| AUTH-05 | `GET /api/remote-access` without session cookie | `401 Unauthorized` |
| AUTH-06 | `GET /api/interesting` without session cookie | `401 Unauthorized` |
| AUTH-07 | Request with expired session cookie | `401 Unauthorized` |
| AUTH-08 | Request with tampered session cookie | `401 Unauthorized` |

### GET /api/stats
| # | Test | Expected |
|---|------|----------|
| API-01 | Authenticated request | Returns `critical_count`, `high_count`, `asset_count`, `escalation_count`, `subnet_count` |
| API-02 | DB is empty | Returns all counts as 0, no crash |

### GET /api/vulnerabilities
| # | Test | Expected |
|---|------|----------|
| API-03 | Authenticated request | Returns only CVSS >= 7.0 findings |
| API-04 | `?severity=critical` | Returns only CVSS >= 9.0 |
| API-05 | `?severity=high` | Returns only CVSS 7.0–8.9 |
| API-06 | `?subnet=154.52.1.0/24` | Returns only findings for that subnet |
| API-07 | `?search=CVE-2024-21762` | Returns matching CVE rows only |
| API-08 | `?page=1&page_size=10` | Returns 10 rows, includes `total` count |
| API-09 | Empty results | Returns `{"data": [], "total": 0}` |

### GET /api/assets
| # | Test | Expected |
|---|------|----------|
| API-10 | Authenticated request | Returns all `probe_assets` rows |
| API-11 | `?subnet=69.167.115.0/24` | Filtered to subnet |
| API-12 | `?search=Prometheus` | Returns only Prometheus assets |
| API-13 | `?page=2&page_size=20` | Correct pagination |
| API-14 | Empty results | Returns `{"data": [], "total": 0}` |

### GET /api/escalations
| # | Test | Expected |
|---|------|----------|
| API-15 | Authenticated request | Returns all open escalations |
| API-16 | `?subnet=` filter | Filters by subnet |
| API-17 | Resolved escalation (`resolved_at` not null) | Not returned by default |
| API-18 | `?include_resolved=true` | Resolved escalations included |

### GET /api/remote-access
| # | Test | Expected |
|---|------|----------|
| API-19 | Authenticated request | Returns SSH/RDP/VNC findings |
| API-20 | `?protocol=ssh` | Returns only SSH findings |
| API-21 | `?protocol=rdp` | Returns only RDP findings |
| API-22 | `?protocol=vnc` | Returns only VNC findings |

### GET /api/interesting
| # | Test | Expected |
|---|------|----------|
| API-23 | Authenticated request | Returns LLM-escalated HTTP probe findings |
| API-24 | `?subnet=` filter | Filtered correctly |

---

## 3. SAML SSO

| # | Test | Expected |
|---|------|----------|
| SAML-01 | `GET /auth/login` | Redirects to IdP with valid SAML AuthnRequest |
| SAML-02 | Valid SAML Response posted to `/auth/saml/callback` | Session cookie issued, redirect to dashboard |
| SAML-03 | Invalid SAML Response (bad signature) | `403 Forbidden`, no session issued |
| SAML-04 | Expired SAML assertion | `403 Forbidden` |
| SAML-05 | Replayed SAML assertion (same ID used twice) | `403 Forbidden` — replay attack blocked |
| SAML-06 | `GET /auth/logout` with valid session | Session destroyed, redirect to IdP SLO |
| SAML-07 | `GET /auth/saml/metadata` | Returns valid SP metadata XML |
| SAML-08 | Session persists across browser tabs | Same session cookie works on all tabs |
| SAML-09 | Session cookie is `httpOnly` | Cannot be read by JavaScript (`document.cookie`) |
| SAML-10 | Session cookie is `Secure` | Only sent over HTTPS |
| SAML-11 | Session cookie has `SameSite=Strict` | Not sent on cross-site requests |

---

## 4. Security Tests

### SQL Injection
| # | Test | Expected |
|---|------|----------|
| SEC-01 | `GET /api/assets?search=' OR '1'='1` | Returns normal filtered results, no data leak |
| SEC-02 | `GET /api/vulnerabilities?subnet='; DROP TABLE nessus_vulns;--` | `400 Bad Request` or empty results, table intact |
| SEC-03 | `GET /api/assets?page=1; SELECT * FROM escalations` | `400 Bad Request` |
| SEC-04 | All filter params use parameterized queries | Verified by code review — no string concatenation into SQL |

### Cross-Site Scripting (XSS)
| # | Test | Expected |
|---|------|----------|
| SEC-05 | Asset with `application = "<script>alert(1)</script>"` in DB | Dashboard renders escaped text, no script execution |
| SEC-06 | Escalation note with `<img src=x onerror=alert(1)>` | Rendered as escaped text |
| SEC-07 | All API responses have `Content-Type: application/json` | Browser treats as data, not HTML |
| SEC-08 | Frontend uses Ant Design Table (React) | React escapes all rendered values by default |
| SEC-09 | No use of `dangerouslySetInnerHTML` in React components | Verified by code review |

### Open Redirect
| # | Test | Expected |
|---|------|----------|
| SEC-10 | `GET /auth/login?next=https://evil.com` | Redirect only to whitelisted internal URLs |
| SEC-11 | `GET /auth/saml/callback` with crafted `RelayState=https://evil.com` | RelayState validated against whitelist |
| SEC-12 | Post-logout redirect to external URL | Blocked — only redirect to `/` or configured SP URL |

### General Security Headers
| # | Test | Expected |
|---|------|----------|
| SEC-13 | All responses include `X-Content-Type-Options: nosniff` | Present |
| SEC-14 | All responses include `X-Frame-Options: DENY` | Present — prevents clickjacking |
| SEC-15 | All responses include `Content-Security-Policy` | Present — restricts script sources |
| SEC-16 | HTTPS enforced — HTTP redirects to HTTPS | `301` redirect on port 80 |
| SEC-17 | API does not expose stack traces in error responses | Error returns generic message, no traceback |
| SEC-18 | Database credentials not exposed in any API response | Verified by code review |

---

## 5. Frontend Layer

| # | Test | Expected |
|---|------|----------|
| FE-01 | Dashboard loads with real data | All 3 tabs render, no console errors |
| FE-02 | Empty database | All tabs show empty state message, no crash |
| FE-03 | Tab 1 severity filter | Only selected severity shown |
| FE-04 | Tab 2 search filter | Table narrows to matching rows |
| FE-05 | Tab 3 sub-section toggle | Correct sub-section displayed |
| FE-06 | `CORRELATED` badge | Appears only when same IP has Nessus critical + no-auth exposure |
| FE-07 | Widget drag and resize | Layout updates correctly |
| FE-08 | Widget layout persists after page refresh | Saved layout restored |
| FE-09 | Renders at 1920×1080 | No overflow, no broken layout |
| FE-10 | Renders at 2560×1440 | No overflow, no broken layout |
| FE-11 | Unauthenticated user visits dashboard URL | Redirected to `/auth/login` |

---

## 6. Integration (End-to-End)

| # | Test | Expected |
|---|------|----------|
| E2E-01 | `./cron_run_redteam.sh --ip <known-ip>` completes | Asset row appears in `probe_assets` and Tab 2 within 60s |
| E2E-02 | Known escalation IP probed | Row in `escalations`, appears in Tab 3 |
| E2E-03 | Nessus import run with known critical finding | Appears in Tab 1 with correct CVSS |
| E2E-04 | Same IP re-probed after application change | Tab 2 shows updated application name, not duplicate |
| E2E-05 | IP with both Nessus critical + no-auth probe | `CORRELATED` badge visible in both Tab 1 and Tab 3 |
| E2E-06 | SSH cracked credential | Appears in Tab 3b Credential Findings |
| E2E-07 | Full batch run `--file docs/batches/all-subnets.txt` | All results in DB, no probe data lost |
| E2E-08 | Probe run with 0 zombie processes after completion | Kali sandbox clean after `cron_run_redteam.sh` finishes |

---

## Pass Criteria

All tests must pass before dashboard is considered production-ready:
- Zero security test failures (SEC-01 through SEC-18) — **hard requirement**
- Zero SAML test failures (SAML-01 through SAML-11) — **hard requirement**
- All API endpoint tests pass
- All E2E tests pass on staging environment with real Nessus + probe data
