<h1>API Wrapper</h1>

<p>
  The <a href="https://github.com/hershyz/hamoc-tools/blob/main/api-wrapper/hamoc_api.py">API wrapper</a> is simply designed to build JSON requsts from function paramters, making requests to server endpoints through a Python class.<br>
  Each function in the API wrapper returns a server response, so every call can be printed to the console for debugging or user purposes.
</p>

<table>
<thead>
  <tr>
    <th>Method</th>
    <th>Parameters</th>
    <th>Purpose</th>
    <th>Target Endpoint</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>add_symbols()</td>
    <td>symbols (array)</td>
    <td>add symbols to the server's target list</td>
    <td>/add_symbols</td>
  </tr>
  <tr>
    <td>get_symbols()</td>
    <td>none</td>
    <td>get all symbols in the server's target list</td>
    <td>/get_symbols</td>
  </tr>
  <tr>
    <td>del_symbols()</td>
    <td>symbols (array)</td>
    <td>delete symbols from the server's target list</td>
    <td>/get_symbols</td>
  </tr>
  <tr>
    <td>update_stock_data()</td>
    <td>none</td>
    <td>update stock data on the server</td>
    <td>/stock_store</td>
  </tr>
  <tr>
    <td>update_options_data()</td>
    <td>none</td>
    <td>update options data on the server</td>
    <td>/options_store</td>
  </tr>
  <tr>
    <td>get_stock_val()</td>
    <td>symbol (string), date (string &gt; YYYY-MM-DD), property (string)</td>
    <td>get the value of a specific property of a stock</td>
    <td>/stock_search</td>
  </tr>
  <tr>
    <td>get_contract_symbols()</td>
    <td>symbol (string), date (string &gt; YYYY-MM-DD)</td>
    <td>fetch contract symbols (call options) of a given stock<br>on any specific date</td>
    <td>/contract_symbols</td>
  </tr>
  <tr>
    <td>get_contract_property()</td>
    <td>symbol (string), contract symbol (string), date ( string &gt; YYYY-MM-DD),<br>property (string)</td>
    <td>fetch contract (call option) properties</td>
    <td>/contract_search</td>
  </tr>
  <tr>
    <td>stock_query()</td>
    <td>low (float), high (float)</td>
    <td>query stocks based on close price (high and low bound)</td>
    <td>/stock_price_query</td>
  </tr>
  <tr>
    <td>option_query()</td>
    <td>low (float), high (float), property (string)</td>
    <td>query options based on a<br>specific property (high and low bound)</td>
    <td>/option_query</td>
  </tr>
</tbody>
</table>

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
