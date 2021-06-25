import yfinance as yf

def store(symbol):
    stock = yf.Ticker(symbol)
    print(stock.options)