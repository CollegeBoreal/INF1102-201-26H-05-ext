import sys
import requests
import time

# Message début
print("Analyse en cours...")

# Argument
file = "data/sites.txt"
if len(sys.argv) > 1:
    file = sys.argv[1]

sites = []

with open(file, "r") as f:
    for line in f:
        if line.strip():
            sites.append(line.strip())

total = len(sites)
errors = 0
times = []

for site in sites:
    try:
        start = time.time()
        r = requests.get(site, timeout=5)
        end = time.time()

        t = round(end - start, 3)
        times.append(t)

        if str(r.status_code).startswith("4") or str(r.status_code).startswith("5"):
            errors += 1

    except:
        errors += 1
        times.append(0)

print("===== RAPPORT MONITORING WEB =====")
print("")
print("Total sites testés :", total)
print("Sites en erreur :", errors)

if len(times) > 0:
    avg = sum(times) / len(times)
    print("Temps moyen :", round(avg, 2), "sec")

print("")
print("Analyse terminée.")
print("Fichiers générés dans le dossier output.")