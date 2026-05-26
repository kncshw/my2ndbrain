# ROK Research Panel — 6-Analyst Deep Dive (with Physical AI TAM analyst)

**Date:** 2026-05-24
**Subject:** Rockwell Automation (ROK)
**Last price:** $452.29 | **Market cap:** $50.3B
**Latest report:** Q2 FY26 (May 5, 2026) — $2.24B rev, +12% reported / **+9% organic**, adj EPS $3.30 (+30%)
**Competitors selected:** Siemens (SIEGY), Emerson (EMR), ABB (ABBNY)

---

## Table of contents

1. [Analyst 1 — Product-to-AI mapping](#analyst-1)
2. [Analyst 2 — ROK vs SIEGY/EMR/ABB](#analyst-2)
3. [Analyst 3 — Moat vs Chinese (Inovance et al.)](#analyst-3)
4. [Analyst 4 — Pure valuation](#analyst-4)
5. [Analyst 5 — Manufacturing / supply chain](#analyst-5)
6. [Analyst 6 — Physical AI mass production TAM (NEW)](#analyst-6)
7. [Orchestrator synthesis](#orchestrator)

---

<a id="analyst-1"></a>
# Analyst 1 — ROK Product-to-AI Mapping

## Q2 FY26 Segment Breakdown (Mar-Q, reported 5/5/26)

| Segment | Q2 Rev | YoY rep | YoY organic | Seg margin |
|---|---|---|---|---|
| Intelligent Devices | $1,008M | +13% | +9% | 20.9% (+320bp) |
| Software & Control | $684M | +20% | **+17%** | **34.9% (+480bp)** |
| Lifecycle Services | $547M | +2% | –1% | 14.6% (flat) |
| **Total** | **$2,239M** | **+12%** | **+9%** | 22.5% (+350bp) |

**End-market color (Moret, Q2 FY26):** Discrete +mid-teens; auto +mid-teens; semi +high-teens; **e-comm/warehouse +>30%**; **data center sales >2x YoY** (still "low single digits" of total); Hybrid +HSD; F&B +HSD; life sciences +LSD; Process +MSD; Logix +20%; ARR +6%. **Sensia JV dissolved April 1, 2026** — ~$100M FY26 revenue impact, EPS-neutral. FY26 guide raised to organic +5–9%, adj EPS $12.80 mid.

## AI-Trend → Product Map

| AI trend | ROK product | Position | Reality |
|---|---|---|---|
| Digital twin / Omniverse | **Emulate3D** + NVIDIA Omniverse (Factory Test debuted GTC 2025) | Contender | Real product; tiny revenue, not disclosed; not mentioned on Q2 call |
| AI-driven MES | **FactoryTalk PharmaSuite, Plex, ProductionCentre, FT Optix** | Dominant in pharma; contender vs SAP/Siemens | Genuine; Plex is profitable per Moret |
| AI quality / vision | Relies on Cognex/Keyence partners | **Mostly absent** | Marketing slideware |
| GenAI for engineers | **FactoryTalk Design Studio Copilot** (Azure OpenAI, GA Jan 2025) | Contender vs Siemens Industrial Copilot | Real; **zero disclosed adoption metrics** |
| OT cybersecurity | **Verve Industrial** (acq Oct 2023) + Lifecycle Services | Contender (Claroty/Dragos lead) | >$100M run-rate; recurring |
| Cobots / safe automation | **GuardLogix** safety + **Otto Motors AMRs** | Dominant in safety; contender in AMR | Real; Otto won Subaru of Indiana |
| Edge AI at controller | **Logix** (ControlLogix, CompactLogix) | **Weak** — no Jetson-class IPC | Siemens S7-1500 TM NPU ahead |
| Reshoring/CHIPS/IRA | Logix + Intelligent Devices install base | **Dominant in NA** | Real — data center, semi, warehouse, energy infra all called out |

## NVIDIA Omniverse Reality Check
- Integration is **real, not slideware** — Emulate3D Factory Test uses OpenUSD + Omniverse APIs + RTX
- **NOT mentioned once on Q2 FY26 call** — likely <$10M today
- Strategic differentiator vs Siemens Xcelerator+Omniverse, but not a near-term needle-mover

## Bull Case TAM (back-of-envelope, sell-side estimates vary)
- **EV battery gigafactory:** $30–50M ROK content
- **Semi fab:** $20–80M (competes against Yaskawa/Mitsubishi in fab tools; stronger in subfab/facility)
- **Hyperscale data center:** Cubic power distribution + Logix replacing commercial controls + drives for HVAC. ~$50–100M run-rate scaling fast (2x YoY)
- **Biotech facility:** $5–20M PharmaSuite + Logix
- **General reshoring:** NA strongest, +10% organic US in Q2

## Cyclical vs Structural — Honest Read

**Verbatim Moret:** *"We did not see any pull forwards or advance orders in the quarter"* … *"we're still not seeing a wholesale unlock of capital in some of our biggest end markets, namely automotive and consumer packaged goods"* … *"the majority of customer investment is still focused on productivity and smaller modernization initiatives."*

FY26's +9% organic is **~70% cyclical recovery + reshoring + warehouse/data center secular, ~30% AI-adjacent**. AI shows up in **internal productivity** and **incremental software ARR (HSD)** — not in a discrete AI revenue line. Software & Control 34.9% margin is the bright spot.

## Sources
- [Motley Fool ROK Q2 FY26 transcript](https://www.fool.com/earnings/call-transcripts/2026/05/05/rockwell-rok-q2-2026-earnings-call-transcript/)
- [ROK Q2 FY26 earnings PDF](https://www.rockwellautomation.com/content/dam/rockwell-automation/documents/pdf/company/about-us/ir/2026/q2-2026-earnings-presentation.pdf)
- [Emulate3D Factory Test at GTC 2025](https://www.rockwellautomation.com/en-us/company/news/press-releases/Rockwell-Automation-Showcases-Emulate3D-Factory-Test-for-the-First-Time-at-NVIDIA-GTC-2025.html)

---

<a id="analyst-2"></a>
# Analyst 2 — ROK vs SIEGY/EMR/ABB

## Positioning

| | **ROK** | **SIEGY (DI)** | **EMR** | **ABB** |
|---|---|---|---|---|
| Mkt Cap | $50B | $239B | $76B | $193B |
| Core | Allen-Bradley PLCs (US discrete) | SIMATIC PLCs (global, EU/Asia) | DeltaV DCS + NI + AspenTech | Electrification (#1), Motion, Process Auto, Robotics |
| Geo core | ~60% US | Global, Europe-anchored | ~45% US | Truly global |
| AI software | FactoryTalk + Plex/Fiix + NVDA/MSFT/PTC | Xcelerator + Industrial AI Suite + Mendix + Omniverse | AspenTech AVA + Inmation OT Data Fabric | ABB Ability + Genix |

**Overlap:** ROK ↔ SIEGY in discrete PLCs/HMIs/drives — Siemens bigger globally but ROK owns US install base. EMR ↔ ABB in process DCS. **ROK is the ONLY one with effectively zero data-center-power exposure** — ABB/SIEGY/EMR all sell into DC electrical/cooling/instrumentation.

## AI/Smart-Factory Revenue Exposure

| | % AI-factory-tied | Most direct AI play |
|---|---|---|
| ROK | ~85-90% (pure-play) | Logix + FactoryTalk + Plex; NVDA/PTC/MSFT alliances |
| SIEGY | DI ~30% of Siemens AG | **Most-diversified** but conglomerate dilution |
| EMR | ~30-40% | **Most direct industrial-AI software pure-play** via AspenTech AVA (launched May 11, 2026) |
| ABB | Electrification ~50% of group = data-center buildout proxy | Power-for-AI, not AI-for-factories |

## Latest Quarter (Mar-2026)

| Ticker | Rev YoY | Op-Inc YoY | Op Margin | Notes |
|---|---|---|---|---|
| **ROK** Q2 FY26 | **+12.0%** (org +9%) | **+38%** | 21.0% | Raised FY26 guide; DC revenue ~2x YoY |
| **SIEGY** Q2 FY26 | +0.0% | +0.7% | 13.6% | Group orders +18% comparable; DI dragged by China |
| **EMR** Q2 FY26 | +2.9% | +4.7% | 19.7% | AspenTech AVA story, not organic volume |
| **ABB** Q1 2026 | **+18.3%** (comp +11%) | +11.7% | 23.5% EBITA | **Electrification orders +44%, DC triple-digit** |

## Stock Performance & Valuation (close 2026-05-22)

| Ticker | YTD-26 | 1Y | 3Y | Fwd P/E |
|---|---|---|---|---|
| ROK | +16.2% | +47.7% | +62.4% | 31.2x |
| SIEGY | +11.0% | +26.5% | +86.8% | 21.1x |
| EMR | +2.8% | +16.3% | +68.2% | **19.1x** |
| ABB | **+43.8%** | **+86.2%** | **+190.5%** | 31.2x |

ABB run hardest — wRSI 73.5, +33% above 200DMA. ROK re-rated post-Q2 but still –1.5% from 52w high. SIEGY mid-cycle, conglomerate-discounted. EMR is the laggard, masking AspenTech story.

## Verdict — Ranking

| Rank | Ticker | AI Tailwind | Defensibility | Entry |
|---|---|---|---|---|
| 1 | **ABB** | A (DC electrification = cleanest AI capex proxy) | A− | C+ (extended) |
| 2 | **ROK** | B+ (DC + warehouse + reshoring) | A− (US install base) | B− (re-rated, justified) |
| 3 | **EMR** | B (AspenTech AVA unproven adoption) | B+ | A− (cheapest) |
| 4 | **SIEGY** | B (broadest but DI volume flat) | B+ | B+ |

**Most AI-buildout torque: ABB > ROK > EMR > SIEGY. Best risk-adjusted entry: ROK. Contrarian software-pure-play: EMR.**

---

<a id="analyst-3"></a>
# Analyst 3 — ROK Moat vs Chinese Automation

## Chinese Landscape

- **Inovance Technology (300124.SZ)** — by far the most important threat. ~$5.2B rev 2024 (+22% YoY), ~$31B mkt cap. **#1 China general-purpose servo at ~32% share**, top-3 PLCs domestically, leader in VFDs. **MX100 Pro PLC** (launched 2023) is first credible mid/high-tier Chinese PLC vs Siemens S7-1500 and Allen-Bradley ControlLogix. ~90% revenue domestic, international expansion accelerating.
- **Estun Automation (002747.SZ)** — ~$680M TTM rev; #1 Chinese-branded industrial robot at 10.5% China share (7 yrs running). Strong in PV/lithium battery (BYD, CATL).
- **Supcon (688777.SH)** — DCS / process automation. Competes Emerson/Honeywell, minimal ROK overlap.
- **Step Electric, Megmeet, Veichi, GoodWell** — commodity drive players.

**Only Inovance has breadth to threaten ROK across PLC + servo + drives + robots.**

## Technology Gap

| Layer | ROK position | Chinese threat |
|---|---|---|
| **PLC/PAC (ControlLogix, CompactLogix)** | Studio 5000 sticky; hardware 20–40% premium; >50% NA share | Inovance MX100 Pro closing functional gap; still no software ecosystem. **5–10 yr software gap.** |
| **Servo drives (Kinetix)** | Mid-tier commoditizing | Inovance already #1 China; credible global mid-tier. **Most exposed.** |
| **VFDs (PowerFlex)** | Commoditized; 30–50% price premium hard | Inovance/Huichuan win on price. **Already eroded.** |
| **Industrial software (FactoryTalk, Plex MES)** | IDC MarketScape Leader; Plex SaaS MES differentiator | Chinese players **no credible global MES**. SAP/Siemens are competition. **Strongest moat.** |
| **EtherNet/IP + ODVA** | Standard-setter; integrator network in NA | Chinese vendors adopt but don't shape. Defended. |
| **OT cybersecurity (Verve)** | Differentiated | Chinese sub-scale, geopolitically toxic. Defended. |

**Software is the moat. Hardware is not.**

## Switching Risk by Geography

- **US factories:** **Near-fortress.** Studio 5000 code library + Section 889 momentum.
- **Europe:** Siemens dominant — not ROK's home market.
- **China domestic:** ROK has been losing share for a decade. **AP organic –4% FY25, –7% Q3 YTD with double-digit China decline.** Structurally disadvantaged.
- **Mexico / SE Asia / Brazil (US/EU OEM nearshoring):** ROK + Siemens dominate when end customer is US/EU multinational.

## China Revenue Exposure

- AP FY2025 = $1,024M = 12.2% of $8.34B total, **down 5% reported / –4% organic**
- China specifically ~5-7% of total (triangulated from AP + management commentary)
- Siemens reported automation orders **+18% in China** — **ROK underperforming peers in China**
- ROK is the **least China-exposed of the Big 3** (vs ABB ~15%+, SIEGY DI ~12-13%) — both a defense and an admission of weakness

## Moat Ratings (1-10)

| Domain | Rating | Why |
|---|---|---|
| **(a) US factory automation** | **9/10** | Install base + Studio 5000 + geopolitics |
| **(b) Industrial software stack** | **7/10** | Real differentiation vs Chinese (≈10); SAP/Siemens credible Western threats (≈6) |
| **(c) Mid-tier servo/VFD in EM** | **3/10** | Inovance/Huichuan win on price. **Actively eroding.** |

**Bottom line:** ROK is no longer a hardware company — it's a US-installed-base + software company that happens to sell hardware. Most underappreciated risk: **Inovance becoming the global default for cost-sensitive mid-tier automation**, capping ROK's TAM growth outside NA and squeezing PowerFlex/Kinetix pricing.

## Sources
- [Inovance MX100 Pro PLC strategy](https://roboticsandautomationnews.com/2025/09/25/inovance-technology-targets-humanoid-robot-components-and-bolsters-core-plc-business/94751/)
- [Estun #1 China robot share 10.5%](https://en.estun.com/?list_52%2F2288.html)
- [Studio 5000 licensing / switching cost](https://industrialmonitordirect.com/blogs/knowledgebase/studio-5000-license-cost-pricing-tiers-for-controllogix)

---

<a id="analyst-4"></a>
# Analyst 4 — ROK Valuation

## Current Snapshot (close 2026-05-22, $452.29)

| Metric | Value |
|---|---|
| Price | $452.29 |
| Market cap | $50.3B (111.3M shares) |
| Enterprise value | $54.0B (net debt ~$3.7B) |
| **TTM P/E (GAAP)** | **47.0x** (EPS $9.63) |
| **Forward P/E** (FY26 mid $12.80) | **35.3x** |
| **Forward P/E** (FY27 cons $14.51) | **31.2x** |
| **EV / TTM EBITDA** | **27.4x** |
| **EV / TTM Sales** | **6.1x** |
| **P / TTM FCF** | **37.6x** |
| Dividend yield | 1.22% (5y avg 1.64%) |
| Buyback yield (FY25) | ~0.85% |
| Shareholder yield | ~2.1% |

## Historical Multiples (10-yr)

| Stat | TTM P/E | TTM P/S |
|---|---|---|
| Min | 14.5 | 2.16 |
| 25th %ile | 25.4 | 3.38 |
| Median | 31.4 | 3.75 |
| 75th %ile | 38.5 | 4.51 |
| 90th %ile | 45.9 | 5.42 |
| Max | 57.5 (Q4 2021) | 6.05 |
| **Current** | **47.0** | **5.72** |
| **Percentile** | **92nd** | **97th** |

**Pre-COVID baseline (2016–2019):** P/E 29.8 median, P/S 3.35, EV/EBITDA ~17. **Today's P/S is +71% above that baseline.**

## Growth Trajectory

| FY | Rev ($M) | YoY | Notes |
|---|---|---|---|
| 2018 | 6,666 | +5.6% | pre-COVID baseline |
| 2019 | 6,694 | +0.4% | |
| 2020 | 6,330 | -5.4% | COVID |
| 2021 | 6,997 | +10.5% | reshoring; Plex acq |
| 2022 | 7,760 | +10.9% | logistics/EV/CHIPS capex |
| 2023 | 9,058 | +16.7% | cycle peak; channel overstocked |
| 2024 | 8,264 | **-8.8%** | brutal destock |
| 2025 | 8,342 | +0.9% | trough/recovery |
| **2026E** | **8,900** | **+5-9%** | data-center driven |
| 2027E | ~9,500 | ~+7% | |

**Organic vs M&A:** Plex (~$200M), Fiix, Verve, Otto Motors (~$30M), ASEM added ~3-4 pts/yr 2021-2024. Stripping M&A, FY18→FY25 organic CAGR ~3-4% — below 5-7% secular.

## What's Priced In

10Y treasury (^TNX) = **4.56%**. Implied IRR from $452 base FY26 EPS $12.80, 50% payout, 5y EPS growth then 5% terminal:

| 5y EPS gr | Term P/E 18 | 20 | 22 | 25 | 28 |
|---|---|---|---|---|---|
| 5% | -5.4% | -3.5% | -1.8% | +0.6% | +2.8% |
| 9% | -1.8% | +0.1% | +2.0% | +4.4% | +6.7% |
| 13% | +1.8% | +3.8% | +5.7% | +8.3% | +10.6% |

To clear 8% IRR → need ~16% 5y EPS growth at term P/E 22, or ~13% at 25.
To match treasury 4.6% → need 9-10% sustained EPS growth + 25x exit.

## Peer Multiples

| Ticker | TTM P/E | Fwd P/E | EV/EBITDA | EV/Sales | Rev gr |
|---|---|---|---|---|---|
| **ROK** | **47.0** | **31.2** | **27.4** | **6.1** | +11.9% |
| ABBNY | 40.0 | 31.2 | 28.1 | 5.7 | +18.3% |
| ETN | 38.3 | 24.9 | 27.3 | 6.1 | +16.8% |
| PH | 31.9 | 25.5 | 21.6 | 5.6 | +10.6% |
| HON | 36.4 | 19.9 | 20.0 | 4.5 | +2.4% |
| EMR | 31.6 | 19.1 | 15.1 | 4.8 | +2.9% |
| SIEGY | 27.6 | 21.1 | 14.6 | 2.2 | flat |

**ROK at top of peer set on EV/EBITDA and EV/Sales — tied with ABB and Eaton (clear AI/electrification beneficiaries growing 17-18%). ROK gets same multiple while organic-growing half as fast.**

## Verdict — **Expensive vs history; priced as hybrid AI-manufacturing beneficiary**

- **92nd %ile P/E, 97th %ile P/S, EV/EBITDA matches 2021 cycle-top**
- "AI-manufacturing premium" = ~9-11 turns of P/E above 20-22x cyclical/defensive industrial fair multiple → **~$120-140/share (~25-30% of price)**
- Justification thin: DC still "low single-digit %"; FY26/27 consensus 5-9%/+7% at — not above — historical secular range
- TTM EPS $9.63 still cycle-suppressed; normalized power $12-13 → **still ~35x normalized**
- **Fair-value range on FY27 EPS $14.50 at 22-25x = $320-365.** At $452, embeds AI-mfg acceleration not yet in corporate numbers

---

<a id="analyst-5"></a>
# Analyst 5 — ROK Manufacturing & Supply Chain

## Manufacturing Footprint (FY2025 10-K, Item 2)

> "Approximately ten principal manufacturing facilities worldwide, with the most significant of these located in the **U.S., Mexico, Poland, India, Canada, and Singapore**."

**China is NOT named among the most significant manufacturing locations** — change from prior-era disclosures.

Notable sites:
- **Milwaukee, WI** — HQ; Mequon facility recently purchased ($60M)
- **New Berlin, WI** — newly announced >1M sq ft greenfield, designed in NVIDIA Omniverse, part of **$2B US investment**
- **Tecate, Mexico** — large electronics for US market
- **Singapore, Katowice (Poland), India** — confirmed in 10-K
- **Harbin/Shanghai (China)** — historical, still operating per Bloomberg, but de-emphasized

Estimate: ~50-55% NA (US + Mexico + Canada), 20% APAC, 15% EMEA.

## Components

10-K generic: *"raw materials essential to the manufacture of our products generally are available at competitive prices."* **No specific suppliers named.** Industry knowledge: NXP/STMicro/TI/Renesas MCUs for PLCs/HMIs, AMD/Xilinx FPGAs for high-end Logix, Infineon/ON Semi/Wolfspeed for power semis in PowerFlex.

## China Supply Chain

10-K flags China-tariff risk explicitly. Mitigation: *"redundant manufacturing locations... high value product lines in more than one geographic location. Tariff costs are expected to be neutral to EPS in fiscal 2026."* CFO: ~1 pt tariff-based pricing in FY26 guide "simply to offset cost." **Component-level China dependency not quantified — disclosure gap.**

## China Revenue Exposure

AP FY2025 = $1,024M = **12.3% of $8,342M**, down 5%/4% YoY. **China specifically ~5-7% of total**, declining mid-to-high single-digits annually.

## Vertical Integration

ROK designs + manufactures + writes software in-house — between fully fabless CGNX and fully integrated Siemens/ABB. GM ~40% range. Capex 2-3% historically — light for hardware OEM, indicating heavy use of subcontracted board assembly with final test/config in-house.

## AI-Manufacturing Readiness

Positive: **New Berlin campus designed in NVIDIA Omniverse** (eats own dog food); Logix 5000/Emulate3D as edge-AI controllers. No 10-K disclosure of AI-inference silicon partners. Capacity headroom from 2022-23 destock.

## CapEx Trajectory

| FY | CapEx ($M) | Rev ($M) | CapEx/Rev |
|---|---|---|---|
| 2022 | 141 | 7,760 | 1.8% |
| 2023 | 161 | 9,058 | 1.8% |
| 2024 | 225 | 8,264 | 2.7% |
| 2025 | 186 | 8,342 | 2.2% |

**$2B/5-year US investment (~$400M/yr) → step-up to 4-5% of revenue starting FY26.** Strongest tangible commitment to reshored AI-era manufacturing in the comp set.

## Sources
- [ROK FY2025 10-K (rok-20250930)](https://www.sec.gov/Archives/edgar/data/0001024478/000102447825000116/rok-20250930.htm)
- [Manufacturing Dive — Wisconsin greenfield $2B](https://www.manufacturingdive.com/news/rockwell-automation-greenfield-wisconsin-largest-factory-2b-investment/806033/)

---

<a id="analyst-6"></a>
# Analyst 6 — Physical AI TAM (NEW)

## Product-by-Product Matrix

| Product family | Physical AI fit | $ content / unit | Volume direction | 2030 TAM uplift |
|---|---|---|---|---|
| **Allen-Bradley PLCs (Logix)** | Cell controllers in AI factories/fab tools/battery lines; NOT inside humanoids | $5-25k per line; $200k-2M per gigafactory | Linear (+) | **$300-600M** |
| **Kinetix servo drives + motors** | Industrial robots, packaging, fab handling. Humanoids use custom BLDC, NOT industrial servos | $50-300k per machine; **~$0 per humanoid** | Linear; flat-to-zero on humanoids | **$100-200M** |
| **PowerFlex VFDs** | Conveyors, HVAC, pumps | $10-50k per line | Linear (+) | **$150-300M** |
| **Stratix Ethernet switches** | TSN/CIP networking for AMR fleets, edge AI, fab | $20-100k per line | Linear-to-mild-exponential | **$100-250M** |
| **GuardLogix safety controllers** | Mandatory for cobots + AMRs; step-change as collaborative scales | $5-30k per cell | Mild exponential | **$150-400M** |
| **PanelView HMIs / IPCs** | Operator interfaces — declining in dark factories | $2-20k per station | Flat / declining | **-$50 to +$50M** |
| **FactoryTalk software** | MES, predictive analytics, edge inference on Logix | $100k-5M per site | Linear (+), SaaS shift accretive | **$300-500M** |
| **Plex (cloud MES)** | Native cloud MES for AI factories | $30-300k ARR per site | Mild exponential | **$400-800M** |
| **Fiix CMMS / predictive maintenance** | ML on installed-base sensor data | $20-100k ARR / plant | Linear (+) | **$100-200M** |
| **Emulate3D + NVIDIA Omniverse** | Digital twin / sim-to-real for AMR, robot training | $50-500k per project | Mild exponential | **$50-150M** |
| **Verve Industrial (SecureOT)** | Mandatory for AI factories; $22B→$49B OT-security TAM | $50-500k ARR / site | **Exponential off small base** | **$200-500M** |
| **Otto Motors AMRs** | Direct AMR play; now produced at Milwaukee HQ | $80-150k per AMR | **Exponential (15-30% CAGR)** | **$400-1,200M** |
| **Sensia (O&G JV)** | Irrelevant | n/a | Flat | ~0 |

## Asymmetric Opportunities (biggest proportional uplift)

1. **Otto Motors AMRs** — ONLY ROK product directly riding the AMR exponential. Base AMR market $3.5B → $10B+ by 2030; shipments 547k → 2.8M units. Otto did ~$95M in 2026; even modest 5-8% share = **$500M-$1B run-rate**.
2. **Verve / SecureOT** — tiny base, $22B→$49B ICS/OT cyber TAM. **5-10× revenue expansion plausible.**
3. **Plex + FactoryTalk + Fiix software stack** — Software & Control already +17% organic, 34.9% margin. ARR +6%. Where the AI dollar lands first.

## Hidden Assets

- **Otto Motors** — first AMRs rolled off Milwaukee line Oct 2025; integrated with NVIDIA Isaac. ROK is now both AMR OEM and customer of itself — **flywheel underappreciated**
- **Verve / SecureOT** — Dragos partnership + buy-and-build; buried inside Lifecycle Services
- **Emulate3D × NVIDIA Omniverse** — small revenue today but strategic option on sim-to-real
- **Embedded Edge Compute Module + LogixAI** — converts Logix install base into edge-AI inference

## Decliners / Non-Beneficiaries

- **PanelView HMIs:** dark factories need fewer operator panels
- **Kinetix in humanoids:** Industrial Kinetix ($1-3k/axis) is over-spec'd and over-priced vs custom integrated BLDC + harmonic-drive joints (target <$500/joint, Optimus Gen 3 BOM <$20k all-in). **ROK gets ZERO humanoid BOM content** — validated
- **Sensia O&G JV** — orthogonal to physical AI thesis

## Quantified TAM Uplift by 2030

Scenario: 1M humanoids/yr, 1M AMRs/yr, AI factory capex 2×.

- **Humanoids direct content: ~$0-50M/yr** (only GuardLogix tail where humanoids deploy as cobots)
- **AMRs:** 1M units × ~$100k = $100B TAM. Otto at 3-5% share → **$3-5B opportunity** vs $95M today. Even 1.5% share = **$1.5B incremental**
- **AI factory buildout:** 200 mega-facilities/yr × $5-20M × ~10-15% ROK share = **$100-450M incremental/yr**. SaaS pull-through (Plex/Fiix/Verve) compounds another **$500M-1B ARR**

**Total incremental ROK revenue TAM by 2030: ~$2-5B on top of $8.3B base = 25-60% uplift.** Roughly 75-85% of uplift from AMRs + AI-factory buildout + software/cyber ARR. **Humanoids contribute <2% of uplift.**

## Conclusion — Asymmetric Bet

**Answer:** ROK is a **steady industrial-automation compounder** for whom **AI-manufacturing buildout adds ~3-5pp to growth** through 2030 — NOT a humanoid play. CEO Blake Moret explicitly called humanoids **"overkill for most factories"** (CNBC, Nov 2025).

**Asymmetric bet ranking:**
1. **Otto Motors AMR scale-out** — only true exponential lever; Milwaukee production + NVIDIA Isaac integration is real. **If ROK goes all-in on ONE vector, this is it.**
2. **Software stack (Plex + FactoryTalk + Verve)** — durable mid-teens growth, 30% margins, recurring
3. **AI-factory buildout** — broad, linear, durable; biggest absolute $ but lowest proportional uplift

## Sources
- [Rockwell CEO calls humanoids 'overkill' — Humanoids Daily](https://www.humanoidsdaily.com/news/rockwell-automation-ceo-calls-humanoid-robots-overkill-for-most-factories)
- [CNBC video: Moret on humanoids](https://www.cnbc.com/video/2025/11/06/humanoid-robots-are-overkill-for-use-in-most-factories-says-rockwell-ceo-blake-moret.html)
- [First Otto AMRs off Milwaukee line](https://www.rockwellautomation.com/en-us/company/news/press-releases/First-Autonomous-Mobile-Robots-Roll-Off-the-Line-at-Rockwell-Automations-Milwaukee-Headquarters.html)
- [ROK × NVIDIA / Otto / Isaac](https://www.manufacturingdive.com/news/nvidia-rockwell-automation-partnership-ai-robotics-otto/718535/)
- [LogisticsIQ AMR $10B TAM, 500k units 2030](https://www.prnewswire.com/news-releases/autonomous-mobile-robots-amr-market-to-cross-10-billion-tam-with-around-500k-amrs-shipment-by-2030---logisticsiq-302253910.html)
- [ABI mobile robot 2.8M shipments by 2030](https://www.abiresearch.com/press/mobile-robots-set-to-reach-28-million-shipments-by-2030-as-applications-expand-across-industries)

---

<a id="orchestrator"></a>
# Orchestrator Synthesis

## Cross-validated picture

| Dimension | Finding |
|---|---|
| **Q2 FY26 print** | $2.24B rev, **+12% reported / +9% organic**, adj EPS $3.30 (+30%) |
| **Stock perf** | $452, +16% YTD, +48% 1Y, +62% 3Y; -1.5% from 52w high |
| **End-market color** | Discrete +mid-teens; semi +high-teens; warehouse +>30%; **DC sales 2x YoY** (still "low single-digit % of total") |
| **Software & Control** | +17% organic, 34.9% margin (+480bp); Plex profitable; ARR +6% |
| **Otto Motors AMRs** | First units off Milwaukee line Oct 2025; ~$95M revenue; NVIDIA Isaac integrated |
| **Manufacturing** | ~10 principal facilities (US/Mexico/Poland/India/Canada/Singapore); **China NOT named principal**; $2B/5yr US capex commitment |
| **China revenue** | ~5-7% of total (declining mid-to-high single-digits) |
| **CEO Moret on humanoids** | **"Overkill for most factories"** (CNBC Nov 2025) |
| **Moat scores** | US factory automation 9/10; Industrial software 7/10; Mid-tier servo/VFD in EM 3/10 |
| **Valuation** | TTM P/E **47x (92nd %ile 10-yr)**, EV/EBITDA 27x (matches 2021 peak), Fwd P/E 31x |
| **Peers (Fwd P/E)** | ROK 31 vs ABB 31 vs SIEGY 21 vs EMR 19 |
| **AI premium priced in** | ~$120-140/share (~25-30% of price) |

## The verdict on "physical AI" for ROK

**ROK is a steady industrial-automation compounder, NOT a primary physical-AI play.** The Analyst 6 work confirms:

1. **Humanoid content: ~$0 per robot.** Industrial Kinetix servos are over-spec'd and over-priced for humanoid BOMs ($1-3k/axis vs <$500 target). CEO Moret himself calls humanoids "overkill for most factories" — that's the company telling you not to price them as a humanoid story.

2. **The one genuine asymmetric physical-AI lever is Otto Motors AMR.** $95M today, $1-5B opportunity by 2030 at modest share gains. But this is buried inside a $50B market cap — even a 10× Otto run-rate adds $1B revenue to an $8B base = 12% uplift, not transformative.

3. **The real AI story for ROK is AI-MANUFACTURING (factories using AI), NOT AI-ROBOTICS (robots themselves).** Every reshored EV battery plant, semi fab, biotech facility consumes $5-50M of Logix + drives + HMIs + FactoryTalk. This is durable +3-5pp to growth — significant but priced in.

4. **The software stack (FactoryTalk + Plex + Verve) is where AI dollar lands first and where the moat is real (7/10 globally, 10/10 vs Chinese players).** Software & Control's +17% organic and 34.9% margin is the most under-appreciated part of the story.

## Competitive ranking (recap from Analyst 2)

If you want AI-manufacturing buildout exposure, the cleanest play is **NOT ROK** — it's **ABB** (data-center electrification orders +44%, DC orders triple-digit growth, +18% revenue YoY). But ABB has run +43% YTD on the narrative and is most extended.

ROK is the **risk-adjusted second-best entry** in the industrial-automation comp set:
- Cheaper than ABB on growth-adjusted basis (similar 31x fwd P/E but slower growth)
- More direct AI-manufacturing pure-play than SIEGY (no conglomerate dilution)
- Better current execution than EMR (whose AspenTech AVA monetization is unproven)

But **at 92nd percentile of its 10-yr valuation, ROK already prices in AI-mfg acceleration that hasn't yet shown up in corporate-level numbers** (DC is still <10% of revenue; consensus +7% FY27 growth is at — not above — historical secular range).

## The honest answer to "is ROK worth buying now"

**No — not at $452.**

- **Bull case ($500-580, +10-30%):** Otto Motors scales faster than consensus (NVDA Isaac partnership accelerates AMR adoption); DC becomes 5-10% of revenue by 2027; software/cyber ARR compounds at 15%+. FY27 EPS beats $14.51 → $16. Multiple stays at 31x fwd.
- **Bear case ($300-360, -20-35%):** FY26 +9% organic turns out to be the cycle peak; auto/CPG capex stays locked; humanoid narrative cools; multiple compresses to 22x on FY27 EPS $14.50 = $320-360. This aligns with Analyst 4's fair-value range.
- **Base case ($420-470):** Earnings deliver consensus; multiple grinds lower as treasuries elevated. Total return = ~2.2% shareholder yield + modest growth = mid-single-digit IRR.

**Triggers:**
- **Buy** at ≤$360 (Fwd P/E ~25x on FY27, closer to peer median and historical 75th %ile)
- **Sell** if FY26 H2 organic decelerates below +5%, OR if Otto Motors revenue disclosure is disappointing
- **Watch** for Automation Fair (annual event, typically November) for AI/Omniverse product announcements

## Comparison to ADI/CGNX panels we did

| Company | Physical AI exposure | Valuation premium | Verdict |
|---|---|---|---|
| **ADI** | Real (DC 11%, +90% YoY) but back-loaded to 2027 | 27x fwd, top-decile historical | Hold; buy ≤$320 |
| **CGNX** | Hollow — $0 humanoid content, narrative trade | 38x fwd, 97th %ile | Wait for $45-50 |
| **ROK** | Modest — Otto AMR is the one lever; humanoids = $0 | 31x fwd, 92nd %ile | Wait for $360 |
| **ZBRA** (vs CGNX) | Under-appreciated stack | 12x fwd | Asymmetric long |
| **TDY** | FLIR microbolometer is real mass-production play | 24x fwd | Best deep-tech moat |

**ROK is the cleanest US industrial-automation compounder in this set, but the entry point at +16% YTD is wrong. The asymmetric bets remain ABB (highest beta if you can stomach the +44% YTD price) or EMR (cheapest software-pure-play via AspenTech).**

## Caveats
- "AI revenue" is not broken out — all sizing is triangulated from management commentary
- Otto Motors unit shipments not publicly disclosed; the $1-5B AMR opportunity assumes execution against Symbotic/Locus/Geek+
- Sensia JV dissolution clouds FY26 H2 comps (~$100M revenue impact)
- The "humanoids = $0 for ROK" call is high-confidence but speculative — a black-swan industrial-cobot humanoid surge could open a GuardLogix tail
- China revenue figure (~5-7%) is triangulated from APAC segment, not directly disclosed
