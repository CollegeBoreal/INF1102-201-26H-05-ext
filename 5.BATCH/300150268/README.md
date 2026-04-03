\# TP Batch – Automatisation d'administration

\## 300150268 | IP: 10.7.237.230



\## 🎯 Objectif

Automatiser la sauvegarde, création d'utilisateur, test réseau et journalisation avec un script Bash planifié par cron.



\## 📁 Structure /entreprise/

/entreprise/

├── data/

│   ├── fichier1.txt

│   └── fichier2.txt

├── backup/

│   ├── fichier1.txt

│   ├── fichier2.txt

│   └── backup\_2026-04-03.tar.gz

└── logs/

&#x20;   └── log.txt



\## 📄 Script : script\_gestion.sh

\- Test réseau : ping 8.8.8.8

\- Sauvegarde : cp -r /entreprise/data/\* /entreprise/backup/

\- Utilisateur temporaire : employe\_temp

\- Archive : tar -czvf backup\_YYYY-MM-DD.tar.gz



\## ⚙️ Cron configuré

0 2 \* \* \* /entreprise/script\_gestion.sh



\## 🔍 Vérification

\- sudo crontab -l

\- systemctl status cron

\- cat /entreprise/logs/log.txt

