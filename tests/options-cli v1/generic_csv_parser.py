def get_val(csv_path, prop, n):

    f = open(csv_path, 'r')
    lines = []
    raw = f.readlines()
    for line in raw:
        line = line.replace("\n", "")
        lines.append(line)
    
    raw_property_line = lines[0]
    property_arr = raw_property_line.split(",")

    target_line = lines[n + 1]
    target_arr = target_line.split(",")

    for i in range(len(property_arr)):
        if property_arr[i] == prop:
            return target_arr[i]

    return "error: could not find value"