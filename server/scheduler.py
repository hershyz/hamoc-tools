import time
import requests

def init(uri):
    while True:
        stock_request = requests.get(uri + "/stock_store")
        options_request = requests.get(uri + "/options_store")
        print("[scheduler]: " + stock_request.text)
        print("[scheduler]: " + options_request.text)
        time.sleep(432000) # 432000 = 12 hours -> update options and data twice a day (on server init)