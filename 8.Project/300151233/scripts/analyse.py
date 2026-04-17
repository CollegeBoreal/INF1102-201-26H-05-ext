import requests
import time
from datetime import datetime

sites = ["https://syphax.com", "https://google.com",  "https://github.com", "https://youtube.com"]

for url in sites:
    try:
        start = time.time()
        response = requests.get(url, timeout=10)
        end = time.time()

        print("===== RAPPORT de suveillance =====")
        print("Date:", datetime.now())
        print("URL:", url)
        print("Code HTTP:", response.status_code)
        print("Temps:", round(end - start, 3), "secondes")
        print("-------------------------")

    except:
        print("===== RAPPORT =====")
        print("Date:", datetime.now())
        print("URL:", url)
        print("Statut: site inaccessible")
        print("-------------------------")
statut = "OK" if response.status_code == 200 else "ERREUR"
print("Statut:", statut)
