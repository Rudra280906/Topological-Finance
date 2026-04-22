import yfinance as yf
import pandas as pd

tickerStrings = ['SPY', 'QQQ', 'SVIX', 'UVIX', 'FNGU', 'TQQQ']
df_list = []
for ticker in tickerStrings:
    data = yf.download(ticker, group_by="Ticker", period='2y')
    data['ticker'] = ticker
    pd.DataFrame.to_csv(data, "Topological-Finance/data/%s.csv" % ticker)