import sys
import requests
import time
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Vérification argument
if len(sys.argv) < 2:
    print("Erreur : fichier sites manquant")
    sys.exit(1)

fichier_sites = sys.argv[1]

resultats = []

# Lire les sites
with open(fichier_sites, "r") as f:
    sites = [ligne.strip() for ligne in f if ligne.strip()]

print("Analyse en cours...")

# Tester chaque site
for site in sites:
    try:
        start = time.time()
        response = requests.get(site, timeout=5)
        end = time.time()

        temps = round(end - start, 3)
        statut = response.status_code

        dispo = "Disponible" if statut == 200 else "Erreur"

    except:
        temps = 0
        statut = "N/A"
        dispo = "Indisponible"

    resultats.append({
        "site": site,
        "statut": statut,
        "temps_reponse": temps,
        "disponibilite": dispo
    })

# DataFrame
df = pd.DataFrame(resultats)

# Sauvegarde CSV
df.to_csv("../output/resultats.csv", index=False)

# Rapport texte
with open("../output/rapport.txt", "w", encoding="utf-8") as f:
    f.write("=== Rapport Monitoring Web ===\n")
    f.write(f"Date : {datetime.now()}\n\n")

    for _, row in df.iterrows():
        f.write(f"Site : {row['site']}\n")
        f.write(f"Statut : {row['statut']}\n")
        f.write(f"Temps : {row['temps_reponse']} s\n")
        f.write(f"Disponibilité : {row['disponibilite']}\n")
        f.write("-----------------------------\n")

# Graphique
plt.figure()
plt.bar(df["site"], df["temps_reponse"])
plt.xticks(rotation=30)
plt.title("Temps de réponse des sites")
plt.tight_layout()
plt.savefig("../output/temps_reponse.png")

print("Rapport généré dans /output")