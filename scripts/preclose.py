#!/usr/bin/env python3
"""
preclose.py — compute block for the BEFORE-CLOSE reminder (12:00pm PT).
Prints VIX / 10Y / WTI and which watchlist names report AFTER CLOSE (AMC) today + this week.
Deps: yfinance + lxml (lxml needed for get_earnings_dates). Usage: python3 scripts/preclose.py
"""
import datetime as dt
import yfinance as yf

# Holdings + market-movers whose earnings gap SMH/QQQ (ETFs excluded — no earnings).
WATCH = ['GOOGL', 'NVDA', 'INTC', 'CSCO', 'MU', 'AVGO', 'TSM', 'AMD',
         'AAPL', 'MSFT', 'META', 'AMZN', 'ORCL', 'ADBE']


def px(t):
    return float(yf.Ticker(t).history(period='5d')['Close'].iloc[-1])


def main():
    vix, tnx, wti = px('^VIX'), px('^TNX'), px('CL=F')
    print(f'INDICATORS VIX {vix:.1f} | 10Y {tnx:.2f}% | WTI ${wti:.2f}')

    today = dt.date.today()
    wk_end = today + dt.timedelta(days=7)
    amc_today, amc_week = [], []
    for t in WATCH:
        try:
            ed = yf.Ticker(t).get_earnings_dates(limit=12)
            for ix in ed.index:
                d = ix.date()
                if ix.hour >= 16:  # 16:00 ET marks an after-close (AMC) report
                    if d == today:
                        amc_today.append(t)
                    elif today < d <= wk_end:
                        amc_week.append(f'{t} {d.strftime("%a %m-%d")}')
        except Exception:
            pass

    print('AMC_TODAY: ' + (', '.join(sorted(set(amc_today))) if amc_today else 'none'))
    print('AMC_THIS_WEEK: ' + (', '.join(dict.fromkeys(amc_week)) if amc_week else 'none'))

    # --- DATA SANITY CHECK (flag stale/null indicator feed) ---
    warns = []
    try:
        idx = yf.Ticker('^VIX').history(period='5d').index
        age = (today - idx[-1].date()).days
        if age > 4:
            warns.append('stale feed? last VIX bar %s (%dd old)' % (idx[-1].date(), age))
    except Exception:
        warns.append('could not verify data freshness')
    for nm, v in [('VIX', vix), ('10Y', tnx), ('WTI', wti)]:
        if v is None or v != v or v <= 0:
            warns.append('%s invalid (%s)' % (nm, v))
    print('DATA_CHECK: ' + ('WARN - ' + '; '.join(warns) if warns else 'OK'))


if __name__ == '__main__':
    main()
