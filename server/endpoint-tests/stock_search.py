import requests

payload = {"symbol": "avgo", "date": "2021-06-24", "property": "close"}

r = requests.get("http://127.0.0.1:5000/stock_search", json=payload)
print(r.text)