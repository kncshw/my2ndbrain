# Brief Routines — Operating Runbook (READ ME FIRST)

> **Authoritative how-to for the daily reminder system.** Any Claude Code session (or Kai) can operate
> everything from this file + the repo. Supersedes the old `daily-brief-routine-plan.md`.
> Last updated: 2026-06-07.

## What this is
Three scheduled Anthropic cloud routines (Claude Code Routines / `RemoteTrigger`) push a daily
risk brief to **Telegram**. Purpose: fix Kai's execution gap (June 5 2026 — under-hedged, unwound
10 of 11 QQQ puts). Past-Kai reminds present-Kai to hold protection. All driven by ONE config file.

## The three routines
| Name | Routine ID | Cron (UTC) | Time (PT) | Does | Script |
|---|---|---|---|---|---|
| morning-brief | `trig_01S6zmBEeEoH9jVr8UkRG5Jc` | `0 14 * * 1-5` | 7:00am wkdays | Full brief: posture, anchor, RSI, loss table, core hedge + tactical QQQ, news | `scripts/daily_brief.py` |
| before-close-reminder | `trig_01EF9B1dCazT519rTAYo3F7K` | `0 19 * * 1-5` | 12:00pm wkdays | Short: posture + VIX/10Y/WTI + breaking news + AMC earnings | `scripts/preclose.py` |
| night-reviewer | `trig_01AKy8q78YiAjiJTG1Upr1cG` | `0 3 * * 2-6` | 8:00pm wkday eves | Nudge: tonight's posture + tomorrow's catalysts + "review/adjust" | (config + WebSearch) |

`RemoteTrigger {action:"list"}` enumerates them live anytime.

## ⭐ HOW TO CHANGE POSTURE (the main task)
**Single source of truth = `notes/finance/brief-config.md`.** All three routines read it each run.
1. Edit `notes/finance/brief-config.md`:
   - `POSTURE` — DEFENSIVE / NEUTRAL / OFFENSIVE (+ regime note)
   - `CURRENT MARKET VIEW` — free text, woven into the briefs
   - `HEDGE SPEC` — switch style if needed (near-term `--otm 0.05 --dte 14` ⇄ longer `--otm 0.10 --dte 45`); the morning agent maps DEFENSIVE→near-term, NEUTRAL→longer
   - `SCENARIOS`, `PORTFOLIO`, `THE ANCHOR` — as needed
2. Commit + push to **main** (routines clone `main`):
   `git add notes/finance/brief-config.md && git commit -m "posture: <x>" && git push origin main`
3. **Takes effect on the next scheduled run automatically.**
4. **To apply IMMEDIATELY** (push a fresh brief now): trigger a manual run —
   `RemoteTrigger {action:"run", trigger_id:"trig_01S6zmBEeEoH9jVr8UkRG5Jc"}` (morning) or the relevant ID.
   Or use the `schedule` skill ("run now").

## Manage routines
- Use the **`schedule` skill** or the **`RemoteTrigger`** tool: `list` / `get` / `update` (partial; for prompt changes resend full `job_config`) / `run`.
- Editing a routine's behavior = `update` with the new prompt. Changing cadence = `update` `cron_expression` (UTC).
- **Cannot delete via API** → https://claude.ai/code/routines.

## Architecture / environment
- **Repo:** github.com/kncshw/my2ndbrain (private). Routines clone `main`. Config + scripts live here (single source of truth).
- **Environment:** `env_011vnutct71APKLmMZNb9bR6` (anthropic_cloud). Holds: **Network access = Full**, and env vars **`TELEGRAM_BOT_TOKEN`** + **`TELEGRAM_CHAT_ID`** (chat id `8844422870`). These are set in the environment UI (claude.ai), NOT via API — do not delete them or Telegram breaks.
- **Delivery:** Telegram only (curl to Bot API, HTML + plain-text fallback). No repo archive (dropped — too verbose).
- **Compute:** Python + yfinance in the cloud sandbox; `pip install lxml` needed for earnings (`get_earnings_dates`). yfinance reaches Yahoo because network=Full.

## Data integrity & caveats
- `scripts/daily_brief.py` prints `DATA_CHECK`: cross-checks computed RSI vs **finviz**, flags stale (>4d old) or null/absurd feeds. If `WARN`, the brief opens with a ⚠️ DATA WARNING line.
- Every actionable brief ends with a **"verify the live quote at your broker before trading"** footer. Data is delayed/EOD from free yfinance (fragile, no SLA); option prices/payoffs are estimates.
- `^TNX` raw value already equals the yield in % (e.g. 4.54 = 4.54%) — do NOT divide by 10 (earlier bug).
- **DST:** all crons are UTC, correct for PDT. When clocks fall back (~Nov 2026), add 1h to each UTC cron.

## Quick sanity test (any session)
`RemoteTrigger {action:"list"}` → should show all 3. `RemoteTrigger {action:"run", trigger_id:"..."}` → fires a test; result lands in Telegram in a few min (API does not return the transcript — check Telegram / claude.ai/code/routines).
