import yfinance as yf
import sys

# args[1] = symbol
# args[2] = date
args = sys.argv

stock = yf.Ticker(args[1])
opt = stock.option_chain(date=args[2])
print(opt.calls)

call_options = opt.calls
call_options.to_csv(args[1] + "-" + args[2] + ".csv")
