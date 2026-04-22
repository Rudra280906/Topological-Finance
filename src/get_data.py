import yfinance as yf
import pandas as pd
import numpy as np

tickerStrings = ['SPY']
df_list = []

def transform(data):
    returns = np.log(data['Close'] / data['Close'].shift(1))
    volatility = np.std(returns)
    u = np.exp(volatility)
    d = np.exp(-volatility)
    print(u)
    print(d)


for ticker in tickerStrings:
    data = yf.download(ticker, group_by="Ticker", period='2y', auto_adjust=False)
    data.columns = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    data['ticker'] = ticker
    print(data)
    pd.DataFrame.to_csv(data, "Topological-Finance/data/%s.csv" % ticker)
    transform(data)
