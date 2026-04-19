import os
import pandas as pd

# script folder
script_dir = os.path.dirname(os.path.abspath(_file_))

# project root = parent of scripts
project_dir = os.path.dirname(script_dir)

# correct paths
csv_path = os.path.join(project_dir, "data", "prix_energie.csv")
output_path = os.path.join(project_dir, "rapport.txt")

# load data
df = pd.read_csv(csv_path)
df["date"] = pd.to_datetime(df["date"])

# analysis
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
