#!/usr/bin/env python3

# =====================================
# Analyse Nginx avec Regex - INF1102
# Auteur : 300150268
# Boreal ID : 300150268
# =====================================

import re, os
from collections import Counter
from datetime import datetime

logfile     = "/var/log/nginx/access.log"
rapport_dir = os.path.expanduser("~/INF1102-201-26H-05/7.REGEX/300150268")
rapport     = f"{rapport_dir}/rapport_nginx_py_{datetime.now().date()}.txt"

if not os.path.exists(logfile):
    print(f"❌ Fichier log introuvable : {logfile}")
    exit(1)

with open(logfile) as f:
    lines = f.readlines()

data   = "".join(lines)
codes  = re.findall(r'" (\d{3}) ', data)
errors = [c for c in codes if c.startswith(('4', '5'))]
ips    = re.findall(r'(\d{1,3}(?:\.\d{1,3}){3})', data)
pages  = re.findall(r'"GET ([^ ]+)', data)

with open(rapport, "w") as f:
    f.write(f"📊 Rapport Nginx Python - {datetime.now()}\n")
    f.write("----------------------------------\n")
    f.write(f"Total requêtes : {len(lines)}\n")
    f.write(f"Erreurs HTTP (4xx/5xx) : {len(errors)}\n")
    f.write(f"Erreurs 404 : {codes.count('404')}\n")
    f.write(f"Erreurs 500 : {codes.count('500')}\n")
    f.write("\nTop 5 IP :\n")
    for ip, count in Counter(ips).most_common(5):
        f.write(f"{count}  {ip}\n")
    f.write("\nTop 5 pages :\n")
    for page, count in Counter(pages).most_common(5):
        f.write(f"{count}  {page}\n")

print(f"✅ Rapport généré : {rapport}")