import requests

class HamocClient:    
    
    def __init__(self, uri):
        self.uri = uri
    
    def add_symbols(self, symbols):
        r = requests.post("/add_symbols")