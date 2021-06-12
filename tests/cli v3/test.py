import csvparser as csv

price = csv.get_val("goog", "2021-01-07", "close")
print(price)