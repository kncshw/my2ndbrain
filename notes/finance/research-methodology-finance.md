# Research Methodology — Financial Data & Technicals

Personal conventions for any market / equity analysis I work on with Claude.

## ⚡ Reusable scripts — USE THESE, re-implement only if they fail

**Before writing any yfinance / RSI code inline, check `/Users/kaini/prj-2026/scripts/`.**

The core utilities are already implemented in `lib_finance.py`:

```python
import sys
sys.path.insert(0, '/Users/kaini/prj-2026/scripts')
from lib_finance import (
    snapshot,           # multi-ticker RSI/200DMA/52wH table
    divergence_check,   # bearish divergence detector
    ndx_smh_spread,     # SMH wRSI - NDX wRSI
    base_rate,          # historical fwd returns by RSI bin
    rsi,                # Wilder RSI (the primitive)
    get_history,        # yfinance wrapper with timezone stripped
    PORTFOLIO, INDEXES, HOLDINGS,  # standard ticker lists
)
```

Full function reference: `/Users/kaini/prj-2026/scripts/README.md`. The Bash heredoc pattern for invoking from Claude Code is documented there.

**Use these — re-implement only if they fail.** If a script breaks or a needed helper is missing, fall back to inline as a last resort, then add the missing helper to `lib_finance.py` and update the README. The methodology must stay singular — divergence between docs and code is how methodology drifts.

---

## Data fetching: Python + yfinance is the default

Web search is unreliable for numerical market data. Articles cite mismatched windows, summaries hallucinate YTDs, issuer pages fail to load. Always default to `yfinance` for prices, returns, and technicals.

```python
import yfinance as yf

t = yf.Ticker("SMH")
hist = t.history(period="2y", auto_adjust=False)

last = hist["Close"].iloc[-1]
ytd_base = hist.loc["2025-12-31":].iloc[0]["Close"]
ytd_pct = (last / ytd_base - 1) * 100
yr_pct  = (last / hist["Close"].iloc[-252] - 1) * 100

print(f"{t.ticker}: ${last:.2f}  YTD {ytd_pct:+.2f}%  1Y {yr_pct:+.2f}%")
```

Web search is for **narrative context only**: news, catalysts, analyst commentary, sentiment color. Not for the numbers themselves.

## Supplemental: financial-datasets MCP

yfinance stays primary. The financial-datasets MCP (`mcp.financialdatasets.ai`) is a supplemental source — use it only where it gives something yfinance can't.

### Free tier — what's actually accessible

Empirically derived (their docs don't enumerate the free tier). Two-axis rule:

**Free for ALL tickers** (SEC EDGAR–sourced, public underlying data):
- `get_income_statement`, `get_balance_sheet`, `get_cash_flow_statement`
- `get_filings`, `get_filing_items`, `list_filing_item_types`
- `get_company_facts`
- `get_segmented_financials`, `get_earnings` (likely — also SEC-sourced)

**Free for demo tickers only** (likely AAPL, MSFT, NVDA, TSLA; others 503 with misleading `balance is $0.00`):
- `get_insider_trades`
- `get_financial_metrics`, `get_financial_metrics_snapshot`
- `get_news`
- `get_stock_price`, `get_stock_prices`
- `screen_stocks`, `list_stock_screener_filters`
- `get_interest_rates` (no ticker; likely free)

**Paid only** (explicit in docs — Pro/Enterprise):
- `get_kpi_guidance`, `get_kpi_metrics`, `get_kpi_non_gaap`

### Portfolio implication

Of holdings (NVDA, GOOGL, TSM, AVGO, INTC, AMD, MU, COHR, GLW), only **NVDA** is in the likely demo set. For everyone else the MCP gives only SEC fundamentals + filing text — no insider, no metrics snapshot, no news, no live prices.

### When the MCP actually adds value vs yfinance

- **SEC filing text extraction** — `get_filing_items` pulls Risk Factors / MD&A / specific items from 10-K/10-Q/8-K. yfinance can't do this.
- **Segmented financials** — clean Search/Cloud/YouTube split for GOOGL, AWS/Retail for AMZN, etc. (free across tickers). yfinance segments are messier.
- **Insider trades on NVDA / demo tickers** — yfinance only summarizes.
- **Company facts** — sector/industry/employee count/CIK in one shot.

For everything else (prices, returns, RSI, basic income/cashflow), stay with yfinance + local scripts.

### Data quality gotchas observed

- **`free_cash_flow` field is wrong in `get_cash_flow_statement`.** Reported $223.6B for GOOGL FY2025; correct figure (OCF − capex = 164.7 − 91.4) is **$73.3B**. Always recompute, never trust the field.
- **Quarterly statements skip Q4s entirely** (source is 10-Q filings; Q4 lives only in the 10-K). To get Q4: take annual minus Q1+Q2+Q3.
- **`get_financial_metrics_snapshot.revenue_growth` is QoQ sequential, not YoY.** NVDA snapshot reported "18%" — actual YoY for the same quarter is +73%. Always cross-check via the quarterly income statement (or yfinance).
- **Error message `Your current balance is $0.00`** is misleading. On the free tier it actually means "this endpoint × this ticker isn't on your plan" — not literally an exhausted credit balance. Don't waste retries.

## RSI is the primary technical indicator

For any market or equity analysis, compute and feature RSI prominently.

### Reporting

- **RSI(14) daily** — base reading
- **RSI(14) weekly** — multi-week-horizon view
- Compute for both the **individual ticker** and its **sector/index parent** (e.g., NVDA + SMH; META + QQQ)
- **Always label timeframe explicitly** — daily and weekly RSI can differ by 5–10+ points; never write a bare number.
- Use **≥2y of price history** for weekly RSI; Wilder smoothing needs convergence room.

### Interpretation

| Reading | Standard meaning | Real-world caveat |
|---|---|---|
| RSI > 70 | Overbought | Momentum stocks hold 70–85 for weeks during strong runs — don't auto-fade |
| RSI < 30 | Oversold | More reliable mean-reversion signal than the overbought side |
| Weekly RSI > 80 (index) | Late-cycle | Rarer; historically marks meaningful tops |
| Divergence | Highest-quality signal | Price new high, RSI not (bearish); or price new low, RSI not (bullish) — always check |

### Compute (clean snippet)

```python
def rsi(series, period=14):
    delta = series.diff()
    gain = delta.where(delta > 0, 0.0)
    loss = -delta.where(delta < 0, 0.0)
    avg_gain = gain.ewm(alpha=1/period, adjust=False, min_periods=period).mean()
    avg_loss = loss.ewm(alpha=1/period, adjust=False, min_periods=period).mean()
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

daily_rsi  = rsi(hist["Close"]).iloc[-1]
weekly_rsi = rsi(hist["Close"].resample("W-FRI").last()).iloc[-1]
```

## Other indicators to pair with RSI

- 200-day MA distance (% above/below)
- Drawdown from 52-week high
- Trailing 1Y / YTD return vs historical distribution
- Shiller CAPE for broad-market valuation context
- AAII bullish % for sentiment

RSI is featured but never solo. The cluster of signals is what matters.

## Workflow rule: discuss before writing

For analysis tasks, *think and refine in conversation first.* Only commit to a document once positions, account constraints, and the framework are settled. No rushed writeups.

## Related notes

- **[watch-loop-architecture.md](./watch-loop-architecture.md)** — the operational framework that uses these conventions (tier system, asymmetric watch, decision authority, cadences)
- **[historical-bear-analog-2021-2022.md](./historical-bear-analog-2021-2022.md)** — example application of these methods: how Wilder RSI + bearish divergence pattern signaled the 2021 top
- **[README.md](./README.md)** — index of all finance notes
