import requests

r = requests.get("http://127.0.0.1:5000/get_symbols")
print(r.text)
