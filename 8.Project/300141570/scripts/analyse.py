import sys
from collections import Counter

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
errors = [c for c in codes if c.startswith("4") or c.startswith("5")]
top_codes = Counter(codes).most_common()

print(f"Total requêtes : {total}")
print(f"Total erreurs : {len(errors)}")
print(f"Erreurs 404 : {codes.count('404')}")
print(f"Erreurs 500 : {codes.count('500')}")

if times:
    avg_time = sum(times) / len(times)
    print(f"Temps de réponse moyen : {avg_time:.2f} sec")

print("\nCodes HTTP :")
for code, count in top_codes:
    print(f"{code} : {count}")
