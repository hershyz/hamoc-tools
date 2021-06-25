import requests

symbols = []
symbols.append("daby")
    
payload = {"symbols": symbols}
r = requests.post("http://127.0.0.1:5000/del_symbols", json=payload)
print(r.text)
