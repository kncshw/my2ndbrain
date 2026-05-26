# ADI Research Panel — 5-Analyst Deep Dive

**Date:** 2026-05-24
**Subject:** Analog Devices (ADI)
**Last price:** $397.07 | **Market cap:** $193B
**Latest report:** Q2 FY2026 (May 20, 2026) — $3.62B rev, +37% YoY, EPS $3.09

---

## Table of contents

1. [Analyst 1 — AI/Datacenter product-line map](#analyst-1)
2. [Analyst 2 — ADI vs TXN vs MPS competitive analysis](#analyst-2)
3. [Analyst 3 — Moat vs Chinese competitors](#analyst-3)
4. [Analyst 4 — Pure valuation analysis](#analyst-4)
5. [Analyst 5 — Manufacturing capacity & vertical integration](#analyst-5)
6. [Orchestrator synthesis](#orchestrator)

---

<a id="analyst-1"></a>
# Analyst 1 — ADI: AI/Datacenter Product-Line Map

**Stock/date:** ADI traded down ~7% post Q2 FY2026 print despite a beat. Last data point ~$385 on 2026-05-21.

## 1. Segment breakdown (Q2 FY2026, reported 2026-05-20)

Verbatim from CFO Richard Puncher commentary:
- **Revenue:** $3.62B record, +15% QoQ, +37% YoY
- **Industrial:** 50% of rev, +20% QoQ, **+56% YoY** (A&D, ATE, ETM, broad market)
- **Automotive:** 24% of rev, +8% QoQ, +2% YoY (GMSL, functionally safe power, A2B, BMS returning to growth)
- **Communications:** 15% of rev, +22% QoQ, **+79% YoY**; **data center is now >75% of comms**, growing **>90% YoY**; wireless +35% YoY
- **Consumer:** 11% of rev, flat QoQ, +23% YoY

Implied data center revenue this quarter ≈ 15% × 75% × $3.62B ≈ **$407M, or ~11% of total ADI**. Run-rate ~$1.6B annual. Compare to Q1 FY2026 when data center was ~8% of total — meaningful acceleration in one quarter.

## 2. AI-exposed product map (trend by trend)

| AI trend | ADI product franchises | Position |
|---|---|---|
| **800V HVDC rack** (NVDA MGX/Rubin) | LTC/Maxim hot-swap controllers (high-V), iCoupler/isoPower isolation, gate drivers, isoBuck DC-DC, BMS-derived high-V monitoring; ADI is officially a **named member of NVIDIA's 800V HVDC Supplier Alliance** (Computex 2025) | **Contender** (alongside TI, Infineon, MPS, Power Integrations, OnSemi, Renesas, Vicor). Strong in isolation/hot-swap; thinner in SiC switches |
| **Vertical power delivery to XPU** | **Empower Semi acquisition ($1.5B, announced May 2026, closes 2H FY26)** — integrated voltage regulators (IVR) + silicon capacitors; layered on top of LTC PolyPhase/μModule, Maxim PMICs, Volterra heritage | Was a **gap**, now becomes **Contender→Dominant** post-close. Roche: "fill critical gaps… time is of the essence." |
| **CPO / Co-Packaged Optics** | Optical TIAs, drivers, CDRs (legacy ADN-series), thermal sensing, micro-power mgmt for optical engines. Q2 transcript: comms growth "fueled pretty much equally by power and optical portfolios" | **Contender, not dominant.** Marvell + MACOM lead TIA/driver. ADI plays in support analog (sensing, power, monitoring) and discrete optical signal chain |
| **Pluggable optics (800G/1.6T today)** | Same as above + clock/timing | **Contender.** Optical is half of ADI's data-center growth per mgmt |
| **HBM signal integrity / DDR5** | Retimers, clock buffers, power rails | **Absent/marginal** (Astera Labs, Rambus, Montage dominate; not ADI's wheelhouse) |
| **Liquid cooling sensors / BMC** | Precision temp sensors (ADT74xx), pressure/flow, fan controllers, ADCs | **Niche contender**, no flagship franchise |
| **BMC / server power telemetry** | LTC PMBus, hot-swap, current-sense amps; Maxim DS-series temp | **Solid contender** (TI/MPS competition) |
| **Networking PHYs** | Limited; some industrial Ethernet (10BASE-T1L) | **Largely absent** in datacenter PHY |
| **Robotics / edge AI** | High-perf sensing, motor drive, GMSL, functionally safe power, isolated comms | **Dominant in industrial/auto edge**, not AI-cluster |

## 3. Bull-case quantification (back-of-envelope)

- **800V rack:** ~$50–200 of incremental ADI content per rack power shelf, 8–16 shelves/rack → **$400–$3,200/rack** silicon TAM step-up (range wide; ADI does not disclose $/rack).
- **Empower IVR per XPU:** Roche claimed Empower **"shrinks power footprint by up to 4×, slashes data center compute power consumption 10–15%"** with "ultrafast transient response required by volatile AI workloads." If priced like Volterra/MPS vertical-stack (~$50–150 per high-end accelerator socket), and Rubin/MI400 ship ~5–10M units/yr by 2027, that's **$250M–$1.5B TAM** for Empower-derived content alone. Roche: *"2027 is when we expect to start seeing the surge in demand… significant revenue in 2027."*
- **CPO/optical:** CPO penetration ~0.5% of optical modules in 2026 → projected 35% by 2030 (TrendForce). ADI's optical content is **support analog, not core TIA/driver** — benefits MACOM/Marvell more than ADI in absolute dollars.

## 4. Honest reality check

**Genuine AI exposure today:** ~11% of revenue is datacenter (Q2 FY26 run-rate). AI portion grows >90% YoY. ATE (inside Industrial) is the *other* AI-adjacent line — together mgmt has sized "AI-driven ATE + data center" at **~20% of total revenue** (Q1 FY26 commentary).

**What's hand-waved by sell-side:**
- Industrial (50% of rev) being narrative-stretched to "AI factory" but underlying drivers are **automation, ETM, A&D, ESS/BMS** — not GPU buildout. +56% YoY industrial is largely **cyclical recovery** from a deep trough + ~2 pts pricing. Roche himself flagged the "steepness of the demand ramp" as a 2027 concern.
- Automotive (24% of rev) has **zero direct AI-datacenter exposure**.
- ADI is **not the lead silicon vendor** in 800G/1.6T optics — content supplier alongside Marvell/MACOM/Broadcom.

**Roche on why Empower matters:**
> "The biggest bottleneck that AI is creating for us today is we have got to solve for power density and delivery efficiency… we have to move closer to the core of the problem, which is down at the XPU, the GPU, the CPU… we are buying some critical and very, very unique intellectual property. The integrated voltage reg and the capacitor technology. These are critical building blocks and essential for ADI to solve our customers' problems on time. And be able to catch the wave."

"To catch the wave" is the tell. ADI was **behind** on vertical power before Empower. $1.5B for a "post-revenue phase" startup signals defensive urgency, not from-strength expansion.

## Tailwinds ranked

1. **800V HVDC + vertical power (post-Empower)** — clearest, largest $ TAM; ADI becomes credible leader by 2027.
2. **DC power management (existing LTC/Maxim)** — already driving +90% YoY comms growth.
3. **Optical signal-chain support** — real but secondary; ADI not the TIA/driver winner.
4. **ATE (Industrial)** — AI-adjacent (testing AI chips); record highs.
5. **Liquid cooling sensing / BMC** — small, no flagship franchise.

## Unverified claims
- Exact $ content per AI server / per 800V rack (ADI undisclosed)
- CPO ramp timeline at hyperscalers (consensus 2027–2028)
- ADN-series TIA presence in current 800G/1.6T modules (ADI optical catalog older-generation)

## Sources
- [ADI Q2 FY2026 Transcript - Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/05/20/analog-devices-adi-q2-2026-earnings-transcript/)
- [Empower Acquisition PR](https://www.prnewswire.com/news-releases/analog-devices-to-acquire-empower-semiconductor-expanding-its-next-generation-high-density-power-portfolio-for-the-ai-era-302776701.html)
- [NVIDIA 800V HVDC Blog](https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/)
- [800V HVDC Supplier Alliance](https://eu.36kr.com/en/p/3518189764418694)
- [ADI 800V hyperscale article](https://www.analog.com/en/signals/articles/800-volts-powering-future-hyperscale-data-centers.html)
- [Optical Module Market Deep Dive](https://deepfundamental.substack.com/p/deep-dive-optical-module-market)
- [Futurum: ADI Q1 FY26 AI DC Upside](https://futurumgroup.com/insights/analog-devices-q1-fy-2026-broad-based-recovery-with-ai-data-center-upside/)

---

<a id="analyst-2"></a>
# Analyst 2 — ADI vs TXN vs MPS

## 1. Product positioning & overlap

| Company | Core franchise | AI infra touchpoints | Defensibility |
|---|---|---|---|
| **ADI** | High-perf data converters, precision signal chain, RF, isolation; LTC/Maxim power | Optical DSP/drivers, hybrid/board power for accelerator boards, ATE | Process+design moat in high-speed ADC/DAC, optical; long industrial cycles |
| **TXN** | Broad-line analog + embedded, in-house 300mm fabs (Sherman, Lehi) | Core power, signal-conditioning, ~$1B+/yr DC business broad-attach | Manufacturing cost + catalog breadth; not silicon-superior, but cheapest at scale |
| **MPS** | Power management ICs + integrated modules | NVDA accelerator VRMs, optical-module power, switch power | Module integration speed; fabless, multi-foundry; **socket-level**, not portfolio |

Overlap zone: **DC board power** — MPS leads in monolithic high-current VRMs for GPUs; ADI (LTC heritage) covers higher-precision/multi-rail; TXN takes everything else with cheaper catalog parts. Outside DC the three barely overlap.

## 2. AI revenue exposure

| | Latest DC/AI rev (est.) | % of total | YoY growth | Concentration |
|---|---|---|---|---|
| **ADI** | ~$400M/q (75% of 15% Comms ≈ 11% of $3.62B) | **~11%** | **+90%+** | Diversified — NVDA + hyperscalers + telco |
| **TXN** | ">$1B/yr", ~$300M/q implied | **~6%** | **+~90%** | Spread across many sockets, low per-customer |
| **MPS** | $263M/q (Enterprise Data segment) | **~33%** | **+97.7%** | Heavily NVDA-skewed; FY26 guide ≥+85% |

MPS = 3x ADI's AI mix, 5x TXN's. But Edgewater Research flagged **socket-share risk** on Blackwell B200/GB200 (Renesas, Infineon second-sourced after MPS VRM performance issues late 2024). Winning back in Rubin (~70% reported). Lose one NVDA platform and Enterprise Data craters.

ADI's 11% is small but +90% YoY — optical-driver content scales with **port count**, not GPU count → protected against any single accelerator cycle. TXN's AI exposure is diluted: even +90% YoY in DC adds only ~3 pp to total growth.

## 3. Growth & margin scorecard

| | Period | Revenue | YoY | GAAP GM | Trend |
|---|---|---|---|---|---|
| **ADI** | Q2 FY26 (Apr) | $3.62B | **+37%** | **67.3%** | Industrial inflecting (+56% YoY), Comms +79% |
| **TXN** | Q1 CY26 (Mar) | $4.83B | +19% | 58.0% | Recovering off 2024 bottom; depreciation pressure on GM |
| **MPS** | Q1 CY26 (Mar) | $0.80B | +26% | 55.3% | Enterprise Data +97.7%; **GM fell** sequentially (mix shift) |

ADI stands out — highest YoY growth, highest GM, broadest cyclical recovery. TXN's 19% looks tepid only because the base is largest; $ added ($760M YoY) similar to ADI's $983M. MPS growth great but GM under pressure.

## 4. Stock performance (through 2026-05-22)

| | YTD-26 | 1Y | 3Y | vs SMH 3Y (+339%) |
|---|---|---|---|---|
| **ADI** | +45.1% | +87.4% | +111.3% | Big lag |
| **TXN** | +74.2% | +71.6% | +82.2% | Bigger lag |
| **MPS** | +69.8% | +136.5% | +275.2% | Near-SMH; AI mostly priced |
| NVDA | +14.0% | +62.1% | +601.7% | Reference |
| SPY | +9.1% | +27.9% | +80.1% | Reference |

Valuations: ADI Fwd P/E **27**, TXN **33**, MPS **53**. P/S 15 / 15 / 26. TXN's YTD outperformance striking given weakest fundamental delta — multiple expansion on AI narrative without proportional AI revenue. MPS clearly priced AI. ADI cheapest entry with strongest current quarter.

## 5. Verdict — ranking

1. **MPS = highest beta, but expensive and concentrated.** Best **trade**, worst **risk-adjusted** entry.
2. **ADI = best risk/reward.** AI 11% growing +90%, industrial recovery +56% YoY. 67% GM, 27x Fwd P/E. Optical/power AI optionality almost free. Wins on **defensibility + entry point**.
3. **TXN = AI tourist.** Real DC but diluted, lower-margin, YTD +74% on a thinner narrative.

**Pick: ADI for AI tailwind with downside protection; MPS only on a 15%+ pullback.**

**Uncertainty flags:** (a) ADI's "75% of Comms" is mgmt verbal; (b) TXN doesn't break out DC; (c) MPS Rubin share (~70%) is sell-side rumor.

---

<a id="analyst-3"></a>
# Analyst 3 — ADI Moat vs Chinese Competition

## 1. Chinese analog landscape today

| Player | Focus | ADI overlap |
|---|---|---|
| **SG Micro (300661.SZ)** | Broad TI-style analog; ~4,000 SKUs; LDOs, op-amps, 24-bit Σ-Δ ADCs (SGM58200/01, ≤960 SPS) | Low/mid precision ADC, op-amps, PMIC |
| **3Peak (688536.SH)** | Signal chain. High-speed catalog **14-bit / 250 MSPS** ADC, 10-bit/125 MSPS DAC; precision: 18-bit 300 kSPS SAR, 24-bit 8 kSPS Σ-Δ | Direct industrial signal-chain overlap, orders of magnitude slower at top |
| **Awinic (688798.SH)** | Audio amps, haptics, LED drivers | Negligible |
| **GigaDevice (603986.SH)** | MCU-first; SAR ADCs ≤5 MSPS, 12–14-bit inside GD32 MCUs | MCU-bundled converters only |
| **Novosense (688052.SH)** | Isolation, sensors, auto signal chain | Direct on isolators / hall sensors |
| **Will/OmniVision (603501.SH)** | CIS image sensors | Out of ADI scope |

**Bleeding edge?** No. Public Chinese leader (3Peak) caps at ~14b/250 MSPS. TI's DAC39RF12 = **24 GSPS / 16-bit**; ADI's AD9176 = **12.6 GSPS / 16-bit**. On precision, Chinese ≤24-bit; TI ADS1263 / ADI LTC2500-32 = **32-bit**. *Caveat: Chinese defense-lab work (CETC, CASIC) not in commercial catalogs.*

## 2. ADC/DAC technology gap

The "5–10 year lead" is **directionally correct but uneven**:

- **High-speed RF (GSPS-class):** gap is real and arguably **widening**. ADI uses TSMC 28nm RF CMOS + custom interleaving/calibration IP + SerDes/JESD204C. Chinese players lack mature JESD204C IP and adequate ATE (>5-GHz characterization). Fab access (SMEE/Naura) not the bottleneck; **design IP + mixed-signal calibration know-how + test infra are.**
- **Mid-resolution precision (16–18-bit, ≤1 MSPS):** gap **closing fast.** 3Peak ships 18-bit SAR; SGMicro shipped 24-bit Σ-Δ (SGM58201) 2025 with 22-bit ENOB, 10 ppm/°C — credible against ADI AD7124. Chinese CAGRs 2018–23: SGMicro 36%, 3Peak 57%, Novosense 101%.
- **32-bit precision and >10 GSPS RF:** no Chinese commercial equivalent.

Verdict: ADI's top-end lead is **structural (3–7+ years)**; commodity precision tier is **months, not years**.

## 3. Datacenter switching risk

**Will US hyperscalers qualify Chinese analog in NVDA-class racks? No, not credibly this decade.**
- ADI named partner in NVIDIA 800 VDC reference architecture (Aug 2025) alongside TI/Infineon/ST. LTC4284/4286/4287 hot-swap controllers in Blackwell rack PDUs.
- Section 1260H / Entity List risk → PRC-origin silicon politically toxic in US AI factories.
- 18–36 month qualification cycles → sticky once in BOM.
- Software/reference-design lock-in (LTpowerCAD, eval boards, simulation models).

**Inverse risk is real:** Chinese hyperscalers (Alibaba, ByteDance, Tencent, Baidu, Huawei) under state pressure to swap US suppliers. Buying Cambricon/Huawei Ascend + qualifying domestic memory; analog content increasingly 3Peak/SGMicro/Novosense + Silergy. ADI captures little of *Chinese-owned* AI infra growth. ADI auto/industrial China revenue also at risk on 5–10 yr horizon.

## 4. China revenue exposure

- **FY2025 (ended Nov 2025): China ≈ $2.9B, ~26% of $11.0B total**, vs US ~$3.2B. Q4 industrial-segment growth ~34% YoY (strongest geo).
- China grew **off a 2023–24 trough**. Bounce is cyclical recovery + EV/industrial-auto share gains, **not** evidence de-risking thesis is wrong.
- Trend: China share 22–28% over 3 years; FY25 strength masks ongoing low/mid-end displacement.

## 5. Verdict (1–10 moat scores)

| Segment | Moat | Rationale |
|---|---|---|
| **(a) High-perf converters (>1 GSPS RF, ≥18-bit)** | **9/10** | Multi-yr IP + test-infra lead; defense/aerospace/CSP sticky |
| **(b) Power management post-LTC/Maxim** | **7/10** | Strong in 48V/800V hot-swap, μModule; eroding vs MPS, Silergy, Infineon in commodity DC-DC |
| **(c) Auto/industrial signal chain** | **6/10** | Real in BMS, isolation, precision sensing; **eroding fastest** in China mid-tier |

**Bottom line:** ADI's crown jewel — high-speed/high-resolution converters in US AI and defense — is genuinely defended next 3–5 years and benefits from 800 VDC buildout. Erosion is at mid/low end inside China (~25% of revenue). Bear case isn't displacement; it's a slow margin grind as Chinese substitutes climb the curve while ADI's China TAM caps out.

## Sources & caveats
- [ADI FY2025 press release](https://www.analog.com/en/newsroom/press-releases/2025/11-25-2025-adi-reports-4th-qtr-fiscal-2025-financial-results.html)
- [ADI 10-K](https://www.sec.gov/Archives/edgar/data/6281/000119312526020138/d75638dars.pdf)
- [ADI 800 VDC PR](https://www.analog.com/en/newsroom/press-releases/2025/8-21-2025-powering-the-future-of-ai.html)
- [Findchips: China analog gap](https://blog.findchips.com/how-big-is-the-gap-between-chinese-and-overseas-signal-chain-chip-manufacturers/)
- [3Peak high-speed ADC](https://www.3peak.cn/high-speed-adc)
- [SGMicro SGM58201 launch](https://component.eetrend.com/content/2025/100589403.html)

**Blind spots:** (1) Chinese defense RF capability not in open sources; (2) didn't pull literal 10-K geo table; (3) Chinese-language coverage would give better SGMicro/3Peak roadmap detail.

---

<a id="analyst-4"></a>
# Analyst 4 — ADI Valuation

**As of 2026-05-24 | Last close 2026-05-22 = $397.07**

## 1. Current valuation snapshot

| Metric | Value |
|---|---|
| Price | **$397.07** |
| Market cap | $193.4B |
| Enterprise value | $198.7B (cash $3.4B / debt $8.7B) |
| **TTM P/E (GAAP)** | **59.2x** ($6.71 TTM EPS) |
| Forward P/E (FY26 non-GAAP est ~$12.09) | **~32.8x** |
| Forward P/E (FY27 cons non-GAAP $14.73) | **~26.7x** |
| TTM EV/EBITDA | **32.3x** |
| TTM EV/Sales | 15.6x |
| TTM P/Sales | 15.2x |
| TTM P/FCF | 42.4x (FCF yield 2.36%) |
| Dividend yield | 1.11% |
| Buyback yield (TTM $2.16B) | 1.12% |
| **Shareholder yield** | **2.23%** |
| 52-wk range | $210.8 – $435.7 |
| US 10Y (^TNX) | 4.56% |

## 2. Historical multiples (10-yr context)

| Multiple | 10-yr min | Median | 10-yr max | **Today** | **Percentile** |
|---|---|---|---|---|---|
| TTM P/E | ~15x (2018) | ~25-28x | ~60x | **59.2x** | ~99th |
| EV/EBITDA | 12.8x | 18.6x | 37.5x | **32.3x** | ~90th |
| P/Sales | ~3.5x | ~7x | ~15x | **15.2x** | ~99th |

**Pre-AI anchors:**
- **FY2018-19 (pre-COVID, pre-AI, post-Linear):** TTM P/E ~17-22x, EV/EBITDA ~13-15x.
- **FY2022 cyclical trough (Oct-Dec 2022):** TTM P/E ~17-19x; EV/EBITDA ~14-15x.
- **10-yr avg P/E ~37.7x** is inflated by trough-earnings years.

Today's TTM P/E of 59x is **near all-time high**; EV/EBITDA 32x in top decile.

## 3. Growth trajectory — pre-AI vs now

| Period | Revenue ($B) | Notes |
|---|---|---|
| FY15 | 3.44 | pre-Linear |
| FY16 | 3.42 | pre-Linear |
| FY17 | 5.11 | Linear closed Mar-2017 |
| FY18 | 6.20 | first full year w/ Linear |
| FY19 | 6.00 | flat — cycle softness |
| FY20 | 5.60 | COVID dip |
| FY21 | 7.32 | Aug-2021 Maxim close (partial) |
| FY22 | 12.01 | first full year w/ Maxim — cycle peak |
| FY23 | 12.31 | prior peak |
| FY24 | **9.43** | cycle trough (-23%) |
| FY25 | 11.02 | recovery (+17%) |
| **TTM** | **12.74** | already above FY23 peak |
| **FY26 est** | **~14.7** | **+34% YoY** at Q3 guide midpoint |

- **Organic FY18→FY19 (post-Linear, pre-Maxim):** ~flat to -3% — cyclical industrial/auto character.
- **FY15-FY19 reported CAGR:** ~14.9% but M&A-driven; **organic mid-single digits** consistent with ADI's secular guide.
- **Q2 FY26:** $3.62B, +37% YoY, +15% QoQ, non-GAAP EPS $3.09. Industrial 50% (+56% YoY); Comms 15% (+79% YoY) with DC >75% of comms +90% YoY.
- **Q3 FY26 guide:** $3.9B ± $0.1B (+35% YoY), non-GAAP EPS $3.30 ± $0.15, adj op margin 49%.
- **FY26 consensus growth:** mid-30s%; FY27 ~10-12%. Pre-AI 4-6% organic baseline replaced by 30%+ "year of AI" print.

## 4. What's priced in?

- **Forward P/E ~26-33x** depending on FY26 vs FY27 anchor.
- **Earnings yield (FY27 non-GAAP fwd): ~3.7%** vs 10Y **4.56%** → **negative implied ERP ~80 bps**.
- **Reverse DCF:** at 9% required IRR with 2.2% shareholder yield, ADI needs **~8-10% EPS CAGR for next decade** to justify 27x fwd — market pricing ADI as having permanently exited 4-6% organic regime.
- Cyclical analog peers historically 15-18x P/E mid-cycle; AI beneficiaries 25-35x+. **ADI now firmly in AI-beneficiary bucket** (32x EV/EBITDA vs NXPI 18x, ON 23x; closest comp TXN 33x).
- Street targets: median $393-$444 (Raymond James $430, TD Cowen $450, Evercore $474) — limited margin of safety.

## 5. Verdict

**Expensive vs history; richly fair vs the new AI narrative.**

- TTM P/E 59x, EV/EBITDA 32x in **90-99th percentile**. Fwd P/E ~27x (FY27) is **~50-80% above FY18-19 pre-AI baseline of 17-22x** — **"AI premium" ≈ 8-10 turns of P/E**, **~$130-160/share of the $397 price**.
- Premium **not unjustified** given DC revenue +90% YoY is a structurally new leg. But requires sustained ~10% EPS growth after FY26 snapback fades.
- **TTM understates** because it captures trough/recovery transition; on normalized FY27 ~$15 non-GAAP EPS, P/E compresses to ~27x — still rich vs pre-AI but not bubble-like.
- **Bottom line:** ADI priced as hybrid cyclical-industrial + AI infra. Negative implied ERP and zero margin of safety to consensus → **no cushion if AI capex slows or Q3 FY26's +35% is the cycle peak**.

---

<a id="analyst-5"></a>
# Analyst 5 — Manufacturing Footprint

## 1. Fab ownership and locations

| Fab | Source | Wafer size | What's made |
|---|---|---|---|
| **Wilmington, MA** | Legacy ADI | 200mm (8") | Proprietary BCD/bipolar; flagship precision analog |
| **Chelmsford, MA** | Legacy ADI | 200mm | Specialty processes (CHIPS Act site) |
| **Camas, WA** | LTC (2017) | 150mm → modernizing to 200mm | LTC bipolar/CMOS, high-perf analog |
| **Beaverton, OR** | Maxim (2021) | Converting to full 200mm, cleanroom +25k sq ft, ~2x capacity | Maxim mixed-signal/power |
| **Limerick, Ireland** | Legacy ADI | 200mm | Large fraction of converter portfolio; ~$1B upgrade |

No 300mm internal fab; ADI accesses 300mm only via TSMC. Historically ~50% internal, ~50% foundry. CFO target: ~70% of revenue via hybrid model.

## 2. Foundry partners

- **TSMC** — primary, 30+ year relationship. Feb 2024 expanded agreement secures **JASM Kumamoto** (12/16nm and 22/28nm FinFET, 300mm) for **wBMS** and **GMSL** converters.
- **GlobalFoundries** — historic RF SOI / mature.
- **Tower Semi, UMC** — secondary mature-node, small share.
- **SMIC / Hua Hong (China)** — **NO disclosed relationship.** Clean differentiator vs MPS.

## 3. Assembly / test / packaging

- **General Trias, Philippines** — largest back-end campus
- **Penang, Malaysia** — test, being expanded
- **Chonburi, Thailand** — wafer-level, CSP, final test; March 2026 expansion explicitly for "geographic diversification"

Philippines remains single largest back-end node; Thailand/Malaysia ramp = de-risking play.

## 4. China-specific exposure (manufacturing)

- **Wafer fab in China: None.** Verified.
- **Back-end ATP in China: None disclosed.** Design centers + Shanghai commercial only.
- **Operational disruption from US-China decoupling: very low** on supply side.
- **Revenue hit material:** China ~$2.86B FY25, +34% YoY, ~26% of $11.0B. Export ban hits top line, not factory.

## 5. Vertical integration vs peers

| | Model | China foundry exposure |
|---|---|---|
| **TXN** | Heavy IDM — building 300mm Sherman + Lehi (multi-$10B capex). Long cycle, GM pressured. | None |
| **ADI** | Hybrid — ~50% internal / 50% foundry, TSMC Japan for 300mm fine-pitch. Lighter capex. | None |
| **MPS** | Fabless — TSMC + **Hua Hong** heavily. Lowest capex; **real China exposure** | **Yes (Hua Hong)** |

Implications: (a) ADI GM more resilient than TXN through cycles (less under-absorption); (b) supply security solid post-TSMC Japan; (c) ADI capex ~5% rev vs TXN mid-teens.

## 6. AI infra manufacturing readiness

- **800V power** — built on mature BCD/bipolar; internal 200mm fabs are right home. No external dependency, no capacity gate.
- **CPO** — finer nodes → TSMC/JASM lean; in-house RF/SiGe at Wilmington covers some.
- **Capacity bottleneck risk:** more likely **back-end test** (driving Thailand/Philippines/Malaysia expansions) than wafer starts. Long-term capex 4–6% of revenue → no major front-end constraint anticipated.

## 7. CapEx trajectory (yfinance)

| FY | CapEx | OpCF | CapEx/Rev |
|---|---|---|---|
| FY22 | **$699M** | $4.48B | ~7% |
| FY23 | **$1,261M** (peak) | $4.82B | ~10% |
| FY24 | **$730M** | $3.85B | ~7.5% |
| FY25 | **$534M** | $4.81B | ~4.8% |

ADI front-loaded capacity in FY22–FY23 (Beaverton + Limerick + Maxim integration) **then cut hard through the downturn**. FY25 capex at floor of 4–6% band. Signal: ADI is **not** ramping a multi-billion fab build for AI — expects TSMC + installed capacity to carry the ramp, supplemented by **CHIPS Act funding (Jan 2025 preliminary)** for Chelmsford/Beaverton/Camas onshoring 180nm/350nm.

## Not verified
- Exact internal vs foundry wafer-start % FY2025 (10-K direct fetch failed; "~50/50 historically" is best available).
- GF / UMC / Tower share of external wafers — not publicly disclosed.
- Final CHIPS Act award amount (Jan 2025 was preliminary).

## Sources
- [ADI FY2025 10-K (SEC)](https://www.sec.gov/Archives/edgar/data/0000006281/000000628125000153/adi-20251101.htm)
- [ADI Resilient Hybrid Manufacturing](https://www.analog.com/en/who-we-are/resilient-hybrid-manufacturing.html)
- [ADI–TSMC Feb 2024 PR](https://www.analog.com/en/newsroom/press-releases/2024/2-22-2024-adi-strengthens-capacity-resiliency-through-expanded-partnership-tsmc.html)
- [Commerce CHIPS preliminary terms](https://www.commerce.gov/news/press-releases/2025/01/department-commerce-announces-preliminary-terms-analog-devices-coherent)
- [ADI Thailand expansion Mar 2026](https://www.analog.com/en/newsroom/press-releases/2026/3-19-2026-adi-strengthens-global-manufacturing-resilience-thailand-facility.html)

---

<a id="orchestrator"></a>
# Orchestrator Synthesis

## Cross-validated picture

| Dimension | Finding |
|---|---|
| **Quarter just printed** | Q2 FY26: $3.62B rev, **+37% YoY**, EPS $3.09; GM 67.3% |
| **Mix** | Industrial 50% (+56% YoY), Comms 15% (+79%, **DC >75% of Comms +90% YoY**), Auto 24% (+2%), Consumer 11% |
| **DC revenue today** | ~$400M/q ≈ **~11% of total**, was ~8% one quarter ago |
| **AI-adjacent (DC + ATE)** | ~20% of total per mgmt |
| **Recent big move** | $1.5B Empower Semi acquisition (May 2026) — vertical IVR for XPUs; Roche: *"to catch the wave"* |
| **Manufacturing** | Hybrid: 5 internal 200mm fabs + TSMC (JASM Japan 12/16nm); **zero China wafer or back-end** |
| **China as customer** | ~26% of revenue ($2.9B FY25, +34% YoY); revenue-side risk only |
| **Moat scores** | High-speed converters 9/10; Power post-LTC/Maxim 7/10; mid-end industrial signal chain in China 6/10 |
| **Valuation** | TTM P/E 59x (~99th %ile), EV/EBITDA 32x (~90th %ile), Fwd P/E ~27x. **Negative implied ERP** |
| **Pre-AI baseline** | FY18-19 organic flat-low single digits; P/E 17-22x. Premium today ≈ **8-10 turns of P/E, ~$130-160/share** |
| **Stock perf** | YTD +45%, 1Y +87%, 3Y +111% — still lagging SMH 3Y (+339%) and MPS (+275%) |

## Convergence points

1. **AI exposure real but small** (~11% of revenue; +90% YoY off a thin base). ADI is not NVDA.
2. **2027 story, not 2026 story** — Empower volume + 800V Rubin rollout both 2027–2028. Today's +37% is **80% cyclical recovery + 20% AI**.
3. **Moat asymmetric** — bulletproof at high end; thinning at China mid-end. Bear case = slow margin erosion, not displacement.
4. **No supply-side China risk; meaningful demand-side China risk.**
5. **Valuation is the problem** — priced as AI beneficiary while only ~20% is AI-exposed. Zero margin of safety.

## Verdict

**High-quality name, wrong entry point. Hold if you own it; build a position only on a 15–20% pullback.**

- **Bull ($475–$520, +20-30%):** FY27 EPS $16+, AI mix 11% → 18%, 800V/Empower content drives ASP step-up, multiple holds. Industrial has 4–6Q recovery left.
- **Bear ($280–$320, -20-30%):** Q2 +37% is cycle peak. Industrial normalizes (Roche's own warning), AI capex digests H2 2026/early 2027, multiple compresses 27x → 20x as market reclassifies back to "cyclical analog with AI optionality."
- **Base (range $360–$430):** EPS deliver, multiple grinds lower as treasuries elevated. Total return = ~2.2% shareholder yield + modest EPS growth = mid-single-digit IRR. Inferior to risk-free.

**Triggers:**
- **Buy aggressively** on pullback to ≤$320 (Fwd P/E ~22x, closer to pre-AI band), OR clear 800V Rubin design-win disclosure with $/rack content.
- **Sell** if hyperscaler capex guides down, OR DC growth decelerates below +50% YoY in Q3/Q4 FY26.

## Peer ranking for AI semis exposure now

1. **MPS on a pullback** — highest beta, socket-concentration risk + 53x Fwd P/E
2. **ADI on a pullback** — best diversification + entry-point asymmetry
3. **TXN** — hardest to justify; 33x Fwd P/E on 19% growth with manufacturing capex drag

---

**Final recommendation: NOT a "back up the truck" name today. Watchlist with buy trigger at $320–$340 (15–20% lower). If you must own analog AI now, prefer ADI to TXN, but size small.**

## Caveats flagged
- ADI's "75% of Comms is datacenter" is mgmt verbal, not GAAP-disclosed
- Empower revenue contribution unknown until 2H FY26 close
- Chinese defense-program RF capability is a blind spot
- Q2 FY26: stock fell ~7% despite the beat — market may be signaling peak-quarter concern
