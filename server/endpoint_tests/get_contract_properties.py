import requests

payload = {
    "symbol": "aapl",
    "contract_symbol": "AAPL210625C00080000",
    "date": "2021-06-25",
    "property": "CURRENCY"
}

r = requests.get("http://127.0.0.1:5000/contract_search", json=payload)
print(r.text)