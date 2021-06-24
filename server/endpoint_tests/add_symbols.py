import requests

symbols = []
symbols.append("goog")
symbols.append("tsla")
symbols.append("msft")
symbols.append("aapl")

payload = {"symbols": symbols}
r = requests.post("http://127.0.0.1:5000/add_symbols", json=payload)
print(r.text)
