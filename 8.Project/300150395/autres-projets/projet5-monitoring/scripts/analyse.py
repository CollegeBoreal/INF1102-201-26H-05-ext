#!/usr/bin/env python3

# =====================================
# Monitoring site web - INF1102
# Auteur : ISMAIL TRACHE
# Boreal ID : 300150395
# =====================================

import sys
import re
from collections import Counter
from datetime import datetime

if len(sys.argv) < 3:
    print("Usage: python3 analyse.py <data/sample.log> <output/rapport.txt>")
    sys.exit(1)

logfile  = sys.argv[1]
rapport  = sys.argv[2]

with open(logfile) as f:
    lines = f.readlines()

total   = len(lines)
codes   = re.findall(r'\| (\d{3}) \|', "".join(lines))
ok      = [c for c in codes if c == "200"]
errors  = [c for c in codes if c != "200"]
times   = re.findall(r'\| (\d+)ms \|', "".join(lines))
times   = [int(t) for t in times]
avg     = round(sum(times) / len(times), 2) if times else 0
fastest = min(times) if times else 0
slowest = max(times) if times else 0

with open(rapport, "a") as f:
    f.write("\n===== ANALYSE PYTHON =====\n")
    f.write(f"Total sites vérifiés : {total}\n")
    f.write(f"Sites OK (200)       : {len(ok)}\n")
    f.write(f"Sites en erreur      : {len(errors)}\n")
    f.write(f"Temps moyen          : {avg} ms\n")
    f.write(f"Temps le plus rapide : {fastest} ms\n")
    f.write(f"Temps le plus lent   : {slowest} ms\n")

    if errors:
        f.write(f"\nCodes d'erreur détectés : {Counter(errors).most_common()}\n")

    f.write(f"\nRapport généré le : {datetime.now()}\n")

print("✅ Analyse Python terminée")
