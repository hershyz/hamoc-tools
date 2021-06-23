import requests

symbols = []
symbols.append("goog")
symbols.append("msft")
symbols.append("avgo")
symbols.append("avgo")
symbols.append("goog")

payload = {"symbols": symbols}
r = requests.post("http://127.0.0.1:5000/add_symbols", json=payload)
print(r.text)