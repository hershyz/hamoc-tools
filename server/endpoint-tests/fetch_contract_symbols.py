import requests

payload = {"symbol": "avgo", "date": "2021-06-25"}

r = requests.get("http://127.0.0.1:5000/contract_symbols", json=payload)
print(r.text)