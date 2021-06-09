import yfinance as yf
import sys

args = sys.argv



def get_data(symbol, _start, _end):
    stock = yf.Ticker(symbol)
    hist = stock.history(start=_start, end=_end)
    print(hist)
    print("------------------------------------------------------")





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
        print(symbol)
        print("------------------------------------------------------")
        get_data(symbol, start, end)




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
        print(symbols[i])
        print("------------------------------------------------------")
        get_data(symbols[i], starts[i], ends[i])