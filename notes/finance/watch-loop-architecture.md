# Watch–Analyze–React Loop Architecture

Operational framework for systematic portfolio risk monitoring.

## The loop

```
WATCH (signals in)  →  ANALYZE (decision rules)  →  REACT (pre-committed actions)
       ↑                                                          ↓
       └────────────────  outcome feedback  ──────────────────────┘
```

Three layers; each runs at its own cadence.

## Tier framework (ordered by time-sensitivity)

| Tier | Risk | Time signature |
|---|---|---|
| **0** | **Fed / CPI / rates** | **Hours to days** |
| 1 | Demand destruction (scaling wall, less memory, hyperscaler capex cuts) | Days to weeks |
| 2 | Memory-specific (HBM oversupply, MU GM compression) | Quarter-to-quarter |
| 3 | Supply / structural (TSM capex cut, NVDA inventory build) | Quarters |
| 4 | Geopolitical (China export controls, war) | Unpredictable |
| 4.5 | Power / permitting / political | Months to quarters (mostly mouth-noise until specific project breaks) |
| 5 | Technical confirmation (RSI divergence, breadth) | Confirms what's already happening |

## Operating principles

### Asymmetric watch — flag DOWNSIDE only
User is a structural bull. Watch becomes a downside risk monitor, not a generic news scanner.

| Tier | Flag | IGNORE |
|---|---|---|
| Tier 0 | Hot prints **vs consensus**, hawkish Fed pivots | Cool prints, dovish surprises |
| Tier 1 | Capex CUTS, scaling-wall claims, "less compute needed" announcements | Capex raises, new model launches |
| Tier 2 | HBM oversupply, MU GM compression | TAM upgrades, pricing strength |
| Tier 3 | NVDA inventory build, TSM capex cut, channel stuffing | TSM capex raise, lead-time extensions |
| Tier 4.5 | Specific projects killed AND hyperscaler comment | Politicians shouting (mouth only) |
| Tier 5 | Bearish divergence, breadth break, semis-to-broader rotation away | Confirming uptrend signals |

### Decision authority — Claude flags, user decides
Triggers are **alerts**, not commitments. Each fired trigger surfaces:
- What fired
- Recommended action
- Estimated cost / urgency
- "Go / no-go / wait" decision request

User makes the call. No auto-execution.

### CPI rule — relative, not absolute
- Trigger: **print above consensus** (either headline or core)
- Ignore: absolute numbers ("0.3 vs 0.4") — they're a numbers game
- Cool print = bullish, no alert needed

## Cadences

| Cadence | What runs | Output |
|---|---|---|
| Weekdays ~7 AM PDT | Daily Tier-0 brief | `../../daily/YYYY-MM-DD-am-brief.md` |
| Sunday evening | Full week-ahead scan (RSI/divergence, news Tier 1–3, catalyst calendar) | `../../daily/YYYY-MM-DD-week-ahead.md` |
| First Sunday/month | Tier 4.5 monthly review (politics, permitting, structural) | `../../daily/YYYY-MM-monthly-review.md` |
| On demand | Manual trigger via prompt to Claude | Inline |

## Output format

Each report uses a consistent structure:

```markdown
# AM Brief — YYYY-MM-DD

## Status: 🟢/🟡/🔴 [one-line summary]

## Tier 0 — Fed/CPI/Rates
- Releases today + consensus
- Yields, fed funds futures
- Trigger status

## Tier 5 — Technical
- RSI snapshot (key indexes + holdings)
- Divergence check (bearish only)
- NDX–SMH spread

## Open alerts requiring decision
(none, or 🔴 with recommended action)

## Sources / verification
```

Traffic-light header makes status scannable. "Open alerts" is the only section demanding action — everything else is informational.

## Implementation phases

### Phase 1 — Validation (now → 2-3 weeks)
- Use **CronCreate** inside Claude Code for scheduling
- Iterate on tier definitions, thresholds, output format
- Decide notification preferences (currently undecided)
- Decide sync architecture (currently undecided)

### Phase 2 — Production (after validation)
- Migrate to **system crontab** firing headless Claude Code sessions
- Persists across reboots, no 7-day expiry
- Requires Mac to be awake at fire times

## CronCreate vs system crontab — key differences

| Property | System `crontab` | CronCreate |
|---|---|---|
| Where it runs | OS scheduler | Inside a running Claude Code session |
| Requires Claude running? | No | Yes, REPL must be idle |
| Survives reboots | Yes | Only with `durable: true` |
| Auto-expiry | Never | 7 days max |
| What it executes | Shell commands | A prompt to Claude |
| Cost | Free | API tokens per fire |

## Notification options (DECISION PENDING)

User has not decided. Options on the table:

| Channel | Latency | Best for |
|---|---|---|
| Markdown to vault | seconds-minutes (iCloud sync) | 🟢 routine reports |
| Email (Gmail SMTP via Python helper) | seconds | 🟡 watch events; passive review |
| `PushNotification` (Claude Code built-in) | instant | 🔴 alerts, interrupt-style |
| iMessage (AppleScript) | instant | 🔴 alerts, alternative to push |

Constraint: User can't take Mac everywhere; iPhone is always with them. → vault needs to sync to iPhone for mobile reading.

## Sync architecture (DECISION PENDING)

User has not decided.

| Option | Cost | Pros | Cons |
|---|---|---|---|
| **Obsidian Sync** (official) | $4–10/mo | E2E encrypted, history, robust | Costs money |
| **iCloud Drive** | Free | Native Apple, easy setup | Sync lag, occasional conflicts |

Vault must move from `/Users/kaini/prj-2026/my2ndbrain/` to whichever sync location is chosen. CLAUDE.md and memory entries will need a one-line path update.

## What's NOT included in the watch loop

- **Execution.** This system *signals*; user *executes* trades via their broker.
- **Position management ledger.** The watch reports current technical/macro state but doesn't track positions or P&L.
- **Bullish surprises.** Asymmetric watch means upside catalysts get no special handling.
- **Real-time intraday.** Briefs are daily/weekly cadence; not minute-by-minute.

## Open offers from prior session (still pending decision)

- Save catalyst-calendar as reusable Sunday-evening template (separate from this loop arch)
- Adapt other equity-research skill templates (`thesis-tracker`, `sector-overview`, `morning-note`)
- Add automated daily-RSI cross-check (live finviz comparison)
- Free options-chain workflow using yfinance `Ticker.option_chain`

## Known limitations / future portability work (DEFERRED 2026-05-10)

**Issue:** the entire stack is hardwired to this Mac Air. Absolute paths (`/Users/kaini/prj-2026/scripts/`) appear in CLAUDE.md, methodology note, memory feedback file. Memory itself lives at `~/.claude/projects/-Users-kaini-prj-2026/` which doesn't auto-sync. Running on a second host (other Mac, work laptop, cloud VM, Linux server) requires manual recreation of structure and re-establishment of context.

**Severity:** blocks multi-host operation. Not blocking single-host (Mac Air) work — the only place we currently run.

**Status:** deferred. Project is not mature enough to warrant the refactor cost yet.

**Proposed approach when revisited:**
1. **Quick:** replace absolute paths with relative (`./scripts/` or `$PROJECT_ROOT/...`) in CLAUDE.md, methodology note, memory feedback file.
2. **Medium:** add `./BOOTSTRAP.md` or `./my2ndbrain/BOOTSTRAP.md` that documents first-time setup on a new host and reconstructs context if memory files are absent. Vault becomes the durable source of truth; memory files become local cache.
3. **Production:** put the project in a private git repo (e.g., private GitHub), add `.gitignore` for secrets, `setup.sh` for Python deps + Claude Code CLI install. Clone-and-go on any host.

**Unavoidable per-machine setup** (will always need manual work):
- Python deps (`pip install yfinance pandas numpy`)
- Claude Code CLI install
- API keys in env vars
- MCP server installs
- macOS-specific notification paths don't work on Linux

**When to revisit:** when there's a concrete second host in play (e.g., user starts using a work laptop or stands up a cloud VM for cron jobs).

## Historical analog reference

The 2021 peak / 2022 bear is the cleanest base-rate reference for today's setup. Full table-form analysis at:
**[historical-bear-analog-2021-2022.md](./historical-bear-analog-2021-2022.md)**

Key reference points the watch loop uses:
- **Bearish divergence pattern** (SMH/SOX price new high + RSI lower high) was THE technical signal in 2021 — Tier 5 should watch for this first
- **2021 SMH peak wkRSI = 74.2** (95th %ile), today = 84.5 (99.9th %ile) → today's technical picture is MORE stretched
- **2021 SMH–NDX spread = +1.1** (in sync), today = +10.3 (wide) → watch for spread compression
- **Drawdown magnitude reference:** SMH -45%, QQQ -36%, NVDA/AMD -65% over 9–13 months — use for hedge sizing
- **First 15% drops without Fed action** — possible even before any Tier 0 trigger fires

## Pilot run

First pilot: Monday morning AM brief, fired manually Sunday afternoon 2026-05-10 (24h ahead).
File: `../../daily/2026-05-11-am-brief.md`
Purpose: validate output format and signal quality before committing to scheduled fires.

## Related notes

- **[research-methodology-finance.md](./research-methodology-finance.md)** — technical conventions (yfinance, Wilder RSI, timeframe labeling) that this loop relies on
- **[historical-bear-analog-2021-2022.md](./historical-bear-analog-2021-2022.md)** — base rates and pattern checklists used by Tier 5 (technical) and for hedge sizing
- **[README.md](./README.md)** — index of all finance notes
