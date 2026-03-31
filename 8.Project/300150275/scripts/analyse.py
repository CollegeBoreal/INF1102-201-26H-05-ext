#!/usr/bin/env python3

# ============================================
# Projet 5 : Monitoring de sites web
# Auteur : Tarik Tidjet - 300150275
# Collecte toutes les 3 minutes
# ============================================

import urllib.request
import time
import csv
import os
from datetime import datetime

SITES = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.wikipedia.org",
    "https://www.youtube.com",
    "https://www.amazon.com"
]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, "../data/monitoring.csv")
RAPPORT  = os.path.join(BASE_DIR, "../output/rapport.txt")

os.makedirs(os.path.dirname(CSV_FILE), exist_ok=True)
os.makedirs(os.path.dirname(RAPPORT), exist_ok=True)

# Créer le CSV avec entête si inexistant
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "site", "code_http", "temps_ms", "statut"])

def verifier_site(url):
    start = time.time()
    try:
        req = urllib.request.urlopen(url, timeout=10)
        code = req.getcode()
    except Exception:
        code = 0
    temps = int((time.time() - start) * 1000)
    statut = "EN LIGNE" if code == 200 else "HORS LIGNE"
    return code, temps, statut

def collecter():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n📡 Collecte - {timestamp}")
    print("=" * 50)

    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        for site in SITES:
            code, temps, statut = verifier_site(site)
            writer.writerow([timestamp, site, code, temps, statut])
            icone = "✅" if statut == "EN LIGNE" else "❌"
            print(f"{icone} {site} | {code} | {temps}ms | {statut}")

    print(f"\n✅ Données sauvegardées dans {CSV_FILE}")

if __name__ == "__main__":
    collecter()
