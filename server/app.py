from flask import Flask, request
from threading import Thread
import util
import stocks
import options
import scheduler

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

    return "stocks updated: " + str(symbols)


# scheduled option data storing (updated from client)
@app.route("/options_store", methods=["GET"])
def options_store():
    symbols = util.read("symbols.txt")
    for symbol in symbols:
        options.store(symbol)
    
    return "options updated: " + str(symbols)


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

    try:
        lines = util.read("options/" + filename)
        contract_symbols = []
        
        i = 1
        while i < len(lines):
            arr = lines[i].split(",")
            contract_symbols.append(arr[1])
            i += 1
    except:
        files = util.get_files("/options")
        valid = []
        for f in files:
            str_f = str(f)
            symbol = str_f.split("---")[0]
            date = str_f.split("---")[2]
            date = str.replace(date, ".csv", "")
            valid.append(symbol + "," + date)
        return "stored option chains: " + str(valid)
        
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

    return "could not find property, valid contract properties: contractSymbol,lastTradeDate,strike,lastPrice,bid,ask,change,percentChange,volume,openInterest,impliedVolatility,inTheMoney,contractSize,currency"


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
    low_bound = float(data['low'])
    high_bound = float(data['high'])
    prop = data['property']
    property_index = options.get_property_index(prop)

    if property_index == -1:
        return "incorrect paramters, valid option query properties are: strike,lastPrice,bid,ask,change,percentChange,volume,openInterest,impliedVolatility"

    files = util.get_files("/options")
    results = []

    for f in files:
        try:
            lines = util.read("options/" + f)
            i = 1
            while i < len(lines):
                arr = lines[i].split(",")
                val = float(arr[property_index])
                if val >= low_bound and val <= high_bound:
                    results.append(arr[1])
                i += 1
        except:
            return "incorrect paramters, valid option query properties are: strike,lastPrice,bid,ask,change,percentChange,volume,openInterest,impliedVolatility"

    return str(results)


if __name__ == "__main__":
    t2 = Thread(target = app.run)
    t2.setDaemon(True)
    t2.start()
    t1 = Thread(target = scheduler.init("http://127.0.0.1:5000"))
    t1.setDaemon(True)
    t1.start()
    # app.run()