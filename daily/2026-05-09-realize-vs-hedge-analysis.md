# Realize vs. Hedge Analysis — Concentrated AI/Semi/Optical Gains

**Date:** 2026-05-09 (Saturday — markets closed; prices reflect Fri 5/8 close or last available)
**Scope:** GOOGL, INTC, AMD, MU, COHR, GLW
**Out of scope (per user):** NVDA, TSM, AVGO — comfortable holding

> **Disclaimer:** This is structured research, not financial advice. Tax treatment depends on your account, lots, and jurisdiction. Run option strategies past your broker / tax advisor before placing them.

---

## TL;DR

| Ticker | Last      | YTD / Recent Move               | Analyst Consensus PT          | Price vs. PT                 | View                             |
| ------ | --------- | ------------------------------- | ----------------------------- | ---------------------------- | -------------------------------- |
| GOOGL  | ~$400.80  | At ATH; JPM top pick            | ~$403–408 (high $515)         | At consensus                 | **Hold / mild covered call**     |
| INTC   | ~$109     | +170% YTD, +107% in past month  | $79.05                        | **38% above**                | **Trim aggressively / collar**   |
| AMD    | ~$408–421 | Fwd P/E ~47–62; GF Value $214   | (mixed)                       | **~97% above GF Value**      | **Trim / collar**                |
| MU     | ~$666     | +120% YTD; ATH 5/6              | $551                          | **~21% above**               | **Trim / collar / partial put**  |
| COHR   | ~$335     | At/near ATH post-Q3             | $330 (MS) – $425 (Rosenblatt) | At low end of upgraded range | **Hold w/ collar**               |
| GLW    | ~$186     | +18% in 5 days post-Nvidia deal | (re-rating in progress)       | News-driven spike            | **Trim partial / trailing stop** |

**The signal that matters:** INTC, AMD, and MU are trading meaningfully above what analysts on average think they're worth. That's not a guarantee of a top, but it removes the "the Street will catch up" tailwind that justified the rally so far. Forward returns from here depend on continued upside *surprises*, not just delivery.

---

## Per-Name Detail

### GOOGL — ~$400.80
- **Setup:** All-time high. JPM top pick at $460, Mizuho $460, Citizens $515. Consensus ~$403–408 (you're roughly there).
- **Risk profile:** Strongest fundamental story of the group (search resilience + Cloud + Gemini + YouTube). Lowest standalone valuation risk among your concerns.
- **Why I wouldn't rush to sell:** Multiple is reasonable for the growth profile; institutional flow still constructive.
- **What I'd do:** Run **covered calls** monthly on a portion (sell upside above $440–460) to monetize IV without giving up the share. If gain is short-term, defer realizing if possible.

### INTC — ~$109 *(your top concern, deservedly)*
- **Setup:** +170% YTD, +107% in the past month. Apple/Tesla/Nvidia/Google catalysts are real but largely priced in.
- **Red flag:** Consensus PT **$79** vs. spot ~$109 — you are **38% above** what the analyst community thinks the stock is worth on average. Rating mix skews Hold, not Buy.
- **History rhymes:** Stocks that rip 100%+ in a month on news that's already public almost always retrace 20–40% before settling — even when the long-term thesis is intact.
- **What I'd do:**
  1. **Trim 30–50% of the position now** — lock the windfall.
  2. **Collar the rest:** sell a 3-month $130 call, buy a 3-month $90 put. Funds itself or close to. You give up upside above $130 (you've already been gifted enough) and floor your downside at $90.
  3. If short-term gain — model the after-tax outcome of selling now vs. holding to LT. The answer is rarely "hold for tax reasons alone" when the stock is 38% above PT.

### AMD — ~$408–421
- **Setup:** Forward P/E in the 47–62 range. GuruFocus GF Value $214 — stock trades **~97% above** that estimate. Trailing P/E 154.
- **Bull case alive?** Yes — MI series ramp + datacenter share gains. But the price now requires that to work *and* margins to expand.
- **What I'd do:**
  - **Trim 25–40%** to right-size if it's grown into an outsized weight.
  - **Cashless collar** on the remainder (sell $475–500 call, buy $360–380 put, 3–6 months). AMD options are liquid; bid/ask is reasonable.
  - Avoid naked puts/short here — momentum names like AMD can grind higher longer than valuation suggests.

### MU — ~$666
- **Setup:** ATH 5/6/2026. HBM sold out through CY2026. Q1 GM 56% → Q2 guided 68%. Average PT $551 (you're ~21% above).
- **Tension:** Memory is *cyclical*. The bull case ("HBM TAM to $100B by 2028") is genuine, but memory cycles end with a thud — usually before the consensus narrative shifts. The setup looks like late-cycle euphoria.
- **What I'd do:**
  - **Trim 25–35%** — memory cycles reward those who sell into strength.
  - Buy a **6-month protective put** at $560 (~15% OTM) on the rest. Pricier than a collar but pure downside insurance with full upside retained.
  - Or **put spread** ($560/$450) to cheapen the hedge if you're worried about a 15–25% pullback but not a full cycle break.

### COHR — ~$335
- **Setup:** Post-Q3 earnings (5/6) with $1.41 EPS, $1.81B revenue. Targets raised: Rosenblatt $425, TD Cowen $395, **Morgan Stanley only $330** — interesting split.
- **Read:** Networking / optical transceiver story is the real AI infra picks-and-shovels thesis. Less crowded than NVDA but the move has been substantial.
- **What I'd do:**
  - **Hold core** — best long-term optical pure-play among your concerns.
  - **Collar** if you want to lock in: sell $400 call / buy $290 put, 3–6 months.
  - Or sell ~20% to fund the put leg outright.

### GLW — ~$186
- **Setup:** +18% 5-day on Nvidia partnership announcement (10x optical capacity expansion in US). Market cap +$25B in 5 sessions.
- **Risk:** This is a **news-driven spike**. GLW's display/specialty materials businesses don't justify the move standalone — the thesis is "AI optical re-rating." If AI capex narrative wobbles, this gives back fast because the float isn't used to this kind of vol.
- **What I'd do:**
  - **Trim 30–40% into the spike** — banked windfall.
  - **Trailing stop ~10–12% off the high** on the rest (or a $165 stop-limit). GLW options are thinner; collars are workable but the bid/ask hurts.

---

## Strategy Menu (when to use which)

| Strategy | When it fits | Cost | Tax effect |
|---|---|---|---|
| **Outright sell (full)** | Conviction the top is in; want cash | None | Triggers cap gain — ST vs. LT matters |
| **Trim partial (25–50%)** | Most common right answer for big runs | None | Partial gain realized |
| **Covered call** | Mildly bullish; want yield | Caps upside | Premium taxed; share assignment may force sale |
| **Protective put** | Want full downside floor, retain upside | Premium (1.5–4% / 3mo at the money-ish) | Resets holding period only if "married put" rules apply — check |
| **Collar (sell call, buy put)** | Want to bound risk both ways cheaply | Often near-zero | Same as above; "constructive sale" rules can apply if collar is too tight — keep ≥15% spread |
| **Put spread** | Hedge a moderate drawdown cheaply | Cheaper than a put, but caps the hedge | Standard option tax |
| **Trailing stop** | Don't want to babysit; thin options | None | Realizes when triggered |
| **Tax-loss harvest offset** | If you have *other* losers to pair with | None additional | Offsets gain — check 30-day wash sale |

### A note on "constructive sale" (IRS §1259)
A collar that is too tight (very narrow band between strikes) can be deemed a constructive sale and trigger immediate cap gains. Keep the put strike well below spot and the call strike well above. Rule of thumb: ≥10–15% room on each side, and don't structure it specifically to lock in price.

---

## A Suggested Sequence (if I were running this book)

1. **This weekend** — decide tax bracket impact. Pull cost basis and lot ages for each name. The ST/LT split changes everything.
2. **Mon 5/11 AM** — execute trims first (cleanest action): INTC, AMD, MU, GLW. Don't try to time the open; use a VWAP order or split into three slices over the day.
3. **Mon–Tue** — set up collars / puts on remaining INTC, AMD, MU, COHR. Use the **3–6 month** tenor (avoids weekly noise; gives time for a thesis to play out).
4. **Standing orders** — trailing stops for GLW; consider on the COHR remainder if you don't want to manage options.
5. **GOOGL** — covered call program, monthly rolls. Lowest urgency.

---

## What would change the call

- **INTC pulls back 15%+ on profit-taking before earnings** → may not need to trim further, just hedge.
- **MU guides Q3 GM above 70%** → cycle thesis extends; loosen MU hedge.
- **AI capex commentary turns cautious from MSFT/META/GOOG/AMZN on next earnings** → tighten everything; this is the dominant macro signal for all six names.
- **VIX spikes above 25** → puts get expensive; pivot to outright trims and trailing stops instead of buying protection.

---

## Sources

- GOOGL: [MarketBeat](https://www.marketbeat.com/stocks/NASDAQ/GOOGL/forecast/), [CoinCentral on JPM $460 PT](https://coincentral.com/alphabet-googl-stock-hits-all-time-high-as-jp-morgan-sets-460-price-target/), [stockanalysis.com](https://stockanalysis.com/stocks/googl/forecast/)
- INTC: [24/7 Wall St — quintupled from lows](https://247wallst.com/investing/2026/05/04/intel-stock-has-quintupled-from-lows-is-the-easy-money-already-gone/), [24/7 Wall St — sell in May?](https://247wallst.com/investing/2026/05/08/intel-just-ripped-116-in-a-month-is-it-time-to-sell-in-may-and-go-away/), [Motley Fool — record highs](https://www.fool.com/investing/2026/05/05/why-intel-stock-skyrocketed-to-record-highs-today/), [Yahoo — Trump $30B](https://finance.yahoo.com/markets/stocks/articles/intel-stock-190-2026-trump-131501491.html)
- AMD: [GuruFocus Forward P/E](https://www.gurufocus.com/term/forward-pe-ratio/AMD), [stockanalysis.com](https://stockanalysis.com/stocks/amd/statistics/), [FinanceCharts P/E](https://www.financecharts.com/stocks/AMD/value/pe-ratio)
- MU: [io-fund — HBM leader 2026](https://io-fund.com/ai-stocks/micron-stock-up-100-hbm-leader-2026-plan), [Seeking Alpha bull case](https://seekingalpha.com/article/4899989-micron-technology-i-think-there-is-a-clear-path-to-over-1500), [TradingKey — super-cycle](https://www.tradingkey.com/analysis/stocks/us-stocks/261867618-us-micron-stock-forecast-ai-memory-semiconductor-hbm-nvda-tradingkey)
- COHR: [Yahoo Finance](https://finance.yahoo.com/quote/COHR/), [QuiverQuant Q3 earnings](https://www.quiverquant.com/news/COHERENT+($COHR)+Releases+Q3+2026+Earnings), [MarketBeat](https://www.marketbeat.com/stocks/NYSE/COHR/forecast/)
- GLW: [CNBC — Nvidia/Corning partnership](https://www.cnbc.com/2026/05/07/nvidia-ceo-ai-partnership-corning-revitalize-american-manufacturing.html), [Trefis — 5-day streak](https://www.trefis.com/articles/598875/corning-stock-5-day-winning-spree-stock-climbs-18/2026-05-09), [Barchart — major Nvidia deal](https://www.barchart.com/story/news/1776631/corning-stock-is-surging-on-a-major-nvidia-deal-ai-is-not-just-a-technology-story-it-is-a-manufacturing-story)
