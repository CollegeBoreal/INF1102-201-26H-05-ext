#!/usr/bin/env python3

# =====================================
# Analyse Monitoring - INF1102
# Auteur : 300150268
# =====================================

import sys
from datetime import datetime

if len(sys.argv) < 2:
    print("Usage: python3 analyse.py <logfile>")
    sys.exit(1)

logfile = sys.argv[1]

with open(logfile) as f:
    lines = f.readlines()

total = len(lines)
ok = 0
errors = 0
temps = []

for line in lines:
    parts = line.strip().split(" | ")
    if len(parts) >= 4:
        code = parts[2].strip()
        duree = parts[3].replace("ms", "").strip()
        statut = parts[4].strip() if len(parts) > 4 else ""

        if "OK" in statut:
            ok += 1
        else:
            errors += 1

        try:
            temps.append(int(duree))
        except:
            pass

print(f"Total sites vérifiés : {total}")
print(f"Sites OK              : {ok}")
print(f"Sites en erreur       : {errors}")

if temps:
    print(f"Temps moyen           : {sum(temps)//len(temps)} ms")
    print(f"Temps le plus rapide  : {min(temps)} ms")
    print(f"Temps le plus lent    : {max(temps)} ms")