# =====================================
# Projet 5 - Monitoring site web
# Auteur : Imad Boudeuf
# Boreal ID : 300152410
# =====================================

import re
from datetime import datetime
from collections import Counter

rapport_in = r"C:\Users\Hocine\INF1102-201-26H-05\8.Project\300152410\output\rapport.txt"
rapport_out = r"C:\Users\Hocine\INF1102-201-26H-05\8.Project\300152410\output\analyse.txt"

with open(rapport_in, "r") as f:
    lines = f.readlines()

# Extraire les statuts
ok_sites = []
error_sites = []

for line in lines:
    if "Status: 200" in line:
        match = re.search(r"(https://\S+)", line)
        if match:
            ok_sites.append(match.group(1))
    elif "ERREUR" in line:
        match = re.search(r"(https://\S+)", line)
        if match:
            error_sites.append(match.group(1))

# Extraire temps de reponse
temps = re.findall(r"Temps: (\d+)ms", "".join(lines))
temps = [int(t) for t in temps]

with open(rapport_out, "w") as f:
    f.write(f"===== ANALYSE MONITORING =====\n")
    f.write(f"Date : {datetime.now()}\n")
    f.write(f"------------------------------\n")
    f.write(f"Sites OK : {len(ok_sites)}\n")
    for s in ok_sites:
        f.write(f"  - {s}\n")
    f.write(f"Sites en erreur : {len(error_sites)}\n")
    for s in error_sites:
        f.write(f"  - {s}\n")
    if temps:
        f.write(f"\nTemps de reponse moyen : {sum(temps)//len(temps)}ms\n")
        f.write(f"Temps min : {min(temps)}ms\n")
        f.write(f"Temps max : {max(temps)}ms\n")

print("Analyse generee :", rapport_out)