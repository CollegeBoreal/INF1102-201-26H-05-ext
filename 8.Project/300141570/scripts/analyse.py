import sys

if len(sys.argv) > 1:
    file = sys.argv[1]
else:
    file = "data/access.log"

codes = []
times = []

with open(file, "r") as f:
    lines = f.readlines()

for line in lines:
    parts = line.strip().split()

    if len(parts) >= 4:
        codes.append(parts[3])

    if len(parts) >= 5:
        try:
            times.append(float(parts[4]))
        except:
            pass

total = len(lines)
errors = 0

for c in codes:
    if c.startswith("4") or c.startswith("5"):
        errors += 1

print("===== RAPPORT MONITORING SITE WEB =====")
print("Date :", "AUTO")
print("")
print("Total requêtes :", total)
print("Total erreurs :", errors)
print("Erreurs 404 :", codes.count("404"))
print("Erreurs 500 :", codes.count("500"))

if len(times) > 0:
    avg = sum(times) / len(times)
    print("Temps de réponse moyen :", round(avg, 2), "sec")

print("")
print("Codes HTTP :")

unique = []
for c in codes:
    if c not in unique:
        unique.append(c)

for c in unique:
    print(c, ":", codes.count(c))
