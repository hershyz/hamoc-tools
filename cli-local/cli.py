import sys
import help_message
import stocks

args = sys.argv

if len(args) < 2:
    help_message.show()
    exit()

for i in range(len(args)):
    args[i] = args[i].lower()

command = args[1]

if command == "help":
    help_message.show()

if command == "stock_store":
    stocks.store(args[2], args[3], args[4])

if command == "stock_lookup":
    print(stocks.lookup(args[2], args[3]))