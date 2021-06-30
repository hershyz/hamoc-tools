import requests

payload = {
    "low_price": 900,
    "high_price": 1000
}

r = requests.get("http://127.0.0.1:5000/stock_price_query", json=payload)
print(r.text)