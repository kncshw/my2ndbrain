# Brief Config — the editable brain for the daily morning-brief routine

> **This file is the single source of truth for the morning brief.** The routine reads it every run.
> To change what the brief says, EDIT THIS FILE and commit it (in Obsidian, on GitHub, or via any Claude
> session) — no special session needed. Last edited: 2026-06-07.

## POSTURE
- **Current posture:** DEFENSIVE
- **Regime note:** Bear in control, high VIX. SEMI just cratered (June 5). Emphasize NEAR-TERM put protection.
- *(Change to NEUTRAL / OFFENSIVE here when your view changes — the brief's tone + hedge urgency follow this.)*

## CURRENT MARKET VIEW  *(free-text — update this daily/whenever; the brief weaves it in)*
- Volatility is high; I expect continued downside near-term. Protect the 84% gain.
- I do NOT trust myself to keep hedges on — the brief must push me to ROLL, not unwind.

## PORTFOLIO  *(update as the book changes)*
- Total: ~$400,000, three ~equal buckets:
  - GOOGL ~$133K
  - SEMI ~$133K (SMH, NVDA, INTC, MU, etc.; hedge proxy = SMH)
  - OTHERS ~$133K (proxy = QQQ)
- Names to hedge: GOOGL, SMH

## HEDGE SPEC  *(drives the put pricing + payoff table)*
- Style: **NEAR-TERM** (high VIX / bear) — target ~14 days to expiry, **5% OTM**
  - *(switch to ~45d / 10% OTM when posture relaxes to NEUTRAL)*
- Hedge instruments: SMH puts (semi book) + GOOGL puts
- Sizing: ~enough contracts to cover each bucket's notional
- **Hedge trigger:** if VIX > 18 → prominently recommend PLACING the near-term hedge today (or ROLLING the existing one)
- Payoff drops to show: -5%, -10%, -15%
- **TACTICAL overlay (optional, same-day only):** a 0-1DTE QQQ put (~1% OTM) — least time premium, highest gamma. Pays explosively if the drop is TODAY, worth ~$0 by tomorrow. NOT standing insurance and NOT the core hedge — a deliberate add ON TOP of the SMH/GOOGL hedge, used only on mornings with real conviction the move is today (CPI/Fed/acute continuation). Re-buy each morning only if conviction holds; do not treat the daily expiry as an excuse to drop core protection. Script args: `--tac_otm 0.01 --tac_dte 1`. Payoff drops: -1%, -2%, -3%.

## SCENARIOS  *(loss table — adjust % as your risk view changes)*
- S1 Pullback: GOOGL -10% / SEMI -15% / OTHERS -10%
- S2 Semi-led correction: GOOGL -12% / SEMI -22% / OTHERS -10%
- S3 2022-style bear: GOOGL -22% / SEMI -35% / OTHERS -20%

## RSI WATCHLIST  *(daily + weekly Wilder-14)*
- GOOGL, SMH, QQQ — flag weekly RSI > 70 (stretched) or < 30 (oversold)

## INDICATORS
- VIX, 10Y (^TNX), WTI (CL=F)

## NEWS TOPICS
- Fresh US econ data (Jobs/NFP, GDP, CPI/PCE) + today's calendar
- Breaking macro/geopolitical (Middle East/Iran, Fed, rates, oil)
- GOOGL / Alphabet
- Semiconductors (NVDA, SMH, INTC, MU, TSM, AVGO)

## THE ANCHOR  *(past-you → present-you; keep verbatim unless you want to rewrite it)*
You were up +84% at peak. On June 5 2026 you lost 6.5% in one day — the risk you had been uneasy about.
You were not blind to it: that morning you bought 11 QQQ puts, then sold 10 and kept 1. That 1 made +$1,300 —
the 10 you dumped would have added ~$13,000. Your weakness is not spotting risk or even hedging — it is that
you UNWIND your protection. Place the hedge today, and do NOT dismantle it.
