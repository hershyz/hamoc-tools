import requests

payload = {
    "low": 2000,
    "high": 2100,
    "property": "strike"
}

r = requests.get("http://127.0.0.1:5000/option_query", json=payload)
print(r.text)