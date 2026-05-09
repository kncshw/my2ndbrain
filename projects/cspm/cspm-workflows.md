# CSPM Workflows

> Part of [[cspm-MOC]]. See [[cspm-system-design]] for architecture and [[cspm-execution]] for run commands.

---

## Workflow Map

| CLI Command | Cron Script | Trigger | Purpose |
|---|---|---|---|
| `run-daily-report` | `cron_run_daily_report.sh` | Daily morning | Parse Nessus email reports → tickets + email |
| `run-scan-discovery` | `cron_run_scan_discovery.sh` | Weekly | Find new NetBox subnets → add to scan system |
| `run-daily-scan-ingest` | `cron_run_daily_kafka_message.sh` (2nd) | Daily post-scan | Nessus results → Kafka events |
| `run-open-port-check` | `cron_run_daily_kafka_message.sh` (1st) | Daily post-scan | Exposed ports → Kafka events + Telnet tickets |
| `run-daily-scan-consume` | manual / Airflow | After ingest | Kafka events → FSR tickets + email report |
| `run-bruteforce-ticket` | `cron_run_daily_bruteforce_ticket.sh` | Daily | Brute force events → FSR tickets |
| `run-health-check` | `cron_run_health_check.sh` | Daily | Nessus scan completion check → alert email |
| `run-scanner-statistics-ingest` | manual / weekly | Weekly | Aggregate stats → Kafka analytics topic |
| `run-weekly-report` | manual / weekly | Weekly | Consume all Kafka data → CSV files → analytics report |

---

## Daily Scan Report (Legacy Email Path)

**Trigger:** `cron_run_daily_report.sh` — daily morning after Nessus emails arrive

**Steps:**
1. Connect to IMAP, fetch Nessus report emails from previous day
2. Extract and parse CSV attachments → `artifacts/YYYY-MM-DD/parsed_emails/`
3. Merge all CSVs → `merged_vulnerabilities.csv`
4. Apply filter list → `filtered_vulnerabilities.csv`
5. Create FortiSOAR tickets for each remaining vulnerability
6. Query NetBox for IP owner info
7. Generate HTML + Excel report
8. Send email to `EMAIL_RECIPIENTS`

**Output:** FSR tickets + email with vulnerability summary and owner info

---

## Scan Discovery

**Trigger:** `cron_run_scan_discovery.sh` — weekly (Monday recommended)

**Steps:**
1. Fetch all /24 public subnets from NetBox
2. Query Scan Management API for already-registered subnets
3. Diff → find subnets in NetBox but not in scan system
4. Map subnet description → category (see `subnet_processor.py` for mapping)
5. POST new subnets to Scan Management API
6. Print summary: added / failed / unknown category

**Output:** New subnets registered for Nessus scanning

---

## Vulnerability Ingestor (Kafka Producer)

**Trigger:** `cron_run_daily_kafka_message.sh` — daily after Nessus scans complete (runs after `run-open-port-check`)

**Steps:**
1. Fetch completed daily scan IDs from Nessus (cached in Redis 24h)
2. For each scan, get vulnerabilities with severity ≥ 3 (High/Critical)
3. Apply filter list
4. For each vulnerability, build Kafka message (`eventType=vulnerability.detected`)
5. Produce to topic `subnet-A-B-C-0_24` with IP as message key

**Output:** Kafka messages per /24 subnet topic, one message per vulnerability/IP combination

---

## Open Port Check

**Trigger:** `cron_run_daily_kafka_message.sh` — runs first, before vulnerability ingest

**Steps:**
1. Fetch Nessus results for specific service plugin IDs:
   - 10092 (FTP), 22964 (HTTP/HTTPS), 10280/10281 (Telnet), 10342 (VNC), 10267 (SSH), 10940 (RDP)
2. Apply filter list
3. Produce `openport.detected` Kafka events per subnet topic
4. For Telnet specifically: also create FortiSOAR tickets immediately
5. Query NetBox for owner info, print port summary report

**Output:** Kafka `openport.detected` events + FSR tickets for Telnet findings

---

## Vulnerability Consumer (Kafka Consumer)

**Trigger:** Manual or Airflow — run after ingest completes

**Steps:**
1. Subscribe to all `subnet-*` topics (regex pattern)
2. Consume messages from last 2 hours with `eventType=vulnerability.detected` and `source=scanner-nessus-aws`
3. Group messages by IP
4. Create FortiSOAR ticket per IP with all vulnerability details
5. Generate HTML email summary with ticket links + owner info
6. Send to `EMAIL_RECIPIENTS`

**Output:** FSR tickets + email report

---

## Brute Force Ticket Creator

**Trigger:** `cron_run_daily_bruteforce_ticket.sh` — daily

**Steps:**
1. Subscribe to all `subnet-*` topics
2. Consume messages from last 2 hours with `eventType=bruteforce-vulnerable`
3. Create FortiSOAR ticket per finding
4. Log ticket links

**Output:** FSR brute force vulnerability tickets

---

## Health Check

**Trigger:** `cron_run_health_check.sh` — daily

**Steps:**
1. Query Nessus for all public subnet scans
2. Flag any scan NOT in `completed` or `empty` status
3. If failures found → send alert email

**Output:** Email alert if any scans failed or stuck

---

## Scanner Statistics Ingestor

**Trigger:** Weekly or manual

**Steps:**
1. Aggregate vulnerability counts by severity from Nessus
2. Calculate scan completion rates and coverage metrics
3. Produce to `scanner-analytics` Kafka topic:
   - `eventType=scanner-statistics` — scan health data
   - `eventType=filter-statistics` — filtered vulnerability counts

**Output:** Kafka analytics messages for weekly report

---

## Weekly Report (Report Data Preparation)

**Trigger:** Manual / weekly cron

**Steps:**
1. Subscribe to all `subnet-*` and `scanner-analytics` topics
2. Consume all messages from past 24 hours
3. Classify by `eventType`:
   - `service.exposed` → `services.csv`
   - `application.detected` → `applications.csv`
   - `openport.detected` + `bruteforce-vulnerable` → correlate exploitability
   - `scanner-statistics` → summary stats
   - `ticket-statistics` → vulnerabilities with ticket links
4. Write 6 CSV output files
5. Generate analytics HTML report

**Output:**
- `services.csv` — open ports with exploitability flag
- `applications.csv` — detected apps
- `vulnerabilities.csv` — ticketed findings with FSR links
- `filtered_reasons.csv` — suppression counts
- `summary_stats.csv` — aggregate scan metrics
- HTML analytics report emailed to recipients
