from flask import Flask, request
import util

app = Flask(__name__)

@app.route("/add_symbols", methods=["POST"])
def add_symbols():
    data = request.get_json()
    symbols = data['symbols']
    storage = open("symbols.txt", "a")
    lines = util.read("symbols.txt")
    unique = []

    for symbol in symbols:
        if symbol not in unique:
            unique.append(symbol)

    for symbol in unique:
        if symbol not in lines:
            storage.write(symbol + "\n")

    return "recieved: " + str(symbols)

if __name__ == "__main__":
    app.run()