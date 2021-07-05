import requests

# api wrapper:
class Hamoc_Client:    
    
    def __init__(self, uri):
        self.uri = uri

    def add_symbols(self, symbols):
        payload = {
            "symbols": symbols
        }
        r = requests.post(self.uri + "/add_symbols", json=payload)
        return r.text

    def get_symbols(self):
        r = requests.get(self.uri + "/get_symbols")
        return r.text

    def del_symbols(self, symbols):
        payload = {
            "symbols": symbols
        }
        r = requests.post(self.uri + "/del_symbols", json=payload)
        return r.text

    def update_stock_data(self):
        r = requests.get(self.uri + "/stock_store")
        return r.text

    def update_options_data(self):
        r = requests.get(self.uri + "/options_store")
        return r.text

    def get_stock_val(self, symbol, date, prop):
        payload = {
            "symbol": symbol,
            "date": date,
            "property": prop
        }
        r = requests.get(self.uri + "/stock_search", json=payload)
        return r.text

    def get_contract_symbols(self, symbol, date):
        payload = {
            "symbol": symbol,
            "date": date
        }
        r = requests.get(self.uri + "/contract_symbols", json=payload)
        return r.text

    def get_contract_property(self, symbol, contract_symbol, date, prop):
        payload = {
            "symbol": symbol,
            "contract_symbol": contract_symbol,
            "date": date,
            "property": prop
        }
        r = requests.get(self.uri + "/contract_search", json=payload)
        return r.text

    def stock_query(self, low, high):
        payload = {
            "low_price": low,
            "high_price": high
        }
        r = requests.get(self.uri + "/stock_price_query", json=payload)
        return r.text

    def option_query(self, low, high, prop):
        payload =  {
            "low": low,
            "high": high,
            "property": prop
        }
        r = requests.get(self.uri + "/option_query", json=payload)
        return r.text


# client:
def show_help():
    print("help:                                                               displays all available commands")
    print("add [symbols]:                                                      adds symbols to the server target list")
    print("getsymbols:                                                         returns a list of symbols from the target list")
    print("del [symbols]:                                                      deletes symbols from the server target list")
    print("updatestocks:                                                       attempts to update stock data")
    print("updateoptions:                                                      attempts to update options data")
    print("getstockval [symbol, YYYY-MM-DD, property]:                         returns the property of a stock given a symbol and date")
    print("contracts [symbol, YYYY-MM-DD]:                                     returns all contracts of a given stock on a specific date")
    print("getcontractval [symbol, contract symbol, YYYY-MM-DD, prpoerty]:     returns the property of a contract symbol given a date")


def command_loop():

    client = Hamoc_Client("http://127.0.0.1:5000")

    raw_command = input("> ")
    command_arr = raw_command.split(" ")
    command = command_arr[0].lower()

    # help command
    if command == "help":
        show_help()
    
    # add command
    if command == "add":
        symbols = []
        i = 1
        while i < len(command_arr):
            symbols.append(command_arr[i])
            i += 1
        print(client.add_symbols(symbols))

    # getsymbols command
    if command == "getsymbols":
        print(client.get_symbols())
    
    # del command:
    if command == "del":
        symbols = []
        i = 1
        while i < len(command_arr):
            symbols.append(command_arr[i])
            i += 1
        print(client.del_symbols(symbols))
    
    # updatestocks command:
    if command == "updatestocks":
        print(client.update_stock_data())
    
    # updateoptions command:
    if command == "updateoptions":
        print(client.update_options_data())

    # getstockval command:
    if command == "getstockval":
        symbol = command_arr[1]
        date = command_arr[2]
        prop = command_arr[3]
        print(client.get_stock_val(symbol, date, prop))
    
    # contracts command:
    if command == "contracts":
        symbol = command_arr[1]
        date = command_arr[2]
        print(client.get_contract_symbols(symbol, date))

    # getcontractval command:
    if command == "getcontractval":
        symbol = command_arr[1]
        contract_symbol = command_arr[2]
        date = command_arr[3]
        prop = command_arr[4]
        print(client.get_contract_property(symbol, contract_symbol, date, prop))

    

    command_loop()


print("Hamoc CLI - enter 'help' for a list of all available commands")
command_loop()