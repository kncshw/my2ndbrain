# Daily Brief Routines — Preliminary Plan (HANDOFF)

> ⚠️ **SUPERSEDED (2026-06-07).** This was the original plan. The system is now built and live —
> see **`brief-routines-runbook.md`** for the authoritative, current operating guide (3 routines,
> Telegram delivery, config-driven posture). This file is kept only as historical record.

> **Status:** Preliminary plan, NOT yet created. Drafted 2026-06-06 in a resume session; handing off to a
> finance-focused Claude session to finalize and create.
> **Context:** User took a large portfolio loss on Fri 2026-06-05. Root cause (their words): they had a
> hedging thesis but did NOT act on it — "I knew something was going to happen but neither prepared nor
> believed myself." They had ~80%+ unrealized profit and under-hedged. The fix they want: a recurring
> brief that puts THEIR OWN plan back in front of them daily, checked against live data, so execution no
> longer depends on in-the-moment conviction.

## What the user decided
1. **Privacy:** ✅ Confirmed OK. `my2ndbrain` is a private GitHub repo (`github.com/kncshw/my2ndbrain.git`).
   User is fine with a cloud routine cloning it (incl. portfolio/positions) and committing briefs back.
2. **Feature:** Anthropic **Routines** (scheduled managed cloud agents) via the `/schedule` skill →
   `RemoteTrigger` tool. Runs on Anthropic cloud, laptop can be off.
3. **Billing:** User is on **Claude Max 5x**. Pre–June 15 2026: draws from Max quota. Post–June 15:
   draws from the included ~$100/mo Max-5x agent credit pool. One brief/run is small → effectively no
   extra cost, BUT verify at claude.ai/settings/usage, especially after the June 15 billing change.
4. **Environment:** Default (id: `env_01FR8w6pXa4B2zmyjqPeLurr`, anthropic_cloud).
5. **Model:** default claude-sonnet-4-6 (confirm; could use a stronger model for analysis).

## The three runs (times in PT; cron in UTC; user is America/Vancouver, currently PDT = UTC−7)
| Run | Local time | Purpose | Cron (PDT, correct NOW) |
|-----|-----------|---------|--------------------------|
| **Morning briefing** | 7:30am PT, weekdays | Full brief: restate plan, overnight news + futures, check holdings/indexes vs live price+RSI, flag any trigger hit | `30 14 * * 1-5` |
| **Noon pre-close** | 12:00pm PT, weekdays | Quick check ~1h before 1pm PT close: is any pre-committed hedge trigger hit? yes/no + action | `0 19 * * 1-5` |
| **Night watcher** | 8:00pm PT, weekdays | Recap + next-day setup; after-hours / Asia-Europe moves | `0 3 * * 2-6` (8pm PT crosses midnight UTC → next UTC day; Tue–Sat = Mon–Fri evenings) |

⚠️ **DST:** these are correct for PDT now. When clocks fall back to PST (Nov 2026), add 1 hour to each
UTC value. Cron does not auto-adjust.

## Delivery
- **Default / reliable:** commit brief to `my2ndbrain/daily/` (date-prefixed `YYYY-MM-DD-...md`) and push.
  Works today, private, no connector needed. **Start here.**
- **Email:** user asked for email. BLOCKER — no claude.ai connectors currently connected. User must add
  an email/Gmail connector at https://claude.ai/customize/connectors first. Caveat: interactively-authed
  connectors can be flaky in headless/cron runs, so keep vault-commit as the dependable backbone.
- **GitHub nudge:** commits trigger repo notifications if user watches the repo / has GitHub mobile.

## Scope of each brief (user approved "restate plan + check triggers + news/macro")
Restate the user's written hedging plan/thresholds → check key holdings & indexes against live
price/RSI → flag any trigger that's hit with a clear action → overnight/intraday news + futures + macro
events that could move the book. Use the finance scripts (`/Users/kaini/prj-2026/scripts/lib_finance.py`:
`snapshot`, `divergence_check`, `ndx_smh_spread`, `base_rate`, `rsi`) — BUT note these are LOCAL, not in
the vault repo, so a cloud routine can't import them. Either (a) port the needed helpers into the repo,
or (b) have the routine use web data + its own calc. Resolve this when finalizing.

## 🔴 BIGGEST OPEN ITEM — rebuild the hedging plan FIRST
The briefs only have value if they restate a CURRENT written plan. Friday's loss likely invalidated the
prior plan, and much of it lived in the user's head, not on paper. **Before/alongside creating the
routines, rebuild the hedging plan into the vault** (thresholds, triggers, "if X then hedge Y no debate"
pre-commitments) so the daily brief has real teeth. This is the actual fix for the execution gap — the
automation just surfaces it. Existing references: `watch-loop-architecture.md`,
`research-methodology-finance.md`, `historical-bear-analog-2021-2022.md`, and the Cisco thesis note.

## Next-session checklist
1. Rebuild the post-loss hedging plan with the user (written, rule-based, pre-committed triggers).
2. Decide local-helper strategy (port lib_finance into repo vs web-data-only).
3. Write a strong, self-contained prompt for each of the 3 routines (remote agent starts with zero context).
4. Create the 3 routines via `/schedule` (RemoteTrigger create), vault-commit delivery; add email later if
   user connects a connector.
5. Verify usage/billing at claude.ai/settings/usage after first runs (and again after June 15).
