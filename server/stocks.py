import yfinance as yf
import os

def store(symbol):
    stock = yf.Ticker(symbol)
    hist = stock.history(period="max")
    hist.to_csv("stocks/" + symbol + ".csv")
