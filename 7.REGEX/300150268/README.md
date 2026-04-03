\# 7.REGEX — Analyse des logs Nginx avec Expressions Régulières

\## 300150268 | IP: 10.7.237.230



\## 🎯 Objectif

Utiliser des expressions régulières pour analyser les logs Nginx.



\## 📂 Structure

7.REGEX/300150268/

├── analyse\_nginx.ps1

├── analyse\_nginx.py

├── rapport\_nginx\_ps1\_2026-04-03.txt

├── rapport\_nginx\_py\_2026-04-03.txt

├── README.md

└── images/



\## 🔍 Regex utilisées

\- IP : (\\d{1,3}(\\.\\d{1,3}){3})

\- Code HTTP : " (\\d{3}) "

\- Pages GET : "GET (\[^ ]+)

\- Erreurs 4xx/5xx : ^\[45]



\## 📊 Résultats

\- Total requêtes : 7

\- Erreurs HTTP (4xx/5xx) : 6

\- Erreurs 404 : 6

\- Erreurs 500 : 0

\- Top IP : 10.7.237.230

\- Top pages : /, /admin, /index.html, /login, /images/logo.png



\## ▶️ Exécution

pwsh ./analyse\_nginx.ps1

python3 ./analyse\_nginx.py



\## ⏰ Cron

0 2 \* \* \* /usr/bin/pwsh \~/INF1102-201-26H-05/7.REGEX/300150268/analyse\_nginx.ps1

5 2 \* \* \* /usr/bin/python3 \~/INF1102-201-26H-05/7.REGEX/300150268/analyse\_nginx.py

