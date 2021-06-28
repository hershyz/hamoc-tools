import yfinance as yf
import util

def store(symbol):
    stock = yf.Ticker(symbol)
    hist = stock.history(period="max")
    hist.to_csv("stocks/" + symbol + ".csv")

def get_property(symbol, date, prop):
    lines = util.read("stocks/" + symbol + ".csv")
    properties = lines[0].split(",")

    for line in lines:
        arr = line.split(",")
        if arr[0] == date:
            for i in range(len(properties)):
                if properties[i].lower() == prop.lower():
                    return arr[i]
    
    return "error: could not read property"