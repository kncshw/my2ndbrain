# Week Ahead — Week of 2026-05-18

## Status: 🟡 Cycle pullback in progress, NVDA ER (Wed 5/20) is the binary event

INTC parabolic broke this week (-16% from 52wH). Memory/optical names (MU, AMD, COHR, GLW) also pulled back hard from peaks. SMH-NDX spread compressed 10.6 → 7.7 — first tactical confirmation of cycle thesis. **No bearish divergence yet** (no failed retest of highs), but the setup is now in place.

## Hedge stack — current state

| Position | Status | Notes |
|---|---|---|
| 1× SMH May-29 $510 put | ✅ HELD | Entry $638. SMH at $556.34 → put OTM by $46. MTM est. $400–700 (IV expanded). Insurance through NVDA ER. |
| 1× INTC May-15 $110/$150 collar | ✅ CLOSED Fri 5/15 | Small profit. INTC dropped to $108.77, $110 put expired ITM. **Not re-hedging** — user holds long-term @ <$40 basis, willing to add on retest to $90s. |
| **1× NVDA May-22 $250 call SELL (new this week)** | ⏳ EXECUTE Mon/Tue | Sell @ ~$1.94 mid. Collect $194 premium. Captures peak ER IV (73.6%) + IV crush post-ER. |
| GOOGL hedge | ⏸ WAITING | Plan: enter Jul-17 $360 put only if I/O pumps GOOGL >$400. Otherwise hold unhedged — $200 cost basis is the hedge. |

## NVDA/SMH thesis — final wrap

**User thesis (decided 5/17):** NVDA ER will be a "nothing burger" — fundamentals strong (GPU shortage, networking demand), price moves ±5% but no real catalyst. Memory already retreated; remaining downside concentrated in NVDA-specific reaction.

**Why we kept the SMH put despite the thesis:** Five paths to SMH-put profit, only one ("nothing burger") loses. The thesis bet is one path; insurance covers the others (weak Q3 guide, sympathetic decline, macro surprise, NVDA bombs).

**Strategy A composite position into ER:**

| Scenario | SMH put P&L | NVDA call P&L | Net |
|---|---|---|---|
| **Nothing burger** (NVDA $215–235) | -$638 | +$194 (keep) | **-$444** |
| Mild beat ($235–245) | -$638 | +$194 (still OTM) | -$444 |
| Strong beat past $250 | -$638 | $194 - upside lost above $250 | depends, +94% realized on basis |
| NVDA miss → SMH down 3-5% | +$300–800 | +$194 (keep) | +$494–994 |
| NVDA bombs ($200 or lower) | +$1,500+ | +$194 | +$1,694+ |

**Net premium income offsets ~30% of "nothing burger" downside** while preserving full insurance.

## Execution notes for the NVDA call sale

- **Timing**: Mon 5/18 or Tue 5/19 morning, ideally with NVDA showing strength. If NVDA drifts lower pre-ER, the call premium drops fast.
- **Strike**: $250 (May-22). 11% OTM. Even if assigned, realized gain = +94% on $130 basis.
- **Order type**: Limit at mid ($1.94) or slightly worse. NVDA call OI is 62,978 at this strike — deep liquidity, tight fills expected.
- **Don't chase**: If NVDA gaps down pre-ER, just don't sell the call — the premium reflects vol; if vol crushes pre-ER, capture is lost.

## Coming-week catalysts

- **Wed 5/20**: NVDA Q1 FY27 earnings (after close). The binary event.
- **Watch Thursday open**: Did "nothing burger" materialize? If yes — close SMH put if MTM still has meaningful value, let NVDA call expire worthless Friday.
- **Friday 5/22**: NVDA call expiry. Outcome locked.
- **Late next week**: Reassess. If cycle technicals (SMH wRSI, NDX-SMH spread) keep compressing, may want to re-establish broader hedges. If they normalize, scale back.

## Decision triggers for the coming week

| Event | Action |
|---|---|
| NVDA opens Thu 5/21 +5% or more | Close SMH put for residual value (~$100–200 likely); accept loss; NVDA call expires worthless = profit |
| NVDA opens Thu 5/21 flat (±2%) | Let everything ride to Fri 5/22 expiry — both legs likely expire worthless except SMH put might retain $50–200 |
| NVDA opens Thu 5/21 -5% or worse | SMH put gains substantially; consider rolling out to Jul if cycle thesis still in play |
| NVDA opens Thu 5/21 -10% or worse | Big SMH put winner. Close put, take profit, reassess whether cycle is breaking |
| GOOGL crosses $400 on I/O news | Trigger GOOGL Jul-17 $360 put buy (see [hedge plan](2026-05-10-hedge-execution-plan.md) §rationale) |

## What's NOT in this week's plan

- AMD / MU / COHR / GLW direct hedges — all retreated this week, less urgent. Watch only.
- Tier 0 (Fed/CPI) — no major releases flagged for the week. Manual check at Mon open.
- Tier 1–3 news scans — deferred.
