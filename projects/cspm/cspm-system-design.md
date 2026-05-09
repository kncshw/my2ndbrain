# CSPM System Design

> Entry point: [[cspm-MOC]]. Execution reference: [[cspm-execution]]. Workflows: [[cspm-workflows]].

BIS-CSPM (Cloud Security Posture Management) is a vulnerability management platform that orchestrates Nessus scans across public IP subnets, processes findings through a Kafka streaming pipeline, creates FortiSOAR tickets, and distributes reports.

---

## Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│  DISCOVERY                                                        │
│  NetBox → scan_discovery → Scan Management API → Nessus subnets  │
└───────────────────────────────┬──────────────────────────────────┘
                                │  daily scans complete
          ┌─────────────────────┼─────────────────────┐
          │                     │                     │
┌─────────▼──────────┐ ┌────────▼───────────┐ ┌──────▼──────────┐
│ LEGACY EMAIL PATH  │ │ KAFKA INGEST PATH  │ │ OPEN PORT PATH  │
│ (run-daily-report) │ │ (run-daily-scan-   │ │ (run-open-port- │
│                    │ │  ingest)           │ │  check)         │
│ Email → parse CSV  │ │ Nessus → filter    │ │ Nessus plugins  │
│ → filter → tickets │ │ → produce Kafka    │ │ → produce Kafka │
│ → email report     │ │   events           │ │   events        │
└────────────────────┘ └────────┬───────────┘ └──────┬──────────┘
                                │                    │
                    ┌───────────▼────────────────────▼──┐
                    │  KAFKA TOPICS                      │
                    │  subnet-A-B-C-0_24  (per /24)      │
                    │  scanner-analytics  (aggregated)   │
                    └───────────┬────────────────────────┘
                                │
          ┌─────────────────────┼────────────────────────┐
          │                     │                        │
┌─────────▼──────────┐ ┌────────▼───────────┐ ┌─────────▼──────────┐
│ VULN CONSUMER      │ │ BRUTEFORCE TICKETS │ │ REPORT DATA PREP   │
│ (run-daily-scan-   │ │ (run-bruteforce-   │ │ (weekly)           │
│  consume)          │ │  ticket)           │ │                    │
│ → FSR tickets      │ │ → FSR tickets      │ │ → 6 CSV files      │
│ → email report     │ └────────────────────┘ │ → analytics report │
└────────────────────┘                         └────────────────────┘
```

---

## Integrations

| System | Purpose | Auth |
|---|---|---|
| **Nessus** | Daily subnet vulnerability scans | Username/password |
| **Kafka** | Event streaming between producer/consumer workflows | SASL/PLAIN |
| **FortiSOAR** | Vulnerability + open port ticket creation | HMAC SHA256 (public/private key) |
| **NetBox** | IP ownership lookup, /24 subnet enumeration | API token |
| **Redis** | Cache IP→description (7d TTL), scan IDs (24h TTL) | Host/port |
| **IPAM (phpIPAM)** | Legacy subnet owner lookup | Username/password |
| **SMTP/IMAP** | Send reports, receive Nessus email attachments | Username/password |
| **Scan Management API** | Register new subnets for scanning | Endpoint only |

---

## Data Flow: Kafka Message Schema

```json
{
  "metadata": {
    "eventType": "vulnerability.detected | openport.detected | bruteforce-vulnerable",
    "source": "scanner-nessus-aws",
    "timestamp": "2026-05-09T10:30:00Z",
    "schemaVersion": "1.0",
    "messageId": "<uuid>"
  },
  "payload": {
    "ip": "<target-ip>",
    "ports": [443, 22],
    "assetGroup": "<asset-group>",
    "tenant": "<tenant-name>",
    "cVSS": 7.5,
    "cVENames": ["CVE-2021-12345"],
    "severity": "High | Critical",
    "vulnerabilitySubject": "Plugin name",
    "solution": "Remediation steps",
    "synopsis": "Summary"
  }
}
```

**Topic naming:** `subnet-A-B-C-0_24` (derived from first 3 octets of IP). Same IP always routes to same partition via IP-as-key.

---

## Subnet Category Mapping

Subnet descriptions from NetBox are mapped to scan categories:

| Keyword in description | Category | Scanned? |
|---|---|---|
| `<category-a-keyword>` | CAT-A | Yes |
| `<category-b-keyword>` | CAT-B | Yes |
| `<category-c-keyword>` | CAT-C | Yes |
| `<category-d-keyword>` | CAT-D | Yes |
| `<category-e-keyword>` | CAT-E | Yes |
| `<category-f-keyword>` | CAT-F | Yes |
| `<demo-keyword>` | DEMO | No |
| `<exempt-keyword>` | EXEMPT | No |
| _(no match)_ | UNKNOWN | No |

---

## Vulnerability Filtering

Filter list at `config/filter_list.csv` — format: `[Plugin ID, Host, Port]`.

A vulnerability matching all three fields is excluded from tickets and reports. This is the primary mechanism for suppressing known false positives or accepted risks. Filter list is never written by the agent — human edits only.

---

## FortiSOAR Ticket Lookup

After creating a ticket, the system queries FSR with exponential backoff:
- Retries: up to 12 times
- Backoff: 2s → 4s → 8s → ... → 60s cap
- Total wait: ~2 minutes
- Lookup key: `External_{ip}`

---

## Caching

| Cache | Key | TTL | Purpose |
|---|---|---|---|
| Redis | IP address | 7 days | NetBox IP→description, avoids repeated API calls |
| Redis | `complete_daily_scans_id` | 24 hours | Nessus completed scan IDs |
| In-memory | Subnet CIDR | Process lifetime | Subnet descriptions within a single run |

---

## Project Layout

```
bis-cspm/
├── BISpubIP_manager/
│   ├── cli.py                  ← entry point, 12 commands
│   ├── config.py               ← frozen dataclasses from env vars
│   ├── core/
│   │   └── scan_manager.py     ← scan orchestration
│   ├── workflows/              ← one file per CLI command
│   │   ├── daily_scan_report.py
│   │   ├── scan_discovery.py
│   │   ├── vulnerability_ingestor.py
│   │   ├── vulnerability_consumer.py
│   │   ├── daily_brute_force_ticket.py
│   │   ├── open_port_check.py
│   │   ├── health_check.py
│   │   ├── prepare_report_data_from_kafka.py
│   │   └── scanner_statistics_ingestor.py
│   ├── integrations/           ← external system clients
│   │   ├── fortisoar.py        ← HMAC auth, ticket creation
│   │   ├── kafka_producer.py   ← SASL/PLAIN, retry logic
│   │   ├── kafka_consumer.py   ← time-windowed, regex topics
│   │   ├── netbox.py           ← IP lookup, Redis-backed cache
│   │   ├── ipam.py             ← legacy phpIPAM
│   │   └── redis_cache.py
│   ├── data/
│   │   ├── subnet_processor.py ← description → category mapping
│   │   ├── data_merger.py      ← merge multiple CSVs
│   │   └── vuln_filtering.py   ← filter list lookup (O(1))
│   ├── reporting/
│   │   ├── summary_email.py    ← HTML email + Excel attachment
│   │   ├── vuln_ticket.py      ← FSR ticket creation from CSV or Kafka
│   │   ├── vuln_analytic_report.py
│   │   └── scan_statistics.py
│   └── scanners/
│       ├── nessus/             ← Nessus API client + Redis caching
│       └── nmap/               ← nmap scanner (secondary)
├── cron_run_*.sh               ← one script per scheduled job
├── Dockerfile
└── requirements.txt
```
