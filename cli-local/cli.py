import sys
import help_message
import stocks
import options
import util

args = sys.argv

if len(args) < 2:
    help_message.show()
    exit()

for i in range(len(args)):
    args[i] = args[i].lower()

command = args[1].lower()
# command = args[1]
# arg1    = args[2]
# arg2    = args[3]
# etc...

if command == "help":
    help_message.show()

if command == "stock_store":
    stocks.store(args[2], args[3], args[4])

if command == "stock_lookup":
    print(stocks.lookup(args[2], args[3]))

if command == "options_store":
    options.store(args[2], args[3])

if command == "calc_profits":
    
    symbol = args[2]
    start = args[3]
    end = args[4]
    investment = args[5]
    
    start_price = stocks.lookup(symbol, start)
    end_price = stocks.lookup(symbol, end)
    ratio = float(end_price) / float(start_price)
    current = float(investment) * ratio
    profit = current - float(investment)

    print("initial investment:  " + investment)
    print("current value:       " + str(current))
    print("profit:              " + str(profit))

if command == "volatility":

    symbol = args[2]
    lines = util.read(symbol + ".csv")
    total = 0
    volatility_total = 0

    i = 2
    while i < len(lines):
        current_volatility = float(util.parse_csv_generic(lines, i, "Close")) - float(util.parse_csv_generic(lines, i - 1, "Close"))
        current_volatility = abs(current_volatility)
        volatility_total += current_volatility
        i += 1
        total += 1

    print(str(volatility_total / total) + " -> average change per day")
