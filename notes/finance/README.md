# Finance notes — index

Reference material for personal portfolio analysis, market monitoring, and hedging decisions. The watch loop is the operational frame; the methodology file is the technical foundation; the historical analog is the base-rate reference.

## Files in this folder

### Foundation
- **[research-methodology-finance.md](./research-methodology-finance.md)** — Data conventions (yfinance default, financial-datasets MCP as supplemental + free-tier rules + gotchas), RSI methodology (Wilder, timeframe labeling, ≥2y history), workflow rules (discuss before writing). Read first when starting any financial analysis.

### Operational framework
- **[watch-loop-architecture.md](./watch-loop-architecture.md)** — Watch–Analyze–React loop. Tier framework (0 through 4.5 + 5), asymmetric watch (downside only), decision authority (Claude flags, user decides), cadence and output format, pending decisions (notification + sync).

### Reference material
- **[historical-bear-analog-2021-2022.md](./historical-bear-analog-2021-2022.md)** — The 2021 peak / 2022 bear analog. Peak/trough magnitudes, SMH timeline with Fed overlay, RSI at peak comparison, bearish divergence pattern, sizing reference for hedge decisions.

## How they relate

```
research-methodology-finance.md
        │
        │ used by
        ▼
watch-loop-architecture.md  ───────  references  ───────►  historical-bear-analog-2021-2022.md
        │                                                              │
        │ informs                                                       │ informs
        ▼                                                              ▼
   daily/YYYY-MM-DD-am-brief.md   (operational output — short-lived)
```

- The **methodology** sets technical conventions used everywhere.
- The **watch loop** is the operational framework that fires daily/weekly briefs.
- The **historical analog** provides base rates and pattern checklists referenced by the watch loop.
- Outputs land in `../../daily/` (short-lived, scratch space).

## External references

- Project conventions (top-level): `../../../CLAUDE.md`
- Daily writeups (scratch / short-lived): `../../daily/`
