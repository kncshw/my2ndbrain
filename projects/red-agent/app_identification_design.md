# Application Identification Design

> Implements the "deterministic first, LLM last" principle from [[agent-design-comparison]]. Part of [[red-agent-MOC]].

## Problem

Too many probe results show `application: unknown` or incorrect names because
the LLM was asked to identify apps from thin HTTP responses — 404 pages, empty
bodies, generic redirects. LLM is good at reasoning; it is bad at pattern
extraction from sparse evidence.

## Principle

Use deterministic extraction first. LLM only for what it is actually good at:
interpreting ambiguous auth states and deciding escalation priority.

```
Deterministic (fast, always accurate when signal exists)
  → SSL cert       — who issued it, what CN says
  → HTTP headers   — Server:, X-Powered-By:, location redirects
  → Page title     — <title> tag is almost always accurate
  → HTTP body      — specific string patterns (product names, version strings)

LLM (slow, token cost, used only when deterministic gives no answer OR for judgment)
  → Auth status    — is content actually accessible without login?
  → Escalation     — should this be alerted given everything we know?
```

---

## Identification Pipeline

### Step 1 — SSL Certificate (highest confidence)

Extract from `openssl x509 -noout -subject -issuer`:

| Field | What to extract | Example |
|---|---|---|
| `CN=` in Subject | Product name or domain | `*.fortimailcloud.com` → FortiMail Cloud |
| `OU=` in Subject | Product line | `OU=Fortiauthenticator` → FortiAuthenticator |
| `OU=` in Issuer | Issuing product | `OU=Certificate Authority, CN=FG6H0FTB...` → FortiGate-issued |
| `O=` in Subject | Vendor | `O=Fortinet` → Fortinet product (generic) |

**Rules:**
- If CN contains a recognisable domain or product name → use it directly as app name, `confidence=high`
- If OU contains a product name → use it directly, `confidence=high`
- If cert is from a public CA (DigiCert, Let's Encrypt, GlobalSign) → CN is a domain name, use domain as app name hint
- If cert is self-signed with Fortinet OU → exact product name, `confidence=high`
- No keyword mapping table — extract the raw value and use it

**Output:** `(app_name, evidence, confidence)` or `None` if cert has no useful identity signal

---

### Step 2 — HTTP Headers (high confidence for known products)

Extract from response headers:

| Header | Signal |
|---|---|
| `Server: FortiGate` | FortiGate |
| `Server: nginx` | NGINX |
| `Server: Apache` | Apache |
| `X-Powered-By: Express` | Node.js/Express |
| `X-Powered-By: PHP/8.x` | PHP app |
| `Location: /remote/login` | FortiGate SSL-VPN |
| `Location: /login/?next=/` | Django app |
| `X-Frame-Options: SAMEORIGIN` + `Vary: Accept-Language,Cookie` | Django middleware fingerprint |
| `Set-Cookie: APSCOOKIE` | FortiGate |
| `Set-Cookie: ccsrftoken` | FortiGate/FortiManager |

**Rules:**
- `Server:` header is authoritative when present
- Redirect destination is a strong fingerprint (FortiGate always redirects to `/remote/login`)
- Cookie names are product-specific and reliable

**Output:** `(app_name, evidence, confidence)` or `None`

---

### Step 3 — Page Title (medium-high confidence)

Extract `<title>` tag from HTML body.

| Title | App |
|---|---|
| `FortiGate` | FortiGate |
| `FortiManager` | FortiManager |
| `SSL VPN` | FortiGate SSL-VPN |
| `FortiAnalyzer` | FortiAnalyzer |
| `Grafana` | Grafana |
| `Prometheus` | Prometheus |
| `Kibana` | Kibana |
| `Log In - ...` | Generic login page (use domain/cert for product name) |

**Rules:**
- Title match is high confidence for known products
- Generic titles (`Log In`, `Welcome`, `Home`) are low confidence — move to Step 4

---

### Step 4 — HTTP Body Patterns (medium confidence)

Look for specific strings in the HTML body:

| Pattern | App |
|---|---|
| `FortiGate` in body text | FortiGate |
| `fgt_lang` JS variable | FortiGate |
| `var fmgAddr` | FortiManager |
| `/site_media/` CSS paths | FortiNAC or FortiAuthenticator (Django) |
| `Grafana` in body | Grafana |
| `data-reactroot` | React app (look at title for product) |
| `__NUXT__` | Nuxt.js app |
| `ng-version` | Angular app |

---

### Step 5 — LLM (auth status + escalation only)

By this point the app name is known from Steps 1-4. LLM receives:

```
Application: FortiAuthenticator (identified from SSL cert OU=Fortiauthenticator)
HTTP status: 302 → /login/?next=/
Headers: [trimmed]
Page content: [trimmed]

Question 1: Is content accessible without authentication? (has_auth, auth_type)
Question 2: Should this be escalated given the app type and auth state?
```

LLM is **not** asked to identify the application. It only judges:
- Whether the auth gate is real or bypassable
- Whether the finding warrants an alert

---

## Decision Tree

```
SSL cert available?
├── YES → extract CN/OU → app_name known, confidence=high
│         → go to Step 5 (LLM for auth only)
└── NO  → check HTTP headers
          ├── Server:/Cookie/Location match → app_name known, confidence=high
          │   → go to Step 5
          └── no header match → check page title
                ├── known title → app_name known, confidence=medium
                │   → go to Step 5
                └── generic title → check body patterns
                      ├── pattern match → app_name known, confidence=medium
                      │   → go to Step 5
                      └── no match → LLM identifies app + auth + escalation
                                     (full LLM, current behaviour, confidence=low)
```

---

## What "unknown" Should Mean After This Change

`unknown` should only appear when:
1. No SSL cert (plain HTTP, no TLS)
2. No identifying headers
3. Generic or empty page title
4. No known body patterns
5. LLM also cannot identify from content

In practice this should cover < 5% of probed hosts in a Fortinet environment.

---

## Implementation Order

1. Rewrite `_parse_cert_identity` — drop keyword map, extract raw CN/OU/O directly
2. Add `_parse_header_identity(headers)` — check Server:, Location:, Set-Cookie:
3. Add `_parse_title_identity(html)` — extract and match `<title>`
4. Add `_parse_body_identity(html)` — check known body string patterns
5. Update `probe_http` — run Steps 1-4 before LLM; if app identified, pass to LLM with
   app name pre-filled and ask only for auth status
6. Update `_identify` prompt — make app name optional input, focus on auth when provided
