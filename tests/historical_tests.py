import yfinance as yf

msft = yf.Ticker("MSFT") # use microsoft symbol as an example for tests
# print(msft.info)

hist = msft.history(period="max") # pandas dataframe object, we are interested in open, high, low, and close price values
# print(hist)

print("--------------------------------------------------")

hist_range = msft.history(start="2021-01-01", end="2021-01-10") # fetching historical data from a range, probably will be more useful this way, note that there are not data points for every single day
print(hist_range)
