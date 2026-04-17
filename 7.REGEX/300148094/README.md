📊 Nginx Log Analyzer

🔍 Analyse automatisée des logs Nginx avec Regex (PowerShell & Python)








🎯 Objectif

Ce projet permet d’analyser automatiquement les fichiers de logs Nginx à l’aide d’expressions régulières (Regex), puis de générer des rapports détaillés.

🚀 Fonctionnalités

✔ Analyse des requêtes HTTP
✔ Détection des erreurs (4xx, 5xx)
✔ Identification des IP les plus actives
✔ Analyse des pages les plus visitées
✔ Génération automatique de rapports
✔ Automatisation possible avec CRON

📸 Exemple de rapport

📊 Rapport Nginx - 2026-04-13

Total requêtes : 1500
Erreurs HTTP : 120
Erreurs 404 : 80
Erreurs 500 : 40

Top 5 IP :
120 192.168.1.1
95 10.0.0.5

Top 5 pages :
300 /index.html
210 /login

📂 Structure du projet

nginx-log-analyzer/

├── REGEX/
│   ├── analyse_nginx.ps1
│   ├── analyse_nginx.py
│   └── rapport_*.txt
├── logs/
│   └── access.log
├── README.md
└── .gitignore
📥 Entrée

Fichier de logs Nginx :

/var/log/nginx/access.log

Exemple de ligne :

192.168.1.10 - - [17/Mar/2026:14:32:10 +0000] "GET /index.html HTTP/1.1" 200 1024

📤 Sortie

Rapports générés automatiquement :

REGEX/rapport_nginx_ps1_YYYY-MM-DD.txt
REGEX/rapport_nginx_py_YYYY-MM-DD.txt

🧠 Regex utilisées

Élément	Expression régulière
Adresse IP	(\d{1,3}\.){3}\d{1,3}
Code HTTP	"\s(\d{3})
Pages (GET)	"GET ([^ ]+)
Erreurs HTTP	`"\s(4

⚡ Installation

🔧 Prérequis

Python 3.x
PowerShell Core (pwsh)
Linux / Windows / WSL

▶️ Utilisation

🟦 PowerShell

pwsh ./REGEX/analyse_nginx.ps1

🐍 Python

python3 REGEX/analyse_nginx.py

📊 Résultats

Chaque rapport contient :

📌 Total des requêtes

⚠️ Nombre d’erreurs HTTP

❌ Erreurs 404
💥 Erreurs 500

🌐 Top 5 IP

📄 Top 5 pages

⏰ Automatisation

🔁 CRON (Linux)

crontab -e

Ajouter :

0 2 * * * /usr/bin/pwsh /home/user/nginx-log-analyzer/REGEX/analyse_nginx.ps1
🔍 Vérification

grep CRON /var/log/syslog

🚀 Roadmap

 Export CSV / JSON
 Graphiques (matplotlib)
 Interface Web (Flask / FastAPI)
 Analyse en temps réel
 Détection d’attaques (DDoS, brute force)
 
🛠️ Technologies

🐍 Python 3

💻 PowerShell

🔍 Regex

🐧 Linux / Cron

🤝 Contribution

Les contributions sont les bienvenues !

git fork
git checkout -b feature/ma-feature
git commit -m "Ajout feature"
git push origin feature/ma-feature
📄 Licence

MIT License

👨‍💻 Auteur

Projet réalisé dans le cadre d’un TP en administration système & automatisation.

⭐ Support


Si ce projet t’aide, laisse une ⭐ sur GitHub !
<img width="1920" height="1080" alt="Screenshot (385)" src="https://github.com/user-attachments/assets/98b31e25-517f-47f1-8b2b-151bd2860c6c" />
<img width="1920" height="1080" alt="Screenshot (384)" src="https://github.com/user-attachments/assets/2ba31277-250f-4e34-af00-8005deef15bb" />


