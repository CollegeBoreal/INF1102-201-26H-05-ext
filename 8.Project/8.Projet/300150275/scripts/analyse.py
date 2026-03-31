#!/usr/bin/env python3

# ============================================
# Projet 5 : Monitoring de sites web
# Auteur : Tarik Tidjet - 300150275
# ============================================

import sys
import os
from collections import Counter
from datetime import datetime

def analyser_log(fichier):
    sites_en_ligne = []
    sites_hors_ligne = []
    temps_reponse = []

    with open(fichier, "r") as f:
        lignes = f.readlines()

    for ligne in lignes:
        parties = ligne.strip().split(" | ")
        if len(parties) < 4:
            continue

        site = parties[0]
        code = parties[1]
        temps = int(parties[2].replace("ms", ""))
        statut = parties[3]

        temps_reponse.append((site, temps))

        if "EN LIGNE" in statut:
            sites_en_ligne.append(site)
        else:
            sites_hors_ligne.append(site)

    output = os.path.join(os.path.dirname(fichier), "../output/rapport.txt")

    with open(output, "a") as f:
        f.write("\n📈 Analyse Python\n")
        f.write("===========================================\n")
        f.write(f"Total sites vérifiés : {len(lignes)}\n")
        f.write(f"Sites en ligne       : {len(sites_en_ligne)}\n")
        f.write(f"Sites hors ligne     : {len(sites_hors_ligne)}\n")

        if temps_reponse:
            plus_rapide = min(temps_reponse, key=lambda x: x[1])
            plus_lent = max(temps_reponse, key=lambda x: x[1])
            moyenne = sum(t for _, t in temps_reponse) // len(temps_reponse)

            f.write(f"\n⚡ Site le plus rapide : {plus_rapide[0]} ({plus_rapide[1]}ms)\n")
            f.write(f"🐢 Site le plus lent  : {plus_lent[0]} ({plus_lent[1]}ms)\n")
            f.write(f"📊 Temps moyen        : {moyenne}ms\n")

        f.write("\n🕒 Analyse effectuée le : " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

    print("✅ Analyse Python terminée !")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 analyse.py <fichier_log>")
        sys.exit(1)
    analyser_log(sys.argv[1])
