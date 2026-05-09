# CSPM Execution Reference

> Part of [[cspm-MOC]]. See [[cspm-workflows]] for what each command does.

---

## Production Environment

- **Host:** `<mgmt-server>` (runs as user `bis`)
- **Code path:** `/home/bis/bis-cspm`
- **Venv:** `/home/bis/bis-cspm/venv/bin/python`
- **Logs:** `/var/log/bis-cspm/cron_runner.log`
- **Docker image:** `bis-cspm:latest`

---

## Setup

### Build Docker image

```bash
cd /home/bis/bis-cspm
docker build -t bis-cspm .
```

### Or use venv directly

```bash
cd /home/bis/bis-cspm
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Running Commands

### Via Docker (production)

```bash
# Run any command — replace <command> with one of the CLI commands below
docker run --network host --rm \
  -v /var/log/bis-cspm/docker/:/var/log/bis-cspm/ \
  bis-cspm <command> >> /var/log/bis-cspm/cron_runner.log 2>&1
```

### Via venv (dev/debug)

```bash
cd /home/bis/bis-cspm
source venv/bin/activate
python -m BISpubIP_manager.cli <command>
```

### Via cron scripts

```bash
./cron_run_daily_report.sh >> /var/log/bis-cspm/cron_runner.log 2>&1
./cron_run_daily_kafka_message.sh >> /var/log/bis-cspm/cron_runner.log 2>&1
./cron_run_scan_discovery.sh >> /var/log/bis-cspm/cron_runner.log 2>&1
./cron_run_health_check.sh >> /var/log/bis-cspm/cron_runner.log 2>&1
```

---

## CLI Commands

```bash
python -m BISpubIP_manager.cli run-daily-report          # parse emails → tickets → report
python -m BISpubIP_manager.cli run-health-check          # check Nessus scan status
python -m BISpubIP_manager.cli run-open-port-check       # detect exposed services → Kafka
python -m BISpubIP_manager.cli run-scan-discovery        # find new subnets → add to scan system
python -m BISpubIP_manager.cli run-daily-scan-ingest     # Nessus vulns → Kafka
python -m BISpubIP_manager.cli run-daily-scan-consume    # Kafka → FSR tickets + email
python -m BISpubIP_manager.cli run-bruteforce-ticket     # Kafka brute force events → FSR tickets
python -m BISpubIP_manager.cli run-scanner-statistics-ingest  # stats → Kafka analytics
python -m BISpubIP_manager.cli run-weekly-report         # all Kafka → CSVs → analytics report
```

---

## Daily Cron Schedule

| Time | Script | Command(s) |
|---|---|---|
| Morning (after emails arrive) | `cron_run_daily_report.sh` | `run-daily-report` |
| After Nessus scans complete | `cron_run_daily_kafka_message.sh` | `run-open-port-check` → `run-daily-scan-ingest` |
| Daily | `cron_run_health_check.sh` | `run-health-check` |
| Daily | `cron_run_daily_bruteforce_ticket.sh` | `run-bruteforce-ticket` |
| Weekly (Monday) | `cron_run_scan_discovery.sh` | `run-scan-discovery` |

---

## Testing

```bash
cd /home/bis/bis-cspm
./venv/bin/python3 -m pytest
```

---

## Environment Variables (`.env`)

```bash
# --- FortiSOAR ---
FSR_API_URL="https://<fsr-host>/api"
FSR_API_PUBLIC_KEY="<path-or-key>"
FSR_API_PRIVATE_KEY="<path-or-key>"
FSR_ROOT_URL="https://<fsr-host>"

# --- Email (IMAP + SMTP) ---
EMAIL_IMAP_SERVER="<imap-server-ip>"
EMAIL_USERNAME="<username>"
EMAIL_PASSWORD="<password>"
EMAIL_RECIPIENTS="<recipient1@domain.com>,<recipient2@domain.com>"

# --- Fortinet IPAM (legacy) ---
IPAM_API_URL="https://<ipam-host>"
IPAM_USERNAME="<username>"
IPAM_PASSWORD="<password>"
IPAM_APP_ID="devops"

# --- NetBox ---
NETBOX_API_URL="https://<netbox-host>"
NETBOX_API_TOKEN="<token>"

# --- Database (if used) ---
DB_HOST="localhost"
DB_PORT="3306"
DB_USERNAME="<user>"
DB_PASSWORD="<password>"
DB_NAME="<dbname>"

# --- Nessus ---
NESSUS_URL="https://<nessus-host>"
NESSUS_USERNAME="<username>"
NESSUS_PASSWORD="<password>"

# --- Kafka ---
KAFKA_HOST="<broker-host>"
KAFKA_PORT="9092"
KAFKA_USERNAME="<username>"
KAFKA_PASSWORD="<password>"

# --- Scan Management ---
SCAN_MGMT_API_ENDPOINT="<endpoint-url>"

# --- Report paths ---
REPORT_BASE_DIR="artifacts"
REPORT_FILTER_LIST_FILE="BISpubIP_manager/data/filter_list.csv"
```

---

## Artifact Directory Structure

```
artifacts/
└── YYYY-MM-DD/
    ├── parsed_emails/          ← raw CSVs from Nessus email attachments
    ├── merged_vulnerabilities.csv
    ├── filtered_vulnerabilities.csv
    └── <previous-day-backup>/
```

---

## Error Handling

All cron scripts check exit codes. On failure:
- Last 30 lines of `cron_runner.log` are captured
- `error_notification.py` sends an alert email with script name + log tail
- Script exits with code 1

To debug a failed run manually:
```bash
tail -100 /var/log/bis-cspm/cron_runner.log
```
