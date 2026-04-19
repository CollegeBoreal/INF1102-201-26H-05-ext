import pandas as pd
import os

# Always start from script location (IMPORTANT for teacher script)
base_path = os.path.dirname(_file_)

# Correct path to CSV
csv_path = os.path.join(base_path, "data", "prix_energie.csv")

# Load data
df = pd.read_csv(csv_path)

# Convert date
df["date"] = pd.to_datetime(df["date"])

# ===== ANALYSIS =====
print("=== ESSENCE TORONTO ===")
print("Moyenne:", round(df["essence_toronto"].mean(), 2))
print("Min:", df["essence_toronto"].min())
print("Max:", df["essence_toronto"].max())

print("\n=== BRENT ===")
print("Moyenne:", round(df["brent"].mean(), 2))
print("Min:", df["brent"].min())
print("Max:", df["brent"].max())
