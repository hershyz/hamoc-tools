<h1>API Wrapper</h1>

<p>
  The <a href="https://github.com/hershyz/hamoc-tools/blob/main/api-wrapper/hamoc_api.py">API wrapper</a> is simply designed to build JSON requsts from function paramters, making requests to server endpoints through a Python class.<br>
  Each function in the API wrapper returns a server response, so every call can be printed to the console for debugging or user purposes.
</p>

<br>

<p><strong>Using All API Functions</strong></p>

```python
# start by importing and constructing the client to the default uri:
import hamoc_api
client = Hamoc_Client("http://hershyz.pythonanywhere.com")

# add an array of symbols to the server's target list:
new_symbols = ["amzn", "ibm"]
client.add_symbols(new_symbols)

# get all the symbols in the server's target list:
print(client.get_symbols())

# delete the symbols we just added:
symbols_to_remove = ["amzn", "ibm"]
client.del_symbols(symbols_to_remove)

# update stocks and options data (the scheduler on the server already does this every 12 hours):
client.update_stocks_data()
client.update_options_data()

# get the value of a property of a stock:
symbol = "aapl"
date = "2021-06-24"
property = "close"
print(client.get_stock_val(symbol, date, property)

# find all contract symbols for a given stock on a specific date:
symbol = "tsla"
date = "2021-06-25"
print(client.get_contract_symbols(symbol, date))

# find the value of a specific contract:
symbol = "aapl"
contract_symbol = "AAPL210625C00080000"
date = "2021-06-25"
property = "strike"
print(client.get_contract_property(symbol, contract_symbol, date, property))

# find all stocks with a close price within an interval:
low = 2500
high = 2700
print(client.stock_query(low, high))

# find all contract symbols with a strike price within an interval:
low = 2500
high = 2700
property = "strike"
print(client.option_query(low, high, prop))
```
