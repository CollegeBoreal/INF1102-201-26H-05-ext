import sys

file = sys.argv[1]

with open(file) as f:
    lines = f.readlines()

total = len(lines)
codes = []
times = []

for line in lines:
    parts = line.strip().split()
    if len(parts) >= 5:
        codes.append(parts[3])
        try:
            times.append(float(parts[4]))
        except:
            pass

errors = [c for c in codes if c.startswith("4") or c.startswith("5")]

print("Total requêtes :", total)
print("Total erreurs :", len(errors))
print("Erreurs 404 :", codes.count("404"))
print("Erreurs 500 :", codes.count("500"))

if times:
    print("Temps de réponse moyen :", sum(times)/len(times))

print("\nCodes HTTP :")
for c in set(codes):
    print(c, ":", codes.count(c))
