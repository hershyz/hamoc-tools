import requests


class HamocClient:    
    
    def __init__(self, uri):
        self.uri = uri
    
    def add_symbols(self, symbols):
        payload = {
            "symbols": symbols
        }
        r = requests.post(self.uri + "/add_symbols", json=payload)
        return r.text