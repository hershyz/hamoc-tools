import requests

payload = {
    "low": 300,
    "high": 400,
    "property": "strike"
}

r = requests.get("http://127.0.0.1:5000/option_query", json=payload)
print(r.text)