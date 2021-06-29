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


# fetching stock data:
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


# contract search:
@app.route("/contract_search", methods=["GET"])
def contract_search():
    data = request.get_json()
    contract_symbol = data['contract_symbol']
    date = data['date']

if __name__ == "__main__":
    app.run()