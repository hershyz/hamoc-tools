import yfinance as yf

msft = yf.Ticker("MSFT")
opt = msft.option_chain(date="2021-06-18") # options with said expiration date

print(opt.calls)
print(opt.puts)
