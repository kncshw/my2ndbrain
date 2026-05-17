# NOW Rebound Trade — Plan & Triggers

**Created:** 2026-05-17 (Sun)
**Status:** Ready to execute Mon 5/18 open

## Thesis (one-liner)

Pure SaaS rebound timing trade on the **only candidate from the 5-name basket that qualifies as a true SaaS rebound** (vs MSFT/META = defensive/adjacent). NOW down -54% from 52w high at the cheapest P/S in 5+ years. wRSI 36.7 oversold. Capital rotation from extended semis → beaten-down SaaS expected over 4-6 weeks.

## Position

| | |
|---|---|
| Ticker | NOW |
| Expiry | **June 18, 2026** (32 days) |
| Strike | **$95** (ATM, spot $95.07) |
| Type | Long calls |
| **Contracts** | **2** |
| Mid premium | $6.95 |
| **Total cost** | **$1,390** |
| Position % of portfolio | ~0.5% (small starter) |

**Why ATM not OTM:** Highest delta (~0.55), highest gamma, lowest breakeven ($101.95 = +7.3%). For an oversold-bounce trade, probability-of-profit matters more than convexity-on-tail-scenarios. ATM wins at any realistic rebound level ($105–$115).

## Why June not July

Per-day theta on Jul-17 $100C is cheaper, BUT total absolute cost is higher and timing trade doesn't need 60 days of life. June expiry forces decisive thesis validation in 4 weeks, captures most-likely rebound window, costs less in total premium.

## P/L grid at June 18 expiry

| NOW spot | Total P/L on 2× $95C | Return |
|---|---|---|
| $90 (-5%) | -$1,390 | -100% |
| $95 (flat) | -$1,390 | -100% |
| $100 (+5%) | -$390 | -28% |
| **$101.95 (BE)** | **$0** | **0%** |
| $105 (+10%) | **+$610** | +44% |
| $110 (+15.7%) | **+$1,610** | +116% |
| $115 (+21%) | **+$2,610** | +188% |
| $120 (+26%) | **+$3,610** | +260% |

Target outcome: NOW rebound to $110–115 (50% retrace of recent leg down) = **+1.5x to +2x return**.

## Valuation context (why NOW vs other beaten-down SaaS)

| Metric | NOW today | NOW historic dips | Verdict |
|---|---|---|---|
| TTM P/S | 7.0x | 10.9x–13.9x at 2020/2022/2025 lows | **Cheapest in 5+ yrs** |
| Fwd P/E | 18.9x | 45–60x at prior dips | Extreme compression |
| Rev growth | 21% | 22–32% historically | Decelerating but durable |
| PEG | 0.88 | n/a | Cheap on growth-adjusted basis |

Multiple compression has run dramatically ahead of growth deceleration. The setup is genuinely asymmetric.

## Moat resilience (stress-tested through 5 angles)

1. ✅ AI displacement — NOW is the workflow/audit/integration layer AI agents run THROUGH, not replace
2. ✅ API dependency — network effects work in NOW's favor, partners need NOW more
3. ✅ Pure-play competitors (PagerDuty, SOAR vendors, etc.) — platform consolidation pattern shows NOW winning
4. ✅ Foundation model dependency — optimal position in AI value chain, no need to own model
5. ✅ Infrastructure — own data centers, not vulnerable to hyperscaler squeeze; better margins than peers

Bear case acknowledged: Microsoft as frenemy competitor in adjacent products. Risk vector but not existential.

## Decision triggers

| Event | Action |
|---|---|
| NOW ≥ $108 by week 2 (May 30) | Close 1 contract, lock half the profit, ride the second |
| NOW ≥ $115 anytime | **Full exit** — realistic technical target hit |
| NOW < $90 on weekly close | Exit both — thesis broken, stop the decay bleed |
| **Jun 4 (2 weeks left) and NOW still < $95** | **Hard decision point** — theta accelerates fast from here |
| Jun 11 (1 week left) and NOW < $98 | Close — gamma trap in final week |

## Theta watch — critical dates

| Window | Per-day decay (2 contracts) |
|---|---|
| Now → May 30 | ~$30/day (manageable) |
| May 30 → Jun 11 | ~$50/day (painful if no movement) |
| Jun 11 → Jun 18 | ~$100/day (brutal — decide and exit) |

**Hard rule:** if NOW shows no rebound signal by Jun 4, exit. Don't fight theta.

## Execution notes

- **Order type:** limit at mid ($6.95) or slightly worse. NOW $95C OI is 7,607 — deep liquidity, tight fills expected.
- **Timing:** Mon 5/18 morning. NOW IV at 59.8% is elevated (reflects the panic that created the buying opportunity); fine to enter, but don't chase if NOW gaps up at open.
- **Skip the call** if NOW gaps up >3% at open Mon — wait for a re-test of $95 or place a lower limit.

## What this trade is NOT

- Not a long-term hold (calls expire)
- Not a fundamental investment in NOW the company (that would be stock, not 32-day calls)
- Not part of the broader hedge stack (separate from SMH put, INTC, GOOGL plans)
- Not a SaaS-basket trade (MSFT/META dropped — they're defensive, not rebound plays)

## What this trade IS

A focused, time-bounded, thesis-driven bet that:
- A genuinely beaten-down SaaS leader (-54% from highs)
- At the cheapest valuation in 5+ years vs own history
- With a structurally defensible moat against AI displacement
- Will mean-revert at least partially within ~4 weeks
- Generating a 1.5x–2x return on a 50% retrace

If the thesis is wrong, max loss = $1,390 (~0.5% of total portfolio).

## Related notes

- [Week-ahead context (5/17)](2026-05-17-week-ahead.md)
- [Original hedge plan (5/10)](2026-05-10-hedge-execution-plan.md)
- Finance methodology: `../notes/finance/research-methodology-finance.md`
