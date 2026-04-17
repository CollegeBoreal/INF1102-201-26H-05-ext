import requests
import csv
import time
import os
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

sites = [
    "https://google.com",
    "https://github.com",
    "https://wikipedia.org",
    "https://youtube.com",
    "https://amazon.com"
]

base_path = "/home/ubuntu/INF1102-201-26H-05/8.Project/300151466"
csv_file = f"{base_path}/data/monitoring.csv"
rapport_file = f"{base_path}/output/rapport.txt"
graph_file = f"{base_path}/output/graphique_evolution.png"

results = []

for site in sites:
    try:
        start = time.time()
        response = requests.get(site, timeout=5)
        end = time.time()

        response_time = round(end - start, 3)
        status = response.status_code
    except:
        response_time = 0
        status = "ERROR"

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    results.append([timestamp, site, status, response_time])

file_exists = os.path.isfile(csv_file)

with open(csv_file, "a", newline="") as f:
    writer = csv.writer(f)
    if not file_exists:
        writer.writerow(["timestamp", "site", "status", "response_time"])
    writer.writerows(results)

with open(rapport_file, "w") as f:
    f.write("=== Rapport Monitoring ===\n\n")
    for r in results:
        f.write(f"{r[0]} | {r[1]} | Status: {r[2]} | Temps: {r[3]}s\n")

# Graphique
try:
    df = pd.read_csv(csv_file)
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    plt.figure(figsize=(10,6))

    for site in df["site"].unique():
        site_data = df[df["site"] == site]
        plt.plot(site_data["timestamp"], site_data["response_time"], marker='o', label=site)

    plt.xlabel("Temps")
    plt.ylabel("Temps de réponse (s)")
    plt.title("Évolution des temps de réponse")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig(graph_file)
    plt.close()

except Exception as e:
    print("Erreur graphique:", e)

print("Analyse terminée + graphique généré")
