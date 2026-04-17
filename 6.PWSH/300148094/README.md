DevOps Batch System Monitor (PowerShell on Linux)

Nom : Ouail Gacem
ID : 300148094
Cours : INF1102

🎯 Overview

Ce projet consiste à développer un script DevOps en PowerShell (pwsh) sous Linux permettant de :

Surveiller l’état du système
Tester la connectivité réseau (SSH)
Générer des rapports automatisés en TXT et JSON

Ce travail a été réalisé dans le cadre du laboratoire PowerShell sous Ubuntu 22.04.

🚀 Features

✔ Surveillance CPU (Top 5 processus)
✔ Surveillance mémoire (Top 5 processus)
✔ Vérification de l’espace disque
✔ Test de connectivité SSH (localhost)
✔ Génération automatique de rapports
✔ Utilisation du pipeline orienté objets PowerShell

📸 Exemple de sortie
===== RAPPORT DEVOPS =====
Date : 2026-03-27 01:35:45
Utilisateur : ubuntu
Machine : vm300150395

Top 5 processus par CPU :
rcu_sched - CPU: 615.44
systemd - CPU: 195.4

Top 5 processus par mémoire :
pwsh - Mémoire: 188960768

Espace disque :
/dev/sda1 9.6G 5.6G 4.0G 59%

Test SSH :
Résultat : OK
📂 Structure du projet
~/devops-batch/
├── rapport.txt
└── rapport.json

~/INF1102-201-26H-05/6.PWSH/300148094/
├── devops_batch.ps1
├── README.md
└── images/
⚙️ Prérequis
Ubuntu 22.04 LTS
PowerShell Core (pwsh)
SSH installé et configuré
🔧 Installation
1. Mettre à jour le système
sudo apt update
2. Installer les dépendances
sudo apt install -y wget apt-transport-https software-properties-common
3. Ajouter le dépôt Microsoft
wget https://packages.microsoft.com/config/ubuntu/22.04/packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
4. Installer PowerShell
sudo apt update
sudo apt install -y powershell
5. Lancer PowerShell
pwsh
▶️ Utilisation

Exécuter le script :

pwsh ./devops_batch.ps1
📊 Rapports générés

📄 Rapport texte :

~/devops-batch/rapport.txt

📦 Rapport JSON :

~/devops-batch/rapport.json
🧠 Exemple de pipeline PowerShell
Get-Process | Where-Object { $_.CPU -gt 10 } | Select-Object ProcessName, CPU

➡️ PowerShell manipule des objets, contrairement à Bash qui utilise du texte.

🔍 Vérifications effectuées
🖥️ Système
Top 5 processus CPU
Top 5 processus mémoire
💾 Disque
Utilisation du disque avec df -h
🌐 Réseau
Test SSH vers 127.0.0.1
🔐 Configuration SSH (Important)

Pour que le test SSH fonctionne :

1. Ajouter la clé du serveur
ssh-keyscan -H 127.0.0.1 >> ~/.ssh/known_hosts
2. Générer une clé SSH
ssh-keygen -t rsa -b 4096 -N "" -f ~/.ssh/id_rsa
3. Autoriser la clé
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
⏰ Automatisation (CRON)

Exécuter automatiquement le script chaque jour à 2h :

crontab -e

Ajouter :

0 2 * * * /usr/bin/pwsh /home/ubuntu/devops_batch.ps1
📈 Roadmap
 Alertes par email
 Dashboard de monitoring
 Intégration Prometheus / Grafana
 Monitoring multi-machines
⚖️ Bash vs PowerShell
Feature	Bash	PowerShell
Type	Texte	Objets
JSON	Externe	Natif
Pipeline	Texte	Objet
DevOps	Moyen	Avancé
💡 Pourquoi PowerShell sur Linux ?
Compatible Linux & Windows
Manipulation native du JSON
Pipelines plus puissants
Automatisation plus fiable
👨‍💻 Auteur

Ouail Gacem
DevOps Student — Collège Boréal

⭐ Support

Si ce projet t’aide, mets une ⭐ sur GitHub !

<img width="1920" height="1080" alt="Screenshot (381)" src="https://github.com/user-attachments/assets/bc598e2d-8fa3-4cfe-b699-cf137089438c" />
<img width="1920" height="1080" alt="Screenshot (380)" src="https://github.com/user-attachments/assets/0dc16c2a-f0b8-418d-8d3b-69fc63993097" />
<img width="1920" height="1080" alt="Screenshot (379)" src="https://github.com/user-attachments/assets/d5726dfe-5a5c-43c3-947a-0f7423acfe98" />
<img width="1920" height="1080" alt="Screenshot (382)" src="https://github.com/user-attachments/assets/eb5475e7-31f7-4989-854c-f05a7cc99245" />
<img width="998" height="474" alt="Screenshot 2026-04-17 013915" src="https://github.com/user-attachments/assets/5d063dae-b09c-4c09-9579-b250c696102f" />


