import pandas as pd

file = "data/prix_energie.csv"
df = pd.read_csv(file)

print("===== RAPPORT PRIX ENERGIE =====")
print("Ville :", "Toronto")
print("Total lignes :", len(df))
print("Prix moyen essence :", round(df["essence_toronto"].mean(), 2))
print("Prix minimum essence :", df["essence_toronto"].min())
print("Prix maximum essence :", df["essence_toronto"].max())
print("Prix moyen Brent :", round(df["brent"].mean(), 2))
print("Prix minimum Brent :", df["brent"].min())
print("Prix maximum Brent :", df["brent"].max())

with open("output/rapport.txt", "w", encoding="utf-8") as f:
    f.write("===== RAPPORT PRIX ENERGIE =====\n")
    f.write("Ville : Toronto\n")
    f.write(f"Total lignes : {len(df)}\n")
    f.write(f"Prix moyen essence : {round(df['essence_toronto'].mean(), 2)}\n")
    f.write(f"Prix minimum essence : {df['essence_toronto'].min()}\n")
    f.write(f"Prix maximum essence : {df['essence_toronto'].max()}\n")
    f.write(f"Prix moyen Brent : {round(df['brent'].mean(), 2)}\n")
    f.write(f"Prix minimum Brent : {df['brent'].min()}\n")
    f.write(f"Prix maximum Brent : {df['brent'].max()}\n")
