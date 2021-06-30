import os


def read(filepath):
    f = open(filepath, 'r')
    lines = []
    raw = f.readlines()
    for line in raw:
        line = line.replace("\n", "")
        lines.append(line)
    return lines

def get_files(dir):
    path = os.getcwd() + dir
    arr = os.listdir(path)
    return arr