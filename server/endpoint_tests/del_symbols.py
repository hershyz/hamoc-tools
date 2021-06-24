import requests

symbols = []
symbols.append("aapl")
symbols.append("ibm")
    
payload = {"symbols": symbols}
r = requests.post("http://127.0.0.1:5000/del_symbols", json=payload)
print(r.text)
