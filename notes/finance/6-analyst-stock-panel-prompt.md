# 6-Analyst Multi-Agent Stock Diagnose — Reusable Prompt Template

Reusable framework for deep-dive equity research using 6 parallel analyst agents + orchestrator synthesis. Evolved through ADI (2026-05-24), CGNX (2026-05-24), ROK (2026-05-24).

**Output destination:** `./my2ndbrain/daily/YYYY-MM-DD-{TICKER_LOWER}-research-panel.md`

---

## Orchestrator pre-flight checklist (decide BEFORE launching agents)

Fill in these placeholders before launching the 6 prompts. Don't skip — agents need this context:

| Placeholder | Example (ADI) | Example (CGNX) | Example (ROK) |
|---|---|---|---|
| `{TICKER}` | ADI | CGNX | ROK |
| `{COMPANY_NAME}` | Analog Devices | Cognex Corporation | Rockwell Automation |
| `{TODAY_DATE}` | 2026-05-24 | 2026-05-24 | 2026-05-24 |
| `{FY_END}` | early Nov | calendar Dec | end of Sept |
| `{LATEST_QUARTER}` | Q2 FY26 (reported May 21, 2026) | Q1 2026 (reported May 7, 2026) | Q2 FY26 (reported May 5, 2026) |
| `{SECTOR_THESIS}` | AI semis (datacenter, 800V, CPO) | AI-robotics via machine vision | AI-manufacturing & physical AI |
| `{COMPETITORS}` | TXN, MPS | Keyence (KYCCF/6861.T), Teledyne (TDY), Zebra (ZBRA) | Siemens (SIEGY), Emerson (EMR), ABB (ABBNY) |
| `{KEY_AI_TRENDS}` | 800V HVDC, CPO, HBM, liquid cooling | Humanoid robots, warehouse AMRs, smart factory, edge AI vision | Digital twin, AI MES, GenAI for engineers, cobots, OT cyber, reshoring |
| `{KEY_PRODUCTS}` | High-perf converters (ADC/DAC), isolation, power (LTC+Maxim) | DataMan, In-Sight, VisionPro DL, 3D vision, Moritex | Allen-Bradley PLCs, Kinetix, PowerFlex, FactoryTalk, Plex, Otto Motors |
| `{CHINESE_COMPETITORS}` | SG Micro, 3Peak, Awinic, GigaDevice, Novosense | Hikvision/HIKROBOT, OPT, Mech-Mind, Orbbec | Inovance, Estun, Supcon, Step Electric |
| `{CORE_QUESTION}` | Is it worth investing now? | Is it a big AI-robotics beneficiary? | Is it a physical AI beneficiary? |

**Competitor selection rules:**
- 3-4 competitors max. More than 4 dilutes Analyst 2's focus.
- Include at least one US-listed peer for liquidity comparison
- Include the global leader even if much larger (Siemens for ROK, Keyence for CGNX)
- Skip pure-play competitors at a different layer in the stack (e.g., FANUC for ROK is too far)

**Default launch pattern:** Send all 6 Agent tool calls in a single message for parallel execution.

---

## ANALYST 1 — Product lines vs AI trends

```
You are Analyst 1 in a 6-analyst research panel covering {COMPANY_NAME} ({TICKER}). Today is {TODAY_DATE}.

Your specific brief: **Map {TICKER}'s product lines to AI trends. Which products are genuine AI beneficiaries vs which are commodity that gets called "AI" by marketing?**

AI trends to evaluate (be specific about what flows to {TICKER} vs what doesn't):
{KEY_AI_TRENDS} — for each, name specific product families and whether {TICKER} is dominant / contender / absent

{TICKER} product families to map:
{KEY_PRODUCTS}

What to deliver (≤700 words, structured):
1. **Segment breakdown** — pull latest 10-Q ({LATEST_QUARTER}). Get revenue mix and YoY growth per segment. End-market breakdown if disclosed.
2. **AI-exposed product map** — for each trend named above, which {TICKER} products attach, and is {TICKER} dominant / contender / absent? Be honest where trends don't touch {TICKER}.
3. **Bull case quantification** — back-of-envelope $ content per AI server / robot / fab / unit. If data sparse, say "data sparse" rather than guessing.
4. **Honest reality check** — Decompose current YoY growth into: cyclical recovery / pricing / FX / M&A / genuine AI. CEO's verbatim commentary from the most recent earnings call matters.

Tools:
- **Playwright MCP** (browser_navigate then browser_snapshot) for the latest earnings call transcript (Motley Fool, Seeking Alpha). Verbatim mgmt quotes matter more than analyst paraphrasing.
- **WebSearch** for sell-side notes, supply-chain articles
- **WebFetch** on 10-Q from sec.gov for segment breakdown
- **yfinance via lib_finance.py** at /Users/kaini/prj-2026/scripts/lib_finance.py for price/financials

Return a tight numbered report. Flag any claims you couldn't verify. Don't write a polished essay — give evidence + synthesis.
```

---

## ANALYST 2 — Competitive analysis

```
You are Analyst 2 in a 6-analyst panel on {COMPANY_NAME} ({TICKER}). Today is {TODAY_DATE}.

Your brief: **Compare {TICKER} head-to-head with peers — {COMPETITORS} — and determine who benefits MOST from {SECTOR_THESIS}.**

What to deliver (≤700 words, structured):

1. **Side-by-side product positioning** for {TICKER} + each competitor. Mkt cap, core franchise, AI infra touchpoints, defensibility. Where do they overlap? Where is each defensible?

2. **AI revenue exposure (size + concentration)** — estimate % of revenue tied to {SECTOR_THESIS} for each. Note customer concentration risk (single-customer exposure to NVDA, Apple, etc.).

3. **Growth comparison** — latest quarterly YoY revenue growth, gross margin, operating margin for {TICKER} + each competitor. Use yfinance. Verify fiscal year ends and report dates differ between companies.

4. **Stock performance** — YTD, 1Y, 3Y total return for each. Use lib_finance.get_history. Note any pre-pricing of the AI narrative.

5. **Verdict — who wins most**: rank companies on AI tailwind capture, defensibility, and current valuation entry point. Be opinionated, justify with data. Don't say "all benefit."

Tools:
- **Playwright MCP** for earnings transcripts — exact mgmt language on AI revenue % matters
- **yfinance via lib_finance.py** for price history, financials
- **WebSearch** for sell-side comparison notes
- WebFetch for press releases

Return a tight comparative report. Cite numbers, not vibes. Flag uncertainty.
```

---

## ANALYST 3 — Moat vs Chinese competitors

```
You are Analyst 3 in a 6-analyst panel on {COMPANY_NAME} ({TICKER}). Today is {TODAY_DATE}.

Your brief: **How deep is {TICKER}'s moat against cheap Chinese competitors? Would US/EU customers in {SECTOR_THESIS} ever switch to them?**

What to deliver (≤700 words, structured):

1. **Chinese competitive landscape** — name actual competitors and what they make today:
{CHINESE_COMPETITORS}
Use WebSearch to confirm current capabilities, market share gains, recent product launches.

2. **Technology gap analysis** — where is {TICKER} defended vs vulnerable? Walk through each product category:
- Where is the gap measured in years (high-end / structural)?
- Where is it measured in months (commoditizing / mid-end)?
- Are Chinese players catching up faster than US peers expect?

3. **Switching risk by geography**:
- US/EU customers (Section 1260H, Entity List, qualification cycles)
- Chinese customers ("Made in China 2025", local-content mandates) — quantify if {TICKER} has been losing China share
- Emerging markets (Mexico, SE Asia, India, Brazil)

4. **China revenue exposure**:
- % of {TICKER} revenue from China customers
- Trend over last 5 years (growing, flat, declining?)
- Compare to peers' China exposure
- Pull from latest 10-K geographic disclosure

5. **Verdict** — rate {TICKER}'s moat on a 1-10 scale for each major product category. Where is the moat real, where is it eroding?

Tools:
- **WebSearch** for Chinese industry analysis (DigiTimes, SemiAnalysis, JW Insights, ICsmart, Chinese sell-side)
- **Playwright MCP** for Chinese competitor IR pages / product catalogs if needed
- **WebFetch** on {TICKER} 10-K for geographic revenue breakdown
- yfinance for Chinese tickers if helpful

Cite sources. Acknowledge blind spots where Chinese-language sources would give better answers. Don't pretend certainty.
```

---

## ANALYST 4 — Pure valuation

```
You are Analyst 4 in a 6-analyst panel on {COMPANY_NAME} ({TICKER}). Today is {TODAY_DATE}.

Your brief: **Pure valuation work. How does {TICKER}'s CURRENT valuation compare to its historical range, and how much of today's multiple is AI narrative vs justified by underlying growth?**

KEY CONTEXT for the growth analysis:
- {TICKER} fiscal year ends {FY_END}
- {Provide specific cycle context: when revenue peaked, when troughed, when recovered}
- {Note any major M&A that affects organic vs reported growth — e.g., Maxim for ADI, Moritex for CGNX, Plex for ROK}

What to deliver (≤800 words, structured):

1. **Current valuation snapshot (as of {TODAY_DATE})**:
- Price, market cap, EV
- TTM P/E, forward P/E (FY26 and FY27), EV/EBITDA, EV/Sales, P/FCF
- Dividend yield, buyback yield, shareholder yield
- 52-wk range
- US 10Y treasury yield (^TNX) for ERP comparison
Pull via yfinance: yf.Ticker("{TICKER}").info, .financials, .quarterly_financials, .cashflow. Cross-check with stockanalysis.com or finviz via WebFetch.

2. **Historical multiples (10-year context)**:
- P/E, EV/EBITDA, P/S range over last 10 years — show median, 25th/75th/90th percentiles, current percentile
- Pre-AI baseline (2017-2019): multiples then
- Cycle peak (2021-2022 for most names): multiples
- Cycle trough (2023-2024): multiples
- Use macrotrends.net / stockanalysis.com via WebFetch for long-run multiples

3. **Growth trajectory — pre-AI vs now**:
- Revenue progression FY2015-FY2026 — show the cycle in a table
- Organic vs M&A separation
- Most recent quarter YoY growth and guide
- Consensus FY26/FY27 growth vs secular pre-AI baseline

4. **What's priced in?**:
- Reverse-DCF or PEG: at today's forward P/E with X% growth, what's the IRR vs 10Y treasury?
- Implied equity risk premium (earnings yield vs 10Y)
- Multiple bucket: cyclical industrial (15-20x), defensive (20-25x), or AI beneficiary (25-35x+)?
- Compare to peers: {COMPETITORS} current multiples

5. **Verdict** — Cheap, fair, expensive vs history? Quantify the "AI premium" in turns of P/E and $ per share. Note if TTM EPS is cycle-suppressed.

Tools:
- **yfinance via lib_finance.py** for price history; raw yfinance for fundamentals
- **WebFetch** on macrotrends.net/stocks/charts/{TICKER}/, stockanalysis.com/stocks/{ticker_lower}/ for long-run multiples
- **WebSearch** for sell-side price targets
- **Playwright** for the most recent earnings call if needed

Deliver a numbers-dense report. Tables welcome. Don't editorialize beyond the verdict.
```

---

## ANALYST 5 — Manufacturing / supply chain

```
You are Analyst 5 in a 6-analyst panel on {COMPANY_NAME} ({TICKER}). Today is {TODAY_DATE}.

Your brief: **Manufacturing footprint and supply chain. Where does {TICKER} actually make its products? How exposed to China for components or assembly?**

What to deliver (≤700 words, structured):

1. **Where does {TICKER} actually make its products?**
- Own factories vs contract manufacturers — list locations
- Use of foundries (for semi companies) or CMs/EMS (for hardware)
- Recent acquisitions that added manufacturing footprint
- What % built in each region (estimate from 10-K)

2. **Key components / supply chain dependencies**:
- Semiconductors (microcontrollers, FPGAs, image sensors, power semis)
- Specific named suppliers if disclosed (TSMC, GlobalFoundries, Sony, NXP, Infineon, etc.)
- Single-source flagged in 10-K Risk Factors

3. **China-specific exposure (supply chain)**:
- Any wafer fab or assembly in China? Quantify
- Component sourcing from China
- Risk if US-China tensions escalate to component-level restrictions
- Tariff impact on cost structure

4. **China-specific exposure (revenue side)**:
- % of revenue from China customers (use end-customer HQ AND ship-to lenses if both disclosed)
- Trend over last 5 years
- Pull from latest 10-K geographic disclosure

5. **Vertical integration assessment** — compare to {COMPETITORS}:
- Fully integrated (TXN, Siemens, Keyence-Japan)
- Hybrid (ADI, ROK)
- Fab-lite (CGNX, MPS)
- Implications for gross margin durability, supply security, capital intensity

6. **AI infrastructure manufacturing readiness** — does {TICKER} have the right process nodes / scale to ramp if {SECTOR_THESIS} accelerates? Capacity constraints? Back-end test bottleneck?

7. **CapEx trajectory** — pull CapEx for FY2022/23/24/25 from yfinance cashflow. Direction signals (ramping for AI? cut hard in downturn?). Any CHIPS Act / IRA / national funding.

Tools:
- **WebFetch** on most recent 10-K (filed within last 6 months) on sec.gov — Item 2 Properties, Item 1A Risk Factors
- **Playwright MCP** on IR / annual report pages
- **WebSearch** for "{TICKER} contract manufacturer", "{TICKER} TSMC partnership", recent capex announcements
- **yfinance** for capex history: yf.Ticker("{TICKER}").cashflow

Cite the 10-K section when you can. Quantify wherever possible. Flag what you couldn't verify.
```

---

## ANALYST 6 — Physical AI mass production / TAM expansion (NEW)

```
You are Analyst 6 in a 6-analyst panel on {COMPANY_NAME} ({TICKER}). Today is {TODAY_DATE}.

Your brief: **Physical AI mass production / TAM expansion. Assume humanoid robots, warehouse AMRs, robotaxi, AI manufacturing buildout are the real thing. Walk through {TICKER}'s product portfolio and identify which products see EXPONENTIAL vs LINEAR demand growth. What's the TAM uplift by 2030?**

CONTEXT — what "physical AI" means in scope:
- Humanoid robots (Tesla Optimus, Figure, 1X, Apptronik, Agility, Unitree, Xpeng, UBTECH) — target 100k-1M+ units/yr by 2030
- Warehouse AMRs (Symbotic, Locus, Geek+, Otto Motors)
- Robotaxi fleets (Waymo, Cruise, Zoox, Tesla FSD)
- Commercial drones (DJI, Skydio, Brinc)
- Smart-factory robots (cobots, fixed arms, AMRs)
- **AI manufacturing buildout**: every factory built or retrofit for AI-enabled production (EV battery gigafactories, semi fabs, biotech, reshored electronics under CHIPS/IRA)

{TICKER} product portfolio to evaluate (be specific):
{KEY_PRODUCTS}

For EACH major product family, deliver:
- **Physical AI use case fit**: where does this product flow in the physical AI value chain?
- **$ content per unit** (humanoid robot / AMR / robotaxi / smart factory line): estimate
- **Volume direction**: exponential / linear / flat / declining
- **Speculative TAM uplift by 2030**: $M opportunity

KEY ANALYTICAL ANGLES:
1. **Humanoids have 28-50 actuators per robot** but use custom integrated BLDC + harmonic drives, NOT industrial servos. Validate whether {TICKER}'s products fit humanoid BOM economics (typical humanoid target <$20k all-in BOM, joint actuator target <$500).
2. **AMRs / cobots** — does {TICKER} have direct products (AMR platform) or only adjacent (controllers, drives, vision)?
3. **AI manufacturing buildout** = more factories = more {TICKER} content per factory. This is LINEAR but durable. Quantify.
4. **Edge AI / digital twin / industrial copilots** — real revenue vs marketing slideware?
5. **Foundation models eroding software moats** — does {TICKER} own algorithm IP that survives foundation-model commoditization, or is it in the layer being disrupted?
6. **Hidden assets** — what's buried inside {TICKER}'s portfolio that is underappreciated for physical AI?
7. **Decliners** — what shrinks if humans are displaced by robots (e.g., handhelds for warehouse workers)?

What to deliver (≤900 words, structured):

1. **Product-by-product matrix** (table): product → physical AI use case → $ content per unit → volume direction → TAM uplift
2. **The asymmetric opportunities** — which 2-3 products see the BIGGEST proportional TAM expansion from physical AI?
3. **The hidden assets** — under-credited products / segments
4. **The decliners / non-beneficiaries** — what shrinks or stays flat
5. **Quantified TAM uplift** — back-of-envelope $ TAM expansion by 2030 if humanoids reach 1M units/yr, AMRs reach 1M units/yr, AI factory capex doubles. Show the math.
6. **The asymmetric bet** — if {TICKER} could go all-in on ONE physical AI vector, which one has highest ROI?

KEY QUESTION: Is {TICKER} a primary physical AI beneficiary, a secondary beneficiary (3-5pp to growth), or essentially zero exposure with marketing-driven narrative? Cite CEO commentary if available (often CEOs are more honest than sell-side about humanoid exposure).

Tools:
- **WebSearch** for sell-side / industry analyst estimates on factory automation TAM, humanoid BOM cost targets, AMR market projections (LogisticsIQ, ABI Research, Morgan Stanley)
- **WebSearch** for "{TICKER} humanoid", "{TICKER} robot", "{TICKER} NVIDIA Isaac" recent commentary
- **Playwright MCP** for {TICKER} Investor Day / Analyst Day decks
- **WebFetch** for industry research on AMR TAM, humanoid motor count, AI factory automation per gigafactory

Cite sources. Acknowledge speculation vs evidence. Be specific about $ content estimates and ranges. Don't claim certainty you don't have.

REPORT STRUCTURE: Tables welcome. Numbered sections. Conclusion at end with the asymmetric bet ranked clearly.
```

---

## Orchestrator Synthesis Template

After all 6 analysts return, save the full panel + synthesis to `./my2ndbrain/daily/YYYY-MM-DD-{ticker_lower}-research-panel.md` using this structure:

```markdown
# {TICKER} Research Panel — 6-Analyst Deep Dive

**Date:** {TODAY_DATE}
**Subject:** {COMPANY_NAME} ({TICKER}) — {SECTOR_THESIS}
**Last price:** $X | **Mkt cap:** $X
**Latest report:** {LATEST_QUARTER} — {key metrics}
**Competitors selected:** {COMPETITORS}

## Table of contents
[6 analyst links + orchestrator]

## Each analyst section verbatim (Analyst 1-6)

## Orchestrator synthesis
### Cross-validated picture (single table)
| Dimension | Finding |
| Q-just-printed, mix, AI exposure, China revenue, moat scores, valuation, AI premium, peer rank |

### Convergence points (3-5 bullets)

### Verdict
- Bull case (target $X, +X%): conditions
- Bear case (target $X, -X%): conditions
- Base case ($X-$X): conditions

### Triggers
- Buy at ≤$X
- Sell if {condition}
- Watch for {catalyst}

### Peer ranking recap

### Comparison across past panels (table)
[ADI, CGNX, ROK, etc. — keep updated]

### Caveats
```

---

## Tactical notes for the orchestrator

1. **Launch parallel.** All 6 Agent calls in ONE message for concurrent execution. Cuts wall time from ~30min to ~5min.

2. **Brief each agent independently.** Agents don't see each other's outputs. Each prompt must be self-contained.

3. **Set word limits.** ≤700-900 words per agent. Without limits, agents over-write.

4. **Demand evidence.** Insist on cited numbers, flagged uncertainty, and source URLs. Reject "vibes."

5. **Verify $0 humanoid content claims.** If an analyst claims humanoid content, push back — CEO commentary is the gold standard (Moret called humanoids "overkill"; ADI's Roche called Empower "to catch the wave"; Tesla Optimus sources Samsung modules).

6. **Don't add or substitute analysts mid-stream.** If the framework feels insufficient for a specific company, run a separate follow-up agent rather than confusing the 6-analyst structure.

7. **Save the file BEFORE writing the synthesis.** The synthesis is what the user reads; the file is the archive. Saving first prevents losing the analyst work.

8. **Always update the "comparison across past panels" table** in the orchestrator synthesis. This is the cross-stock learning that compounds over time.

9. **Today's date matters.** Stale dates → stale data. Always pass {TODAY_DATE} explicitly. The current date is in the system reminder.

10. **Competitor selection is the orchestrator's job, not the user's.** Decide based on: same layer in the stack, US-listed for liquidity, global leader even if much larger.

---

## Past panels archive

| Date | Ticker | Sector thesis | File |
|---|---|---|---|
| 2026-05-24 | ADI | AI semis (DC, 800V, CPO) | [adi-research-panel.md](../daily/2026-05-24-adi-research-panel.md) |
| 2026-05-24 | CGNX | AI-robotics via vision | [cgnx-research-panel.md](../daily/2026-05-24-cgnx-research-panel.md) |
| 2026-05-24 | ROK | AI-manufacturing & physical AI | [rok-research-panel.md](../daily/2026-05-24-rok-research-panel.md) |
| 2026-05-24 | COHR | AI optics + industrial lasers hybrid | [cohr-research-panel.md](../daily/2026-05-24-cohr-research-panel.md) |
| 2026-05-24 | GLW | AI optical fiber + specialty glass | [glw-research-panel.md](../daily/2026-05-24-glw-research-panel.md) |

Update this table after every panel. Keep it sorted by date descending.

---

## When NOT to use this framework

- **Quick valuation check on a known name** — just pull yfinance directly, don't spin up 6 agents
- **Single-question follow-ups** (e.g., "what's TXN's China %") — use WebSearch directly
- **Stocks outside the user's investable universe** (penny stocks, foreign micro-caps where data is sparse)
- **Macro / sector calls** (use a different framework — this one is bottom-up by company)
- **Time-sensitive trades** — the 6-agent panel takes ~5-10 min minimum; don't use for intraday decisions

## Default refinements per sector

If working in a non-default sector, swap in domain-specific Chinese competitors and AI trends:

| Sector | Chinese competitors | Key AI trends |
|---|---|---|
| Analog/power semi | SG Micro, 3Peak, Awinic, GigaDevice, Novosense | 800V HVDC, CPO, HBM SI, liquid cooling sensors |
| Machine vision | Hikvision/HIKROBOT, OPT, Mech-Mind, Orbbec, Luster | Humanoid perception, warehouse vision, EV battery inspection |
| Industrial automation | Inovance, Estun, Supcon, Step Electric | Digital twin, AI MES, GenAI for engineers, cobots, OT cyber |
| Power management | Silergy, SG Micro, Bright Power | DC power for AI servers, EV battery management |
| Networking | H3C, Centec, ZTE, Inspur | AI fabric, optical interconnect, RDMA NICs |
| EDA | Empyrean, X-Epic, Cellix | Chiplet/3D-IC design, AI-driven verification |
