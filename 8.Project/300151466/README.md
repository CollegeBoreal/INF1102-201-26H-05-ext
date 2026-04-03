# 🚀 Projets INF1102 — Adel Bennacer (300151466)

**Environnement :** Ubuntu 22.04 LTS | **Cours :** INF1102

---

## 📋 Sommaire

| Projet | Description |
|--------|-------------|
| Projet 5 — Monitoring Web | Vérifie la disponibilité de sites web et mesure le temps de réponse |
| Projet Gobuster — VM Scanner | Scanner automatique des VMs Proxmox avec Gobuster |

---

# Projet 5 — Monitoring de sites web

## Objectif
Vérifier la disponibilité des sites web et mesurer leur temps de réponse avec Bash + Python.

## Structure
projet5-monitoring/
- scripts/analyse.sh
- scripts/analyse.py
- data/sample.log
- output/rapport.txt

## Exécution
bash projet5-monitoring/scripts/analyse.sh

## Résultats
===== RAPPORT MONITORING =====
Date : 2026-03-27

https://google.com       | 301 | 339ms | OK
https://github.com       | 200 | 489ms | OK
https://collegeboreal.ca | 200 | 218ms | OK
https://example.com      | 200 | 190ms | OK
https://httpstat.us/404  | 000 | 236ms | ERREUR

===== ANALYSE =====
Total : 5
OK    : 3
Erreur: 2
Moyenne: 294 ms

## Cron
0 * * * * bash /home/ubuntu/INF1102-201-26H-05/8.Project/300151466/projet5-monitoring/scripts/analyse.sh

---

# Projet Gobuster — VM Scanner

## Objectif
Scanner les VMs Proxmox pour détecter les serveurs web.

## Structure
projet-gobuster/
- scripts/gobuster_all_vms.sh
- data/sample.log
- output/rapport.txt

## Exécution
bash projet-gobuster/scripts/gobuster_all_vms.sh

## Résultats
10.7.237.226 → index.html
10.7.237.229 → index.html
10.7.237.239 → index.html, script.js

---

# Références Bash

mkdir -p → créer dossier  
cp -r → copier  
tar -czvf → compresser  
ping → tester réseau  
curl → tester site  
gobuster → scanner  
crontab -e → planifier  
date → timestamp  

---

# Conclusion
Projet permettant :
- monitoring web
- analyse réseau
- scan automatique
- automatisation avec cron
