import yfinance as yf

def store(symbol):
    stock = yf.Ticker(symbol)
    dates = list(stock.options)
    opt = stock.option_chain(str(dates[0]))
    calls = opt.calls
    calls.to_csv("options/" + symbol + "---option---" + dates[0] + ".csv")


# arr[0] -> row number (not important)
# arr[1] -> contract symbol
# arr[2] -> date (not important)
# arr[3] -> strike
# arr[4] -> last price
# arr[5] -> bid
# arr[6] -> ask
# arr[7] -> change
# arr[8] -> percent change
# arr[9] -> volume
# arr[10] -> open interest
# arr[11] -> implied volatility

def get_property_index(prop):
    if prop == "row_number":
        return 0
    if prop == "contract_symbol":
        return 1
    if prop == "date":
        return 2
    if prop == "strike":
        return 3
    if prop == "last_price":
        return 4
    if prop == "bid":
        return 5
    if prop == "ask":
        return 6
    if prop == "change":
        return 7
    if prop == "percent_change":
        return 8
    if prop == "volume":
        return 9
    if prop == "open_interest":
        return 10
    if prop == "implied_volatility":
        return 11
    else:
        return -1