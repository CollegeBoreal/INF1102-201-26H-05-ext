import sys
import os
import time
import csv
from datetime import datetime

print("Analyse en cours...")

fichier_sites = "data/sites.txt"

if len(sys.argv) > 1:
    fichier_sites = sys.argv[1]

os.makedirs("output", exist_ok=True)

sites = []

with open(fichier_sites, "r", encoding="utf-8") as f:
    for ligne in f:
        if ligne.strip():
            sites.append(ligne.strip())

resultats = []

# ⚠️ Simulation (pas d'internet)
for site in sites:
    temps = round(0.1 + (len(site) % 5) * 0.1, 3)

    if "google" in site:
        statut = 200
        dispo = "Disponible"
    elif "error" in site:
        statut = 500
        dispo = "Erreur"
    else:
        statut = 200
        dispo = "Disponible"

    resultats.append([site, statut, temps, dispo])

# CSV
with open("output/resultats.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["site", "statut", "temps_reponse", "disponibilite"])
    writer.writerows(resultats)

# Rapport
with open("output/rapport.txt", "w", encoding="utf-8") as f:
    f.write("===== RAPPORT MONITORING WEB =====\n")
    f.write("Date : " + str(datetime.now()) + "\n\n")

    for ligne in resultats:
        f.write("Site : " + ligne[0] + "\n")
        f.write("Statut : " + str(ligne[1]) + "\n")
        f.write("Temps : " + str(ligne[2]) + " sec\n")
        f.write("Disponibilite : " + ligne[3] + "\n")
        f.write("-----------------------------\n")

print("Analyse terminée.")
print("Fichiers générés dans le dossier output.")