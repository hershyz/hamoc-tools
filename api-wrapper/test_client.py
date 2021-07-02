import hamoc_api as hamocapi

client = hamocapi.Hamoc_Client("http://127.0.0.1:5000") # intiialze the client

# ctrl + / in vscode to uncomment any block below:

# add symbols
# print(client.add_symbols(["ibm", "amzn"]))

# get symbols:
# print(client.get_symbols())

# delete symbols:
# print(client.del_symbols(["ibm", "amzn"]))

# update stock data:
# print(client.update_stock_data())

# update options data:
# print(client.update_options_data())

# get stock values:
# symbol = "avgo"
# date = "2021-06-04"
# prop = "close"
# print(client.get_stock_val(symbol, date, prop))

# fetch contract symbols on a given date:
# symbol = "avgo"
# date = "2021-06-25"
# print(client.get_contract_symbols(symbol, date))

# fetch contract properties:
# symbol = "aapl"
# contract_symbol = "AAPL210625C00080000"
# date = "2021-06-25"
# prop = "strike"
# print(client.get_contract_property(symbol, contract_symbol, date, prop))

# stock price query:
# low = 2000
# high = 2100
# print(client.stock_query(low, high))