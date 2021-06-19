import yfinance as yf

def store(symbol, expiration_date):
    stock = yf.Ticker(symbol)
    opt = stock.option_chain(expiration_date)
    calls = opt.calls
    calls.to_csv(symbol + "-option-" + expiration_date + ".csv")
