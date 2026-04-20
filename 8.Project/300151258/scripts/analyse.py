import csv
import os

# Find CSV from either project root or scripts folder
if os.path.exists("data/prix_energie.csv"):
    csv_path = "data/prix_energie.csv"
    output_path = "rapport.txt"
elif os.path.exists("../data/prix_energie.csv"):
    csv_path = "../data/prix_energie.csv"
    output_path = "../rapport.txt"
else:
    raise FileNotFoundError("prix_energie.csv not found")

essence_vals = []
brent_vals = []

with open(csv_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        essence_vals.append(float(row["essence_toronto"]))
        brent_vals.append(float(row["brent"]))

ess_mean = round(sum(essence_vals) / len(essence_vals), 2)
ess_min = min(essence_vals)
ess_max = max(essence_vals)

brent_mean = round(sum(brent_vals) / len(brent_vals), 2)
brent_min = min(brent_vals)
brent_max = max(brent_vals)

report = [
    "=== ESSENCE TORONTO ===",
    f"Moyenne: {ess_mean}",
    f"Min: {ess_min}",
    f"Max: {ess_max}",
    "",
    "=== BRENT ===",
    f"Moyenne: {brent_mean}",
    f"Min: {brent_min}",
    f"Max: {brent_max}",
]

for line in report:
    print(line)

with open(output_path, "w", encoding="utf-8") as f:
    for line in report:
        f.write(line + "\n")
