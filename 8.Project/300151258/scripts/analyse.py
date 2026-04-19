import os
import pandas as pd

# Detect CSV path from either launch location
if os.path.exists("data/prix_energie.csv"):
    csv_path = "data/prix_energie.csv"
    output_path = "rapport.txt"
elif os.path.exists("../data/prix_energie.csv"):
    csv_path = "../data/prix_energie.csv"
    output_path = "../rapport.txt"
else:
    raise FileNotFoundError("CSV file not found")

df = pd.read_csv(csv_path)
df["date"] = pd.to_datetime(df["date"])

ess_mean = round(df["essence_toronto"].mean(), 2)
ess_min = df["essence_toronto"].min()
ess_max = df["essence_toronto"].max()

brent_mean = round(df["brent"].mean(), 2)
brent_min = df["brent"].min()
brent_max = df["brent"].max()

report = []
report.append("=== ESSENCE TORONTO ===")
report.append(f"Moyenne: {ess_mean}")
report.append(f"Min: {ess_min}")
report.append(f"Max: {ess_max}")
report.append("")
report.append("=== BRENT ===")
report.append(f"Moyenne: {brent_mean}")
report.append(f"Min: {brent_min}")
report.append(f"Max: {brent_max}")

for line in report:
    print(line)

with open(output_path, "w", encoding="utf-8") as f:
    for line in report:
        f.write(line + "\n")
