from pathlib import Path
from collections import Counter

base = Path(__file__).resolve().parent.parent

log_file = base / "data" / "sample.log"
rapport_file = base / "output" / "rapport.txt"

ips = []
urls = []

with open(log_file, "r", encoding="utf-8") as fichier:
    for ligne in fichier:
        elements = ligne.split()
        if len(elements) >= 3:
            ips.append(elements[0])
            urls.append(elements[-1].replace('"', ""))

top_ips = Counter(ips).most_common(3)
top_urls = Counter(urls).most_common(3)

with open(rapport_file, "w", encoding="utf-8") as rapport:
    rapport.write("===== RAPPORT ANALYSE LOG =====\n\n")
    rapport.write("Top IP:\n")
    for ip, n in top_ips:
        rapport.write(f"{ip}: {n}\n")

    rapport.write("\nTop URLs:\n")
    for url, n in top_urls:
        rapport.write(f"{url}: {n}\n")

print("Analyse terminee")