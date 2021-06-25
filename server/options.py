import yfinance as yf

def store(symbol):
    stock = yf.Ticker(symbol)
    dates = list(stock.options)
    opt = stock.option_chain(str(dates[0]))
    calls = opt.calls
    calls.to_csv("options/" + symbol + "---option---" + dates[0] + ".csv")