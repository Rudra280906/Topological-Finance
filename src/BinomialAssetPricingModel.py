import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

tickers = {'SPY': 0, 'QQQ': 0}
simulated_prices = {}
df_list = []

def BinomialAssetPricingModel(S_0, ticker, u, d, r, n):
    S_n = S_0
    risk_neutral_p = (1+r-d)/(u-d)
    for i in range(1, n+1):
        outcome = ""
        X = random.random() #Random Variable that outputs something between 0 and 1
        if X <= risk_neutral_p:
            S_n *= u
            outcome = "H"
        else:
            S_n *= d
            outcome = "T"
    return S_n
def transform(data):
    returns = np.log(data['Close'] / data['Close'].shift(1))
    volatility = np.std(returns)
    u = np.exp(volatility)
    d = np.exp(-volatility)
    return u, d

for ticker in tickers.keys():
    data = yf.download(ticker, group_by="Ticker", period='5y', auto_adjust=False)
    data.columns = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    data['ticker'] = ticker
    pd.DataFrame.to_csv(data, "Topological-Finance/data/%s.csv" % ticker)
    values = transform(data)
    tickers[ticker] = (values[0], values[1])

for i in range(10000):
    ticker = 'SPY'
    t = BinomialAssetPricingModel(100, ticker, tickers[ticker][0], tickers[ticker][1], 0, 50)
    if t in simulated_prices.keys():
        simulated_prices[t] += 1
    else:
        simulated_prices[t] = 1

for price in simulated_prices.keys():
    plt.scatter(price, simulated_prices[price])
plt.show()