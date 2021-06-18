def read(filepath):
    f = open(filepath, 'r')
    lines = []
    raw = f.readlines()
    for line in raw:
        line = line.replace("\n", "")
        lines.append(line)
    return lines