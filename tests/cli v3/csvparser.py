'''
    format:
    arr[0] = date
    arr[1] = open
    arr[2] = high
    arr[3] = low
    arr[4] = close
'''

def get_val(symbol, d, prop):

    filename = symbol.upper() + ".csv"
    prop = prop.lower()

    f = open(filename, 'r')
    lines = []
    raw = f.readlines()
    for line in raw:
        line = line.replace("\n", "")
        lines.append(line)

    for i in range(len(lines)):
        arr = lines[i].split(",")
        
        if arr[0] == d:
            if prop == "open":
                return arr[1]
            if prop == "high":
                return arr[2]
            if prop == "low":
                return arr[3]
            if prop == "close":
                return arr[4]
    
    return "error: invalid property"