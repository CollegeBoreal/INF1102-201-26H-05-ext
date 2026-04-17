import re
from collections import Counter

logfile = "data/sample.log"
rapport = "output/rapport.txt"

with open(logfile, "r") as f:
    lines = f.readlines()

ips = []
urls = []
codes = []

for line in lines:
    ip_match = re.match(r'(\d{1,3}(?:\.\d{1,3}){3})', line)
    url_match = re.search(r'"GET ([^ ]+)', line)
    code_match = re.search(r'" (\d{3}) ', line)

    if ip_match:
        ips.append(ip_match.group(1))
    if url_match:
        urls.append(url_match.group(1))
    if code_match:
        codes.append(code_match.group(1))

errors = [c for c in codes if c.startswith(("4", "5"))]

with open(rapport, "w") as f:
    f.write("Rapport d'analyse des logs\n")
    f.write("-------------------------\n")
    f.write(f"Total des requêtes : {len(lines)}\n")
    f.write(f"Total des erreurs HTTP : {len(errors)}\n")
    f.write(f"Erreurs 404 : {codes.count('404')}\n")
    f.write(f"Erreurs 500 : {codes.count('500')}\n")

    f.write("\nTop 3 IP :\n")
    for ip, count in Counter(ips).most_common(3):
        f.write(f"{count} - {ip}\n")

    f.write("\nTop 3 URLs :\n")
    for url, count in Counter(urls).most_common(3):
        f.write(f"{count} - {url}\n")

print("Rapport généré :", rapport)
