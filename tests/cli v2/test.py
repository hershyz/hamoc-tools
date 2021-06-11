import yfinance as yf

stock = yf.Ticker("GOOG")
hist = stock.history(start="2021-01-01", end="2021-06-10")
hist.to_csv('test.csv')