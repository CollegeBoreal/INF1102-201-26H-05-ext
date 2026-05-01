import sys
import os
import time
from datetime import datetime

import requests
import pandas as pd
import matplotlib.pyplot as plt


# Vérification de l'argument
if len(sys.argv) < 2:
    print("Erreur : veuillez fournir le fichier contenant les sites.")
    print("Exemple : python scripts/analyse.py data/sites.txt")
    sys.exit(1)

fichier_sites = sys.argv[1]

# Vérifier que le fichier existe
if not os.path.exists(fichier_sites):
    print(f"Erreur : le fichier {fichier_sites} est introuvable.")
    sys.exit(1)

# Créer le dossier output (à la racine du projet)
os.makedirs("output", exist_ok=True)

resultats = []

# Lire la liste des sites
with open(fichier_sites, "r", encoding="utf-8") as f:
    sites = [ligne.strip() for ligne in f if ligne.strip()]

print("Analyse en cours...")

# Tester chaque site
for site in sites:
    try:
        debut = time.time()
        reponse = requests.get(site, timeout=5)
        fin = time.time()

        temps_reponse = round(fin - debut, 3)
        statut = reponse.status_code

        if statut == 200:
            disponibilite = "Disponible"
        else:
            disponibilite = "Erreur HTTP"

    except requests.exceptions.RequestException:
        temps_reponse = 0
        statut = "N/A"
        disponibilite = "Indisponible"

    resultats.append({
        "site": site,
        "statut": statut,
        "temps_reponse": temps_reponse,
        "disponibilite": disponibilite
    })

import sys
import os
import time
from datetime import datetime

import requests
import pandas as pd
import matplotlib.pyplot as plt


if len(sys.argv) < 2:
    print("Usage: python scripts/analyse.py data/sites.txt")
    sys.exit(1)

fichier_sites = sys.argv[1]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
output_dir = os.path.join(BASE_DIR, "output")

os.makedirs(output_dir, exist_ok=True)

if not os.path.exists(fichier_sites):
    print("Fichier introuvable")
    sys.exit(1)

with open(fichier_sites, "r") as f:
    sites = [l.strip() for l in f if l.strip()]

resultats = []

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

df = pd.DataFrame(resultats)

csv_path = os.path.join(output_dir, "resultats.csv")
txt_path = os.path.join(output_dir, "rapport.txt")
img_path = os.path.join(output_dir, "temps_reponse.png")

df.to_csv(csv_path, index=False)

with open(txt_path, "w") as f:
    f.write(f"Date: {datetime.now()}\n\n")
    for _, row in df.iterrows():
        f.write(f"{row['site']} - {row['disponibilite']} - {row['temps_reponse']}s\n")

plt.bar(df["site"], df["temps_reponse"])
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(img_path)

print("OK")