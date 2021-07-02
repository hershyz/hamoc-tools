import hamoc_api as hamocapi

client = hamocapi.Hamoc_Client("http://127.0.0.1:5000") # intiialze the client

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