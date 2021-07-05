def read(filepath):
    f = open(filepath, 'r')
    lines = []
    raw = f.readlines()
    for line in raw:
        line = line.replace("\n", "")
        lines.append(line)
    return lines

def parse_csv_generic(lines, n, prop):
    raw_property_line = lines[0]
    property_arr = raw_property_line.split(",")

    target_line = lines[n]
    target_arr = target_line.split(",")

    for i in range(len(property_arr)):
        if property_arr[i] == prop:
            return target_arr[i]

    return "error: could not find value"
