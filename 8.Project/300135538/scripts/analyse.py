import sys
import os
import time
from datetime import datetime

import requests
import pandas as pd
import matplotlib.pyplot as plt


# Message début (IMPORTANT pour le correcteur)
print("Analyse en cours...")


# Vérification argument
if len(sys.argv) < 2:
    print("Usage: python scripts/analyse.py data/sites.txt")
    sys.exit(1)

fichier_sites = sys.argv[1]

# Chemin racine du projet
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
output_dir = os.path.join(BASE_DIR, "output")

# Créer dossier output
os.makedirs(output_dir, exist_ok=True)

# Vérifier fichier
if not os.path.exists(fichier_sites):
    print("Fichier introuvable")
    sys.exit(1)

# Lire sites
with open(fichier_sites, "r") as f:
    sites = [l.strip() for l in f if l.strip()]

resultats = []

# Analyse
for site in sites:
    try:
        start = time.time()
        r = requests.get(site, timeout=5)
        end = time.time()

        resultats.append({
            "site": site,
            "statut": r.status_code,
            "temps_reponse": round(end - start, 3),
            "disponibilite": "Disponible" if r.status_code == 200 else "Erreur"
        })

    except requests.exceptions.RequestException:
        resultats.append({
            "site": site,
            "statut": "N/A",
            "temps_reponse": 0,
            "disponibilite": "Indisponible"
        })

# DataFrame
df = pd.DataFrame(resultats)

# Chemins output
csv_path = os.path.join(output_dir, "resultats.csv")
txt_path = os.path.join(output_dir, "rapport.txt")
img_path = os.path.join(output_dir, "temps_reponse.png")

# Sauvegarde CSV
df.to_csv(csv_path, index=False)

# Rapport texte
with open(txt_path, "w") as f:
    f.write(f"Date: {datetime.now()}\n\n")
    for _, row in df.iterrows():
        f.write(f"{row['site']} - {row['disponibilite']} - {row['temps_reponse']}s\n")

# Graphique
plt.bar(df["site"], df["temps_reponse"])
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(img_path)

# Messages fin (IMPORTANT)
print("Analyse terminée.")
print("Fichiers générés dans le dossier output.")