#!/usr/bin/env python3
import requests
from datetime import datetime

sites = [
    "https://google.com",
    "https://github.com",
    "https://youtube.com",
    "https://wikipedia.org",
    "https://stackoverflow.com"
]

rapport = "output/rapport.txt"

with open(rapport, "w") as f:
    f.write(f"Rapport Monitoring - {datetime.now()}\n")
    f.write("----------------------------------\n")
    for site in sites:
        try:
            r = requests.get(site, timeout=5)
            status = r.status_code
            temps = round(r.elapsed.total_seconds(), 2)
            f.write(f"OK {status} - {temps}s - {site}\n")
            print(f"OK {status} - {temps}s - {site}")
        except Exception as e:
            f.write(f"ERREUR - {site} - {e}\n")
            print(f"ERREUR - {site}")

print(f"Rapport genere : {rapport}")
