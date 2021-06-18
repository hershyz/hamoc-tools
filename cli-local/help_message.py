def show():
    print("command:      args:                              description:")
    print("---------------------------------------------------------------------------------------------")
    print("help:                                            displays all commands")
    print("stock_store   [symbol, start, end]:              fetches historical data given a stock symbol and date bounds and dumps it in a csv file")
    print("stock_lookup  [symbol, date]:                    looks up the close price of a given stock (stock_store must be run first)")

    # to be implemented
    print("options_store [symbol, date]:                    creates a csv file with all the calls for the given stock expiring on the specific date")
    print("calc_profits  [symbol, start, end, investment]:  calculates how much money would have been made (or lost) between two dates given an initial investment on a stock (stock_store must be run first)")
    print("volatility    [symbol, start, end]:              calculates the average daily change in a stock from a start and end date (stock_store must be run first)")
    print("aroc          [symbol, start, end]:              finds the average rate of change of a stock given a start and end date (stock_store must be run first)")
    print("compare       [symbol1, symbol2, start, end]:    finds a relationship between two stocks")