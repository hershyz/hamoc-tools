import yfinance as yf
import sys

# args[1] = symbol
# args[2] = date
args = sys.argv

stock = yf.Ticker(args[1])
opt = stock.option_chain(date=args[2])
print(opt.calls)

call_options = opt.calls
csv_path = args[1] + "-" + args[2] + ".csv"
call_options.to_csv(csv_path)

f = open(csv_path, 'r')
lines = []
raw = f.readlines()
for line in raw:
    line = line.replace("\n", "")
    lines.append(line)

lines[0] = "num" + lines[0]

f = open(csv_path, 'w')
for line in lines:
    f.write(line + "\n")
f.close()