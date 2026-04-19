import sys

file = sys.argv[1]

with open(file) as f:
    lines = f.readlines()

print("Nombre de lignes :", len(lines))