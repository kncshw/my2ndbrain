# SOC Agent — Execution Reference

> Runbook for deploying and running the SOC agent on `bis-ptmgmt`.
> Model: `google/gemma-4-26B-A4B-it` → [[Gemma4_Deployment]]
> System prompt: [[soc-analyst-prompt-min]]

---

## Setup (fresh venv)

Run this when the venv is broken or missing:

```bash
cd ~/bis-soc-agent
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

**What `pip install` installs:** openharness-ai + anthropic, openai, pydantic, vLLM client stack, textual TUI, playwright, pytest/mypy/ruff dev tools.

---

## Running the agent

```bash
cd ~/bis-soc-agent
set -a && source .env && set +a
./bin/bis-soc <alert_id>
```

---

## Example: Alert-114680 — Escalated (C2 activity)

**Alert:** Compromised host `146.70.173.178` detected

```
==== Processing 114680 ====
  > fortisoar_get_alert(alert_id=114680)
  ✓ FortiSOAR Alert-114680: Compromised host 146.70.173.178 detected

  > faz_query_security_events(adom=FortiCloud_Server device=CA_VAN3-B-C007-RH-GW-FGT_TMP end_time=2026-05-07 19:49:05 time_range=10m)
  ✓ FortiAnalyzer security events returned

  > faz_query_logs(adom=FortiCloud_Server device=CA_VAN3-B-C007-RH-GW-FGT_TMP end_time=2026-05-07 19:49:05 ip=146.70.173.178 time_range=10m)
  ✓ Traffic logs returned (after event window)

  > faz_query_logs(adom=FortiCloud_Server device=CA_VAN3-B-C007-RH-GW-FGT_TMP end_time=2026-05-07 19:39:05 ip=146.70.173.178 time_range=10m)
  ✓ Traffic logs returned (before event window)

  > faz_query_logs(adom=FortiCloud_Server ip=10.125.246.38 time_range=10m)
  ✓ Lateral movement check on internal IP

  > fortisoar_escalate_alert(alert_id=114680 findings=...)
  ✓ Alert-114680 escalated to human review
```

**Agent conclusion:**
> External IP `146.70.173.178` was actively attempting exploits (Log4j, Grafana Path
> Traversal) and communicating with suspicious OAST domains (`alibaba.oast.pro`,
> `aws.oast.online`). Traffic logs confirmed multiple completed sessions (`action=close`)
> with significant data transfer — potential C2 or exfiltration. Escalated.

---

## Common errors

| Error | Cause | Fix |
|---|---|---|
| `bad interpreter: No such file or directory` (exit 126) | venv path broken — old path baked into `oh` shebang | Rebuild venv: `rm -rf .venv && python3 -m venv .venv && pip install -e ".[dev]"` |
| `status=Closed` on resolve | Alert already closed — agent correctly skips | Re-open alert via API before re-testing |

---

## Environment variables (`.env`)

```bash
# --- FortiAnalyzer ---
FAZ_HOST=https://172.16.100.235
FAZ_USER=bis_cloud_api
FAZ_PASSWORD=<password>
FAZ_ADOMS="FortiCloud_Server:Burnaby Canada,FortiCloud_MIS_Colocation:worldwide colocations"
FAZ_VERIFY_SSL=false

# --- FortiSOAR ---
FORTISOAR_URL=https://bis-fsr.corp.fortinet.com
FORTISOAR_PUBLIC_KEY_FILE=/home/kaini/prj2026/fsr-prod.pub
FORTISOAR_PRIVATE_KEY_FILE=/home/kaini/prj2026/fsr-prod.priv
FORTISOAR_TENANT="Cloud Services"
FORTISOAR_SOURCE=IS_FAZ_MIS_Cloud
FORTISOAR_VERIFY_SSL=false

# --- SOC whitelist ---
# Path to YAML whitelist of IPs/CIDRs for auto-close without LLM. Unset = all alerts go through LLM.
# Never let the agent write to this file — human edits only.
SOC_WHITELIST_FILE=config/soc_whitelist.yaml

# --- LLM backend ---
OH_API_FORMAT=openai
OH_BASE_URL=http://172.16.100.38:8000/v1
#OH_BASE_URL=http://172.27.106.27:8000/v1
OH_API_KEY=sk-dummy-key
OH_MODEL=google/gemma-4-26B-A4B-it
OH_VERIFY_SSL=false
OH_STREAM=false        # Disable SSE streaming — prevents tool-call parsing failures from network re-chunking
OH_TEMPERATURE=0.2     # 0.1–0.3 recommended for batch SOC tasks

# --- NetBox ---
NETBOX_API_URL=https://10.121.56.31
NETBOX_API_TOKEN=<token>

# --- Alternative backends (swap in as needed) ---
# DashScope (Qwen):
# OH_API_FORMAT=openai
# OH_BASE_URL=https://dashscope-intl.aliyuncs.com/compatible-mode/v1
# OH_API_KEY=sk-...
# OH_MODEL=qwen2.5-72b-instruct
#
# Anthropic (Claude):
# OH_API_FORMAT=anthropic
# OH_BASE_URL=
# OH_API_KEY=sk-ant-...
# OH_MODEL=claude-sonnet-4-5
```
