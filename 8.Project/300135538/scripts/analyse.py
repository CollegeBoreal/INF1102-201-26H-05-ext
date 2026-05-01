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
    print("Exemple : python analyse.py ../data/sites.txt")
    sys.exit(1)

fichier_sites = sys.argv[1]

# Vérifier que le fichier existe
if not os.path.exists(fichier_sites):
    print(f"Erreur : le fichier {fichier_sites} est introuvable.")
    sys.exit(1)

# Créer le dossier output si nécessaire
os.makedirs("../output", exist_ok=True)

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

# Création du tableau de résultats
df = pd.DataFrame(resultats)

# Sauvegarde des résultats en CSV
df.to_csv("../output/resultats.csv", index=False, encoding="utf-8")

# Génération du rapport texte
with open("../output/rapport.txt", "w", encoding="utf-8") as rapport:
    rapport.write("=== Rapport Monitoring Web ===\n")
    rapport.write(f"Date d'analyse : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

    for _, ligne in df.iterrows():
        rapport.write(f"Site : {ligne['site']}\n")
        rapport.write(f"Statut HTTP : {ligne['statut']}\n")
        rapport.write(f"Temps de réponse : {ligne['temps_reponse']} seconde(s)\n")
        rapport.write(f"Disponibilité : {ligne['disponibilite']}\n")
        rapport.write("-----------------------------\n")

# Génération du graphique
plt.figure(figsize=(10, 5))
plt.bar(df["site"], df["temps_reponse"])
plt.xlabel("Sites web")
plt.ylabel("Temps de réponse (secondes)")
plt.title("Temps de réponse des sites web")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("../output/temps_reponse.png")

print("Analyse terminée.")
print("Fichiers générés dans le dossier output.")