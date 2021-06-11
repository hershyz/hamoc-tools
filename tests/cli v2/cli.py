import yfinance as yf
import pandas as pd
import sys
from datetime import date, timedelta

args = sys.argv

# returns pandas dataframe of the stock data:
def get_data(symbol, _start, _end):
    stock = yf.Ticker(symbol)
    hist = stock.history(start=_start, end=_end)
    # print(hist)
    # print("------------------------------------------------------")
    return hist



# filters dates from other strings, returns true if the input string is a date:
def filter(s):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    ALPHA = alpha.upper()
    
    for c in alpha:
        if c in s:
            return False
    
    for C in ALPHA:
        if C in s:
            return False
    
    return True


# stores the dataframe into the csv file:
def store_dataframe(df):

    '''
    did not realize that you could convert pandas dataframes to csv files, keeping this code because having an array of dates (from start to end) might be useful
    y1 = int(start.split("-")[0])
    m1 = int(start.split("-")[1])
    d1 = int(start.split("-")[2])

    y2 = int(end.split("-")[0])
    m2 = int(end.split("-")[1])
    d2 = int(end.split("-")[2])

    sdate = date(y1, m1, d1)
    edate = date(y2, m2, d2)

    range = pd.date_range(sdate,edate-timedelta(days=1),freq='d')
    raw = str.replace(str(range), "DatetimeIndex", "")
    raw = str.replace(raw, "(", "")
    raw = str.replace(raw, ")", "")
    raw = str.replace(raw, "[", "")
    raw = str.replace(raw, "]", "")
    raw = str.replace(raw, "'", "")
    raw = str.replace(raw, " ", "")

    raw_arr = str(raw).split(",")
    dates_arr = []

    for term in raw_arr:
        term.strip()
        term = str.replace(term, "\n", "")
        if filter(term):
            dates_arr.append(term)
    '''

    df.to_csv('data.csv')


# format: cli input symbol1 symbol3 symbol3.... start end
if args[1].lower() == "input":

    symbols = []
    start = args[len(args) - 2]
    end = args[len(args) - 1]
    
    i = 2
    while i < len(args) - 2:
        symbols.append(args[i].upper())
        i+=1

    for symbol in symbols:
        hist = get_data(symbol, start, end)
        store_dataframe(hist)


# format:        cli parse (csv)
# csv format:    symbol, start, end
if args[1].lower() == "parse":

    f = open(args[2], 'r')
    lines = []
    raw = f.readlines()
    for line in raw:
        line = line.replace("\n", "")
        lines.append(line)

    symbols = []
    starts = []
    ends = []

    for line in lines:
        arr = line.split(",")
        symbols.append(arr[0].upper())
        starts.append(arr[1].upper())
        ends.append(arr[2].upper())

    for i in range(len(symbols)):
        hist = get_data(symbols[i], starts[i], ends[i])
        store_dataframe(hist)