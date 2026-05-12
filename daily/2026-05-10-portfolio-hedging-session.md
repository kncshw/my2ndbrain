# Portfolio Hedging Session — 2026-05-09 to 05-10

## TL;DR

- The recent run is **historically extreme in semis specifically**, not in the broader market. SMH weekly RSI 84.5 (99.9th percentile of all-time), SOX 85.5 (99.7th percentile, 3.5 RSI points below the March 2000 dot-com peak).
- **QQQ and SPX are elevated but not in the historical "danger zone."** QQQ at 74.2 is rare (95th percentile) but the historical base rate at this specific RSI level has been *positive* (89% positive 12M returns).
- **The actionable trade is hedging the semi book.** Other slices of the book either don't need hedging or are already de-risked.

---

## Portfolio frame (three roughly equal buckets)

| Bucket | ~Weight | Names | View |
|---|---|---|---|
| Mega-cap quality | 1/3 | **GOOGL** | At ATH, in "rewarded spender" camp; concentration risk |
| Semi + Optical | 1/3 | NVDA, TSM, AVGO (comfortable), INTC, AMD, MU (concerned), COHR, GLW (optical, concerned) | Most stretched bucket |
| Other big-tech / index | 1/3 | QQQ, MSFT, META | MSFT/META already corrected -22%; QQQ extended but not extreme |

### Account constraints
- **Tax-free retirement account** — no §1259 issues, no tax cost on selling.
- **Options permissions:** long puts + covered calls only. **No spreads.**
- **Share counts:** Only **GOOGL and INTC** have ≥100 shares (covered call eligible). Other positions too small for individual call writing.

---

## Data findings

### Weekly RSI percentiles (May 8 close, computed via yfinance, Wilder method, ≥2y history)

| Index | Weekly RSI | All-time percentile | Note |
|---|---|---|---|
| SMH | **84.5** | **99.9%** | Essentially ties all-time high (84.6 in Nov 2017) |
| SOX | **85.5** | **99.7%** | 3.5 points below March 2000 dot-com top |
| QQQ | 74.2 | 95.2% | Rare but base rate constructive at this level |
| NDX | 74.2 | 93.1% | — |
| SPX | 69.4 | 85.6% | Elevated, historically benign |

### Base rates from historical RSI bins

**SMH/SOX [80–90) bin:** 62% / 86% negative at 12M, median max DD -22% / -45%. Every prior reading at this level produced significant drawdowns within 12 months.

**QQQ [74–76) bin (current):** Only 11% negative at 12M, median +16.2%, median max DD -11.7%. **Danger zone for QQQ kicks in at 78+.**

**SPX even at 80+:** Only 19% negative at 12M. SPX is RSI-resilient.

### Individual name RSI standouts
- **INTC weekly RSI 90.5** — genuinely once-in-an-era. Most stocks never see weekly 90s.
- **MU 84, AMD 85** — extreme cohort.
- **GOOGL daily 84, weekly 75** — daily extreme but weekly elevated, not extreme.
- **NVDA weekly 65** — surprisingly tame; "still cheap" thesis supported by RSI math.
- **MSFT 46, META 46** — already de-risked.

---

## Hedging plan (within account constraints)

| # | Action | Rationale |
|---|---|---|
| 1 | **SMH long put** (6-month, ~10% OTM) | Core macro hedge for the semi book. RSI in 99.9th percentile + base rate 62% negative 12M. Highest-conviction trade. Cash-funded since most semi positions can't write calls. |
| 2 | **GOOGL legged collar** | Sell 2–3M covered call ~10% OTM ($440-ish), buy 6M put ~10% OTM ($360-ish). Premium partly offsets put cost. Hedges 1/3 of book + concentration risk. |
| 3 | **INTC covered call** ($130 strike) | Generates premium AND functions as auto-exit. INTC weekly RSI 90.5 — if called away, that's a great exit. Don't need separate INTC put (covered by SMH). |
| 4 | **COHR/GLW** | Too small for covered calls; long puts inefficient. Cleanest move: trim if nervous (no tax cost). |
| 5 | **MSFT, META, QQQ, broader market** | **No hedge.** MSFT/META already corrected -22%. QQQ at 74 historically constructive. SPX RSI-resilient. Paying for unmaterialized risk. |

### Sizing / probability framing
- **SMH hedge:** ~62% historical hit rate of paying off in 12 months. Highest conviction.
- **QQQ hedge:** ~11% base rate of being needed at current RSI. Mostly wasted premium.
- **Watch trigger:** if QQQ weekly RSI crosses 78, recalibrate.

---

## Methodology established (saved to CLAUDE.md + my2ndbrain/notes/research-methodology-finance.md)

- **yfinance is default for numerical data**; web search only for narrative/news.
- **RSI(14) Wilder, daily and weekly** — featured indicator.
- **Always label timeframe explicitly** ("daily" vs "weekly"). Daily and weekly diverge meaningfully.
- **Weekly RSI needs ≥2y history** for Wilder convergence.
- **Cross-check daily RSI against finviz** — verified exact match for SMH, QQQ, INTC.
- **Discuss before writing** — no rushed polished documents until thinking is mature.

---

## Catalyst calendar — week of May 11–15

| Date | Event | Impact |
|---|---|---|
| Mon 5/11 | ASMC conference opens, Albany NY (5/11–14) | M (foundry/INTC commentary) |
| **Tue 5/12** | **US CPI April, 8:30 AM ET** | **HIGH — single most important event** |
| Wed 5/13 | US PPI April, 8:30 AM ET | M–H |
| Thu 5/14 | Retail Sales, Industrial Production | M (verify times) |

**No holdings have earnings this week.** NVDA earnings **May 20** (next week, Wed after-close) — IV will ramp through this week.

### Pre-CPI positioning thoughts
- If executing the SMH put, doing it pre-CPI captures the binary catalyst. Slightly elevated IV, but asymmetric reward.
- If selling covered calls on GOOGL/INTC, this week is a good window — IV richening into NVDA earnings + macro.

---

## Open questions / next session

- **Option market check:** What are SMH put IV vs realized vol actually showing? Is the option market already pricing the risk in (puts expensive) or not (cheap insurance)?
- **Hyperscaler capex trajectory:** the actual demand signal. Q1 hyperscaler capex was raised, not cut — that's a *bullish* tell that contradicts the bearish RSI signal. Worth digging into.
- **Conditional probability:** what's the QQQ base rate when RSI is 74 *and* CAPE is in the 95th percentile (today's regime)? Sample is small (1999-only) but the answer matters for sizing.
- **Specific strikes / dollar sizing:** When ready to execute, run actual option chain pricing for SMH and GOOGL puts/calls.

## Open offers I made but didn't act on

- **Save catalyst-calendar as a reusable Sunday-evening template** at `./my2ndbrain/notes/template-catalyst-week-ahead.md`. Workflow:
  - Pull next week's earnings dates for the book via yfinance
  - Pull macro calendar (BLS schedule, Fed events, key conferences) via web search
  - Compile into `./my2ndbrain/daily/YYYY-MM-DD-week-ahead.md` using the format from the 5/10 example
  - Flag highest-impact events + position implications
  - Trigger phrase: "run the week-ahead catalyst pull"
  - Decision pending — say yes and I'll create the template file.

- **Adapt other equity-research skill templates** (`thesis-tracker`, `sector-overview`, `morning-note`) into retail-investor versions saved in `./my2ndbrain/notes/`. Same idea: harvest the prompt structure from the financial-services marketplace plugins without installing the broken paid-data dependencies.

- **Add an automated daily-RSI cross-check** to the script in CLAUDE.md (pull live finviz RSI, assert match against yfinance computation to ±0.05). Self-test on every future analysis. Decision pending.

- **Free options-chain workflow** using yfinance's `Ticker.option_chain` to do real IV-vs-realized-vol analysis on SMH puts before sizing the hedge. Adapts the LSEG `option-vol-analysis` skill structure to free data. Decision pending.

---

## Files updated this session

- `./CLAUDE.md` — lean: vault paths + pointer to finance methodology
- `./my2ndbrain/notes/research-methodology-finance.md` — yfinance + RSI conventions, timeframe rules
- Memory: routes any finance prompt to load the methodology note first
- This file (`./my2ndbrain/daily/2026-05-10-portfolio-hedging-session.md`) — session summary
- (Earlier rushed draft `2026-05-09-realize-vs-hedge-analysis.md` left as record of pre-mature thinking)
