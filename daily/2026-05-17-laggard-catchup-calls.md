# AI Laggard Catch-Up Calls — MSFT / META / ORCL

**Created:** 2026-05-17 (Sun)
**Thesis:** "AI laggards catch up" — beaten-down or perceived-loser AI exposure rebounds via rotation from extended infra/hyperscaler names. Patience acceptable (4-6 weeks), but not earnings binary risk.

## Status

| Leg | Status |
|---|---|
| **MSFT** | ✅ **FIRM** — execute Mon 5/18 |
| META | 🟡 PENDING DECISION |
| ORCL | 🟡 PENDING DECISION |

## Recommended structure (all 2-contract packs for "sell one to cover" strategy)

| Leg | Status | Expiry | Strike | Contracts | Mid | Cost |
|---|---|---|---|---|---|---|
| **MSFT $460C** | FIRM | Jun-26 (40d) | $460 (+9% OTM) | 2 | $5.15 | **$1,030** (limit $5.00 = $1,000) |
| META $700C | PENDING | Jun-26 (40d) | $700 (+14% OTM) | 2 | $5.05 | $1,010 (limit $5.00 = $1,000) |
| ORCL $210C | PENDING | Jun-5 (19d) | $210 (+9% OTM) | 2 | $4.72 | $944 |
| **Total if all 3** | | | | | | **~$2,984** |
| **MSFT only** | | | | | | **~$1,000** |

## Why Jun-26 (not Jul)

- "Beginning of July" weeklies don't exist (Jul-2, Jul-10 not listed). Jun-26 (5.7 weeks) is the closest fit within the 6-week max constraint.
- Pre-Jul-29 ER: no binary event risk inside option life.

## Why 2 contracts each

"Sell one to cover cost" strategy: when any leg doubles, sell 1 contract to recover the full 2-pack premium → ride the second contract as risk-free upside.

**Double-trigger spot prices (within ~2 weeks of entry):**

| Leg | Double trigger | Spot move needed | Sell 1 → recover |
|---|---|---|---|
| MSFT $460C | call to ~$10.30 | MSFT ~$445 (+5.5%) | **+$1,030** = full cost back |
| META $700C | call to ~$10.10 | META ~$685 (+11.5%) | **+$1,010** = full cost back |
| ORCL $210C | call to ~$9.44 | ORCL ~$210 (+8.8%) | **+$944** = full cost back |

## Per-leg thesis

### MSFT (FIRM)
- The cleanest "AI laggard" of the three — capex-shock derate (-22% from 52wH)
- +18% revenue growth re-accelerating; fortress balance sheet (0.04x net debt/EBITDA)
- 54 analysts, all Buy/Hold, avg target $561 (+33% upside)
- Risk: rotation thesis takes longer than 6 weeks; theta bleed accelerates

### META (PENDING)
- Best fundamentals: +33% revenue growth (latest Q), +57% EPS beat
- Q1 26 earnings was textbook strong; selloff is about *forward* capex guide ($100-115B FY26)
- 17x fwd P/E with 33% growth = PEG ~0.5 (cheapest of three)
- Low analyst target = $614 = current spot (no further downside per Street)
- Concern: deeper OTM strike (+14% OTM) is required to fit budget; needs bigger move to print

### ORCL (PENDING)
- ⚠️ Reframed: NOT a laggard play. Valuations at all-time highs (EV/Rev 10.6, EV/EBITDA 24.7)
- TTM FCF **negative -$24.7B**; net debt 3.5x EBITDA
- Pre-ER trade only — exit by Jun 5 expiry (before Jun-10 ER)
- This is a pre-earnings sentiment/IV trade, NOT a "value catch-up"
- Skip if uncomfortable with the leverage story; consider if you want pure pre-ER vol/sentiment exposure

## Stop-loss rules

### Spot-based hard stops (primary)

| Leg | Hard stop spot | % move | Why |
|---|---|---|---|
| MSFT | **< $400** | -5.2% | 50d MA break + ~70% premium loss in week 2 |
| META | < $580 | -5.6% | Recent base break + ~70% loss |
| ORCL | < $185 | -4.1% | Short-term support break + ~70% loss |

### Time-based hard stops

| Date | Action |
|---|---|
| May 26 (ORCL Day 9) | If ORCL < $200 → exit ORCL leg |
| Jun 5 | ORCL hard expiry — close all by EOD if not already exited |
| Jun 14 (MSFT/META Day 28) | If MSFT < $425 or META < $625 → exit |
| Jun 21 (1 week to MSFT/META expiry) | Hard close if still OTM — gamma trap in final week |

### Option-price stops (mechanical GTC orders)

Set sell-stop limits at:
- MSFT $460C: stop at $2.50 (50% loss)
- META $700C: stop at $2.50 (50% loss)
- ORCL $210C: stop at $2.30 (50% loss)

## Profit-taking rules

### Step 1: "Sell one to cover" trigger
When any leg's call price doubles (e.g., MSFT $460C reaches ~$10.30):
- **Sell 1 contract immediately** → recover 2-pack cost
- Hold remaining 1 contract as risk-free upside

### Step 2: Full exit on extension
| Leg | Full exit trigger |
|---|---|
| MSFT $460C | MSFT ≥ $475 OR call ≥ $20 |
| META $700C | META ≥ $720 OR call ≥ $30 |
| ORCL $210C | ORCL ≥ $215 OR call ≥ $7 (smaller — short expiry) |

## P/L grid at expiry — assuming Option A (all three, ~$2,984)

| Scenario | MSFT (Jun-26) | META (Jun-26) | ORCL (Jun-5) | Total |
|---|---|---|---|---|
| All flat | -$1,030 | -$1,010 | -$944 | -$2,984 |
| All +10% | -$190 (MSFT $464) | -$1,010 (META $676 — still OTM) | +$1,056 (ORCL $212) | -$144 |
| All +15% | +$4,970 (MSFT $485) | -$210 (META $706) | +$1,456 (ORCL $222) | **+$6,216** |
| All +20% | +$9,170 | +$6,390 | +$3,456 | **+$19,016** |

## P/L grid — MSFT-only execution (~$1,000)

| MSFT move | MSFT spot | Per-contract intrinsic | 2-contract P/L |
|---|---|---|---|
| -10% | $379.73 | $0 | -$1,030 |
| Flat | $421.92 | $0 | -$1,030 |
| +5% | $443.02 | $0 | -$1,030 |
| +9.7% (BE) | $470.30 | $5.15 | $0 |
| +10% | $464.11 | $4.11 | -$208 |
| +15% | $485.21 | $25.21 | +$4,012 |
| +20% | $506.30 | $46.30 | +$8,230 |
| +25% | $527.40 | $67.40 | +$12,450 |

## Execution checklist (MSFT, Mon 5/18 morning)

- [ ] Place limit buy order: 2× MSFT Jun-26 $460C at $5.00 mid
- [ ] If filled: set sell-limit GTC at $10.30 for 1 contract (cost-recovery trigger)
- [ ] If filled: set sell-stop GTC at $2.50 for both contracts (50% stop)
- [ ] Calendar: Jun 14 = Day 28 hard reassessment
- [ ] Calendar: Jun 21 = 1 week to expiry, mandatory close decision

## Decisions to make on META/ORCL

### META — questions to resolve
1. Are you comfortable with +14% OTM strike requiring a bigger move?
2. Is the "no FCF guidance concern" you flagged a deal-breaker, or is the +33% growth + 17x fwd P/E enough?
3. Comfortable holding through 4 weeks of potential theta drag?

### ORCL — questions to resolve
1. Now that we've reframed ORCL as "NOT a laggard" (multiples at ATH, negative FCF, 3.5x leverage) — is the pre-ER vol trade still attractive?
2. Comfortable with 19-day theta on a sentiment-driven bet?
3. Alternative: skip ORCL entirely and redirect $944 to dry powder for other opportunities

## What this trade is NOT

- Not a fundamental value investment (calls expire)
- Not a hedge (this is directional long-leverage)
- Not earnings-event speculation (MSFT/META expire pre-ER; ORCL exits pre-ER)
- Not part of the SaaS rebound trade ([NOW rebound](2026-05-17-now-rebound-trade.md) is separate)

## What this trade IS

A leveraged bet on:
- Capital rotation from over-extended AI infra (which is unwinding) into perceived laggards
- Pre-ER sentiment drift for ORCL specifically
- Modest 5-15% moves in MSFT/META giving 1-5x leveraged returns
- "Sell one to cover" structure means downside capped at premium but upside is asymmetric after cost recovery

## Related notes

- [NOW Rebound Trade (5/17)](2026-05-17-now-rebound-trade.md) — separate, higher-conviction SaaS rebound trade
- [Week-ahead context (5/17)](2026-05-17-week-ahead.md)
- [Original hedge plan (5/10)](2026-05-10-hedge-execution-plan.md)
- Finance methodology: `../notes/finance/research-methodology-finance.md`
