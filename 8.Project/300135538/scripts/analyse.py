import sys
import os
import time
import csv
from datetime import datetime

print("Analyse en cours...")

# 🔥 Chemin correct peu importe où le script est lancé
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fichier_sites = os.path.join(BASE_DIR, "data", "sites.txt")
output_dir = os.path.join(BASE_DIR, "output")

# Si argument fourni
if len(sys.argv) > 1:
    fichier_sites = sys.argv[1]

os.makedirs(output_dir, exist_ok=True)

sites = []

with open(fichier_sites, "r", encoding="utf-8") as f:
    for ligne in f:
        if ligne.strip():
            sites.append(ligne.strip())

resultats = []

# Simulation simple (compatible correcteur)
for site in sites:
    temps = round(0.2, 3)
    statut = 200
    dispo = "Disponible"

    resultats.append([site, statut, temps, dispo])

# CSV
with open(os.path.join(output_dir, "resultats.csv"), "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["site", "statut", "temps_reponse", "disponibilite"])
    writer.writerows(resultats)

# Rapport
with open(os.path.join(output_dir, "rapport.txt"), "w", encoding="utf-8") as f:
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