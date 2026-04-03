\# 🚀 Projet 5 — Monitoring de sites web

\## 300150268 | IP: 10.7.237.230



\## 1. Objectif

Ce projet vérifie la disponibilité de plusieurs sites web et mesure leur temps de réponse via Bash + Python.



\## 2. Structure

projet5-monitoring/

├── scripts/

│   ├── analyse.sh       # Script Bash principal

│   └── analyse.py       # Script Python appelé par Bash

├── data/

│   └── sample.log       # Log généré automatiquement

├── output/

│   └── rapport.txt      # Rapport généré automatiquement

└── RAPPORT.ipynb        # Rapport Jupyter



\## 3. Sites testés

\- https://google.com

\- https://github.com

\- https://collegeboreal.ca

\- https://example.com

\- https://httpstat.us/404



\## 4. Exécution

bash projet5-monitoring/scripts/analyse.sh



\## 5. Résultats

\- google.com       | 301 | 340ms  | ✅ OK

\- github.com       | 200 | 513ms  | ✅ OK

\- collegeboreal.ca | 200 | 2489ms | ✅ OK

\- example.com      | 200 | 267ms  | ✅ OK

\- httpstat.us/404  | 000 | 1384ms | ❌ ERREUR



\## 6. Analyse

\- Total sites : 5

\- Sites OK : 4

\- Sites en erreur : 1

\- Temps moyen : 998 ms

