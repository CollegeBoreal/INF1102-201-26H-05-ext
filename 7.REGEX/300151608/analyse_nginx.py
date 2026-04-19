import re
from collections import Counter
from datetime import datetime

logfile = "/var/log/nginx/access.log"
rapport = f"rapport_nginx_py_{datetime.now().strftime('%Y-%m-%d')}.txt"

# Lecture du fichier
with open(logfile, "r") as f:
    lines = f.readlines()

# Total des requêtes
total = len(lines)

# Extraire les codes HTTP
codes = []
for line in lines:
    match = re.search(r'" (\d{3}) ', line)
    if match:
        codes.append(match.group(1))

# Calcul des erreurs
errors = [c for c in codes if c.startswith(("4", "5"))]

# Extraire les IP (début de ligne)
ips = []
for line in lines:
    match = re.match(r'(\d{1,3}(?:\.\d{1,3}){3})', line)
    if match:
        ips.append(match.group(1))

# Extraire les pages GET
pages = []
for line in lines:
    match = re.search(r'"GET ([^ ]+)', line)
    if match:
        pages.append(match.group(1))

# Écriture du rapport
with open(rapport, "w") as f:
    f.write(f"Rapport Nginx Python - {datetime.now()}\n")
    f.write("--------------------------------------\n")
    f.write(f"Total des requêtes : {total}\n")
    f.write(f"Total des erreurs HTTP : {len(errors)}\n")
    f.write(f"Erreurs 404 : {codes.count('404')}\n")
    f.write(f"Erreurs 500 : {codes.count('500')}\n")

    f.write("\nTop 5 des IP :\n")
    for ip, count in Counter(ips).most_common(5):
        f.write(f"{count} - {ip}\n")

    f.write("\nTop 5 des pages :\n")
    for page, count in Counter(pages).most_common(5):
        f.write(f"{count} - {page}\n")

print(f"Rapport généré avec succès : {rapport}")
