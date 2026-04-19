#!/usr/bin/env python3
import sys
from collections import Counter

if len(sys.argv) > 1:
    file = sys.argv[1]
else:
    file = "data/access.log"

codes = []
times = []

with open(file, "r", encoding="utf-8") as f:
    lines = f.readlines()

for line in lines:
    parts = line.strip().split()

    if len(parts) >= 4:
        codes.append(parts[3])

    if len(parts) >= 5:
        try:
            times.append(float(parts[4]))
        except ValueError:
            pass

total = len(lines)
errors = [c for c in codes if c.startswith("4") or c.startswith("5")]

text = []
text.append("===== RAPPORT MONITORING SITE WEB =====")
text.append(f"Total requêtes : {total}")
text.append(f"Total erreurs : {len(errors)}")
text.append(f"Erreurs 404 : {codes.count('404')}")
text.append(f"Erreurs 500 : {codes.count('500')}")

if times:
    avg_time = sum(times) / len(times)
    text.append(f"Temps de réponse moyen : {avg_time:.2f} sec")

text.append("")
text.append("Codes HTTP :")
for code, count in Counter(codes).items():
    text.append(f"{code} : {count}")

for line in text:
    print(line)

with open("output/rapport.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(text) + "\n")
