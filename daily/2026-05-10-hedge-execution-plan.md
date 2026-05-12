# Hedge Execution Plan — 2026-05-10

Status: approved, pending execution. Budget: ~$2,000 of protection. All positions in tax-advantaged accounts.

## Thesis (one-liner)

Semis sector at historically extreme readings (SMH wRSI 84.5, +54% vs 200DMA, NDX-SMH spread 10.3 vs 2021-peak 1.1, base rate from this RSI bin: -22% median max-DD over 12M). No bearish divergence yet → hedge, don't max-short. INTC is the standout name (+195% vs 200DMA, wRSI 90.5). GOOGL hedge is for AI-multiple-compression risk on largest holding; fundamentals themselves are accelerating.

## Final stack

| # | Leg | Action | Strike(s) | Expiry | Mid | Cost / Contract |
|---|---|---|---|---|---|---|
| 1 | SMH put | BUY | $510 (10% OTM) | 2026-05-29 (19d) | $6.38 | **-$638** |
| 2 | GOOGL put (near) | BUY | $360 (10% OTM) | 2026-06-18 (39d) | $3.58 | **-$358** |
| 3 | GOOGL put (far) | BUY | $360 (10% OTM) | 2026-07-17 (68d) | $7.12 | **-$712** |
| 4 | INTC collar (weekly, rolling) | BUY put / SELL call | $110 / $150 | 2026-05-15 (5d), roll Fridays | -$0.07 | **~-$7 × N contracts** |

**Net opening cost: ~$1,708** + INTC sizing (essentially free per contract). Within $2,000 budget regardless of INTC share count.

## Per-position rationale

### SMH May-29 $510 put

- Pure bet on NVDA earnings (May 20) as cycle catalyst — NVDA insider tape supports: $213M open-market sales Jan–Mar 2026, zero buys (CFO Kress, EVP Puri $145M, Dir Stevens $38.5M)
- 47% basket coverage on $120K semi exposure (NVDA in basket: 100+ shares ≈ $21.5K, also gets partial NVDA cover via this proxy)
- Loss capped at $638 if NVDA beats and SMH rips
- Breakeven: SMH at $503.62 by May 29 (-11.1%)

### GOOGL Jun-18 + Jul-17 $360 puts (calendar, same strike, staggered)

- Puts-only, no call leg (user preference: don't risk assignment on largest holding)
- Layered coverage: 200 shares notional (53%) protected first 39 days, 100 shares (27%) days 40–68
- Both expire pre-Q2 earnings (Jul 23) — no ER vol risk
- Calendar approach saves $354 vs 2× Jul puts while preserving full early-window coverage
- Fundamentals strong (Q1 rev +21.8% YoY, op margin 36.1% expanding); hedge is multiple-compression insurance only

### INTC weekly $110/$150 collar (rolling)

- Zero-cost structure: $110 put -$7.88 + $150 call +$7.72 = essentially flat
- Protection at -12% (below $110), upside cap at +20% ($150) — generous given +195% above 200DMA already
- Weekly rolls chosen for flexibility (re-strike each Friday based on price action)
- Start with May-15 — most liquid weekly on chain (OI 7,170 put / 10,338 call)
- Per-week cost trivial (~$7–40); over 5 rolls cumulative ~$1.50 more than monthly Jun-18 equivalent
- INTC IV ~93% — both legs benefit from elevated vol, near-net-zero vega exposure

## Execution notes

- **Limit orders only.** SMH spreads are tight enough for marketable limits; INTC 95% IV → wider spreads, place limits at mid or slightly worse to avoid bid/ask leakage.
- **Staggered entry across multiple days** (not all in one session). Each leg has its own optimal IV window.

### Suggested entry sequence

| Day | Leg | Reason |
|---|---|---|
| **Mon–Wed (5/11–5/13)** | INTC May-15 collar | Must place before May-15 expiry; zero-cost so price not a factor |
| **Mon–Wed (5/11–5/13)** | GOOGL Jun-18 + Jul-17 puts | Before Google I/O — buy pre-event IV, avoid post-event vol crush bouncing back into expensive territory |
| **Mon–Tue (5/18–5/19)** | SMH May-29 put | Before NVDA ER (5/20). Don't wait past 5/19 — IV builds into ER. If SMH rips further before then, that's a better entry (more OTM, cheaper) |

### Hard constraints

- INTC: place by Wed 5/13 (or skip to next week's roll if not placed)
- GOOGL: place before I/O announcement
- SMH: place no later than Tue 5/19 (the day before NVDA ER)

### Order type / sizing

- Use limit orders at mid or slightly worse. INTC collar legs may need legging in separately given 95% IV spreads.
- **INTC sizing:** pending share count. At any reasonable size (1–5 contracts), opening cost is ≤$35.

## Decision triggers

**SMH:**
- NVDA beats and SMH rips above $580 → let expire worthless, reassess thesis
- NVDA misses → put gains; consider rolling out to Jul/Aug at higher strikes to extend
- SMH drops to $510 by mid-May → put is ATM with intrinsic value; can hold to expiry or harvest

**GOOGL:**
- I/O catalyst (mid-May): if positive surprise pops stock past $420, puts decay; let ride to expiry
- Q2 ER prep (mid-July): if no rollover by Jul-10, let Jul put expire; reassess Aug/Sep cycle
- If GOOGL drops below $380 in May/Jun: harvest near-leg put profit, hold far leg

**INTC weekly:**
- If INTC ripped to $145+ by Friday → don't roll. Let assigned at $150 if hit (would be +20% gain anyway), or close just before assignment if it actually approaches strike.
- If INTC drops to $115: harvest put profit. Reassess whether to re-establish.
- If thesis broken (parabolic continues 2+ weeks unfazed): stop rolling, accept the cycle is wrong.

## Open items

- [ ] INTC share count → contract sizing for weekly collar
- [ ] Execute trades during NYSE hours, ideally avoid first 30 minutes (volatile opens)

## Watch loop tier

This is a **Tier 4 action** per `notes/finance/watch-loop-architecture.md` — extreme readings + pending decisions + execution underway. Move back to Tier 2-3 monitoring once positions are open.
