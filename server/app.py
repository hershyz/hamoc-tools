from flask import Flask, request
import util
import stocks
import options

app = Flask(__name__)

# endpoints:
# add symbols:
@app.route("/add_symbols", methods=["POST"])
def add_symbols():
    data = request.get_json()
    symbols = data['symbols']
    storage = open("symbols.txt", "a")
    lines = util.read("symbols.txt")
    unique = []
    added = []

    for symbol in symbols:
        if symbol not in unique:
            unique.append(symbol)

    for symbol in unique:
        if symbol not in lines:
            storage.write(symbol + "\n")
            added.append(symbol)

    return "added: " + str(added)


# get symbols
@app.route("/get_symbols", methods=["GET"])
def get_symbols():
    symbols = util.read("symbols.txt")
    return str(symbols)


# delete symbols
@app.route("/del_symbols", methods=["POST"])
def del_symbols():
    data = request.get_json()
    symbols = data['symbols']
    existing_symbols = util.read("symbols.txt")
    for symbol in symbols:
        existing_symbols.remove(symbol)
    overwrite = open("symbols.txt", "w")
    overwrite.write("")
    overwrite.close()
    add_symbols = open("symbols.txt", "a")
    for symbol in existing_symbols:
        add_symbols.write(symbol + "\n")
    return "new symbol list: " + str(existing_symbols)


# scheduled stock data storing (updated from client)
@app.route("/stock_store", methods=["GET"])
def stock_store():
    symbols = util.read("symbols.txt")
    for symbol in symbols:
        stocks.store(symbol)

    return "updated: " + str(symbols)


# scheduled option data storing (updated from client)
@app.route("/options_store", methods=["GET"])
def options_store():
    symbols = util.read("symbols.txt")
    for symbol in symbols:
        options.store(symbol)
    
    return "updated: " + str(symbols)


# gets the value of a specific property of a stock:
@app.route("/stock_search", methods=["GET"])
def stock_search():
    data = request.get_json()
    symbol = data['symbol']
    date = data['date']
    prop = data['property']
    return stocks.get_property(symbol, date, prop)


# fetch contract symbols:
@app.route("/contract_symbols", methods=["GET"])
def contract_symbols():
    data = request.get_json()
    symbol = data['symbol']
    date = data['date']
    filename = symbol + "---option---" + date + ".csv"
    lines = util.read("options/" + filename)
    contract_symbols = []
    
    i = 1
    while i < len(lines):
        arr = lines[i].split(",")
        contract_symbols.append(arr[1])
        i += 1

    return str(contract_symbols)


# get properties given a contract symbol:
@app.route("/contract_search", methods=["GET"])
def contract_search():

    data = request.get_json()
    symbol = data['symbol']
    contract_symbol = data['contract_symbol']
    date = data['date']
    prop = data['property']
    lines = util.read("options/" + symbol + "---option---" + date + ".csv")
    property_line_arr = lines[0].split(",")
    property_line_arr.insert(0, "row")
    property_line_arr.remove("")

    i = 1
    while i < len(lines):
        arr = lines[i].split(",")
        if arr[1] == contract_symbol:
            for j in range(len(property_line_arr)):
                if property_line_arr[j].lower() == prop.lower():
                    return arr[j]
        i += 1

    return "could not find property"


# stock price query endpoint, finds all stocks (stored on the server-side) within the given close price range:
@app.route("/stock_price_query", methods=["GET"])
def stock_price_query():
    
    data = request.get_json()
    low_price = float(data['low_price'])      # lower price bound
    high_price = float(data['high_price'])    # higher price bound
    symbols = util.read("symbols.txt")
    results = []

    # arr[4] -> close price
    # arr[0] -> date
    for symbol in symbols:
        lines = util.read("stocks/" + symbol + ".csv")
        i = 1
        while i < len(lines):
            curr_arr = lines[i].split(",")
            curr_close = float(curr_arr[4])
            if curr_close <= high_price and curr_close >= low_price:
                results.append(symbol + "," + curr_arr[0])
            i += 1
    
    return str(results)


# option query endpoint, finds all contract symbols that fall within the given property range:
@app.route("/option_query", methods=["GET"])
def option_query():

    data = request.get_json()
    low_bound = data['low']
    high_bound = data['high']
    prop = data['property']
    results = []

    # arr[0] -> row number (not important)
    # arr[1] -> contract symbol
    # arr[2] -> date (not important)
    # arr[3] -> strike
    # arr[4] -> last price
    # arr[5] -> bid
    # arr[6] -> ask
    # arr[7] -> change
    # arr[8] -> percent change
    # arr[9] -> volume
    # arr[10] -> open interest
    # arr[11] -> implied volatility

    

if __name__ == "__main__":
    app.run()