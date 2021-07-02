import requests


class Hamoc_Client:    
    

    # init
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


    # update stock data:
    def update_stock_data(self):
        r = requests.get(self.uri + "/stock_store")
        return r.text
    

    # update options data:
    def update_options_data(self):
        r = requests.get(self.uri + "/options_store")
        return r.text
    

    # gets the value of a specific property of a stock
    # properties: Date,Open,High,Low,Close,Volume,Dividends,Stock Splits
    def get_stock_val(self, symbol, date, prop):
        payload = {
            "symbol": symbol,
            "date": date,
            "property": prop
        }
        r = requests.get(self.uri + "/stock_search", json=payload)
        return r.text

    
    # fetch contract symbols (call options) of a given stock on any specific date:
    def get_contract_symbols(self, symbol, date):
        payload = {
            "symbol": symbol,
            "date": date
        }
        r = requests.get(self.uri + "/contract_symbols", json=payload)
        return r.text


    # fetch contract (call option) properties:
    # properties: contractSymbol	lastTradeDate	strike	lastPrice	bid	ask	change	percentChange	volume	openInterest	impliedVolatility	inTheMoney	contractSize	currency
    def get_contract_property(self, symbol, contract_symbol, date, prop):
        payload = {
            "symbol": symbol,
            "contract_symbol": contract_symbol,
            "date": date,
            "property": prop
        }
        r = requests.get(self.uri + "/contract_search", json=payload)
        return r.text