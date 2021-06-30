import requests

payload = {
    "low": 1,
    "high": 1,
    "property": "bab"
}

r = requests.get("http://127.0.0.1:5000/option_query", json=payload)
print(r.text)