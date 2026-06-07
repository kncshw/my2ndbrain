#!/usr/bin/env python3
"""
daily_brief.py — deterministic compute block for the morning-brief routine.

Prints a DATA BLOCK (indicators, RSI, spots, loss scenarios, hedge + payoff) that the
morning-brief agent composes into the brief. The agent picks the hedge style from
notes/finance/brief-config.md HEDGE SPEC and passes it here:
  near-term / DEFENSIVE  -> --otm 0.05 --dte 14
  longer-dated / NEUTRAL -> --otm 0.10 --dte 45

Deps: yfinance (pip install yfinance). Stdlib math only otherwise.
Usage: python3 scripts/daily_brief.py [--otm 0.05] [--dte 14] [--port 400000]
"""
import math, datetime as dt, argparse
import yfinance as yf

# Loss scenarios (GOOGL / SEMI / OTHERS drop %). Edit here to change the loss table.
SCEN = {'S1_Pullback': (-.10, -.15, -.10),
        'S2_SemiLed':  (-.12, -.22, -.10),
        'S3_2022Bear': (-.22, -.35, -.20)}
RSI_TICKERS   = ['GOOGL', 'SMH', 'QQQ']
SPOT_TICKERS  = ['GOOGL', 'SMH', 'NVDA', 'INTC', 'CSCO', 'MU', 'QQQ']
HEDGE_TICKERS = ['SMH', 'GOOGL']


def wrsi(c, p=14):
    """Wilder RSI; c = closes oldest->newest. Returns latest."""
    c = list(c)
    if len(c) < p + 1:
        return None
    d = [c[i] - c[i - 1] for i in range(1, len(c))]
    g = [max(x, 0.0) for x in d]
    l = [max(-x, 0.0) for x in d]
    ag = sum(g[:p]) / p
    al = sum(l[:p]) / p
    for i in range(p, len(d)):
        ag = (ag * (p - 1) + g[i]) / p
        al = (al * (p - 1) + l[i]) / p
    return 100.0 if al == 0 else 100 - 100 / (1 + ag / al)


def ncdf(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def bsput(S, K, T, r, s):
    if T <= 0 or s <= 0:
        return max(K - S, 0.0)
    d1 = (math.log(S / K) + (r + 0.5 * s * s) * T) / (s * math.sqrt(T))
    d2 = d1 - s * math.sqrt(T)
    return K * math.exp(-r * T) * ncdf(-d2) - S * ncdf(-d1)


def px(t):
    return float(yf.Ticker(t).history(period='5d')['Close'].iloc[-1])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--otm', type=float, default=0.05, help='put % out-of-the-money (0.05 = 5%)')
    ap.add_argument('--dte', type=int, default=14, help='target days to expiry')
    ap.add_argument('--port', type=float, default=400000, help='total portfolio $')
    a = ap.parse_args()

    vix, tnx, wti = px('^VIX'), px('^TNX'), px('CL=F')
    r = tnx / 100
    print(f'INDICATORS VIX {vix:.1f} | 10Y {tnx:.2f}% | WTI ${wti:.2f}')

    print('RSI Wilder-14 (daily | weekly):')
    for t in RSI_TICKERS:
        dc = yf.Ticker(t).history(period='1y')['Close']
        wc = yf.Ticker(t).history(period='3y', interval='1wk')['Close'].dropna()
        print(f'  {t}: {wrsi(dc.values):.1f} | {wrsi(wc.values):.1f}')

    for t in SPOT_TICKERS:
        print(f'SPOT {t} ${px(t):.2f}')

    B = a.port / 3
    for nm, (g, s, o) in SCEN.items():
        lg, ls, lo = B * g, B * s, B * o
        tot = lg + ls + lo
        print(f'{nm} GOOGL {g*100:.0f}% ${lg:,.0f} SEMI {s*100:.0f}% ${ls:,.0f} '
              f'OTH {o*100:.0f}% ${lo:,.0f} TOTAL ${tot:,.0f} ({tot/a.port*100:.1f}%)')

    def hedge(t):
        tk = yf.Ticker(t)
        spot = px(t)
        tgt = spot * (1 - a.otm)
        today = dt.date.today()
        exp = min(tk.options, key=lambda e: abs((dt.date.fromisoformat(e) - today).days - a.dte))
        dte = (dt.date.fromisoformat(exp) - today).days
        T = max(dte, 1) / 365
        p = tk.option_chain(exp).puts
        row = p.iloc[(p['strike'] - tgt).abs().argmin()]
        K = float(row['strike'])
        bid = float(row.get('bid', 0) or 0)
        ask = float(row.get('ask', 0) or 0)
        mid = (bid + ask) / 2 if (bid and ask) else float(row.get('lastPrice', 0) or 0)
        iv = float(row.get('impliedVolatility', 0) or 0)
        ct = round(B / (spot * 100))
        print(f'HEDGE {t}: buy {ct}x {K:.0f}p exp {exp} ({dte}d) @ ${mid:.2f} '
              f'cost ${mid*100*ct:,.0f} (spot ${spot:.2f} IV {iv*100:.0f}%)')
        for dp in (0.05, 0.10, 0.15):
            val = bsput(spot * (1 - dp), K, T, r, iv)
            gain = (val - mid) * 100 * ct
            print(f'   {t} -{dp*100:.0f}%: put ~${val:.2f} hedge gain ~${gain:,.0f}')

    for t in HEDGE_TICKERS:
        hedge(t)


if __name__ == '__main__':
    main()
