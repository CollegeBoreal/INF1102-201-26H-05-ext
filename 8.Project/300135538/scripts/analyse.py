import sys
import os
import time
import csv
from datetime import datetime
from urllib.request import urlopen
from urllib.error import URLError, HTTPError


print("Analyse en cours...")

# Fichier par défaut
fichier_sites = "data/sites.txt"

# Si le prof lance : python scripts/analyse.py data/sites.txt
if len(sys.argv) > 1:
    fichier_sites = sys.argv[1]

# Créer le dossier output s'il n'existe pas
os.makedirs("output", exist_ok=True)

# Lire les sites web
sites = []

with open(fichier_sites, "r", encoding="utf-8") as f:
    for ligne in f:
        if ligne.strip():
            sites.append(ligne.strip())

resultats = []

# Tester chaque site
for site in sites:
    try:
        debut = time.time()
        reponse = urlopen(site, timeout=5)
        fin = time.time()

        statut = reponse.getcode()
        temps = round(fin - debut, 3)

        if statut == 200:
            disponibilite = "Disponible"
        else:
            disponibilite = "Erreur"

    except HTTPError as e:
        statut = e.code
        temps = 0
        disponibilite = "Erreur HTTP"

    except URLError:
        statut = "N/A"
        temps = 0
        disponibilite = "Indisponible"

    resultats.append([site, statut, temps, disponibilite])

# Créer le fichier CSV
with open("output/resultats.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["site", "statut", "temps_reponse", "disponibilite"])
    writer.writerows(resultats)

# Créer le rapport texte
with open("output/rapport.txt", "w", encoding="utf-8") as f:
    f.write("===== RAPPORT MONITORING WEB =====\n")
    f.write("Date : " + str(datetime.now()) + "\n\n")

    total_sites = len(resultats)
    total_indisponibles = 0

    for ligne in resultats:
        if ligne[3] != "Disponible":
            total_indisponibles += 1

    f.write("Total sites testes : " + str(total_sites) + "\n")
    f.write("Sites indisponibles ou en erreur : " + str(total_indisponibles) + "\n\n")

    for ligne in resultats:
        f.write("Site : " + str(ligne[0]) + "\n")
        f.write("Statut : " + str(ligne[1]) + "\n")
        f.write("Temps de reponse : " + str(ligne[2]) + " sec\n")
        f.write("Disponibilite : " + str(ligne[3]) + "\n")
        f.write("-----------------------------\n")

print("Analyse terminée.")
print("Fichiers générés dans le dossier output.")