import requests


class Hamoc_Client:    
    
    def __init__(self, uri):
        self.uri = uri
    
    # add symbols:
    def add_symbols(self, symbols):
        payload = {
            "symbols": symbols
        }
        r = requests.post(self.uri + "/add_symbols", json=payload)
        return r.text
    
    # get symbols:
    def get_symbols(self):
        r = requests.get(self.uri + "/get_symbols")
        return r.text

    # delete symbols:
    def del_symbols(self, symbols):
        payload = {
            "symbols": symbols
        }
        r = requests.post(self.uri + "/del_symbols", json=payload)
        return r.text