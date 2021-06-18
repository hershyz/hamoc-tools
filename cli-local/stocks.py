import yfinance as yf
import util

def store(symbol, start_date, end_date):
    stock = yf.Ticker(symbol)
    hist = stock.history(start=start_date, end=end_date)
    hist.to_csv(symbol + ".csv")

def lookup(symbol, date):
    lines = util.read(symbol + ".csv")
    # date = 0, close = 4
    for i in range(len(lines)):
        arr = lines[i].split(",")
        if arr[0] == date:
            return arr[4]