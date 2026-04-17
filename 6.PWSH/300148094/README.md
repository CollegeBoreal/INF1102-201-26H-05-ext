⚙️ DevOps Batch System Monitor (PowerShell on Linux)

ID Projet : 300148094






🎯 Overview

Ce projet est un script d’automatisation DevOps développé en PowerShell (pwsh) sur Linux.

Il permet de surveiller le système et de générer automatiquement des rapports structurés en format texte et JSON.

🚀 Features

✔ Surveillance système (CPU, Mémoire, Disque)
✔ Vérification de connectivité réseau (SSH)
✔ Génération automatique de rapports (TXT + JSON)
✔ Utilisation du pipeline orienté objets (PowerShell)
✔ Script DevOps cross-platform (Linux / Windows)

📸 Exemple de sortie
===== RAPPORT DEVOPS =====
Date : 2026-04-13
Utilisateur : user
Machine : ubuntu

Top 5 processus CPU :
nginx - CPU: 25
python - CPU: 18

Espace disque :
/dev/sda1 40G 20G 50%

Test SSH :
Résultat : OK
📂 Structure du projet
/devops-batch/
├── devops_batch.ps1
├── rapport.txt
└── rapport.json
⚙️ Prérequis
Ubuntu 22.04 (ou similaire)
PowerShell Core (pwsh)
Client SSH installé
🔧 Installation
1. Installer PowerShell
sudo apt update
sudo apt install -y powershell
2. Créer le dossier du projet
sudo mkdir /devops-batch
3. Créer le script
sudo nano /devops-batch/devops_batch.ps1
▶️ Utilisation

Exécuter le script :

sudo pwsh /devops-batch/devops_batch.ps1
📊 Rapports générés

📄 Rapport texte

/devops-batch/rapport.txt

📦 Rapport JSON

/devops-batch/rapport.json
🧠 Exemple de pipeline PowerShell
Get-Process | Where-Object { $_.CPU -gt 10 } | Select-Object ProcessName, CPU

➡️ Contrairement à Bash, PowerShell manipule des objets et non du texte brut, ce qui rend l’automatisation plus fiable.

🔍 Vérifications effectuées
🖥️ Système
Top 5 processus CPU
Top 5 processus Mémoire
💾 Disque
Utilisation du disque (df -h)
🌐 Réseau
Test de connectivité SSH (localhost)
⏰ Automatisation (CRON)

Ajouter une tâche planifiée :

crontab -e

Puis :

0 2 * * * /usr/bin/pwsh /devops-batch/devops_batch.ps1

➡️ Exécution automatique tous les jours à 2h du matin

📈 Roadmap
 Alertes par email
 Dashboard de monitoring
 Intégration Prometheus / Grafana
 Export API
 Monitoring multi-machines
⚖️ Bash vs PowerShell
Feature	Bash	PowerShell
Type de données	Texte	Objets
JSON	Externe	Natif
Pipeline	Texte	Objet
Automatisation	Moyenne	Avancée
💡 Pourquoi PowerShell sur Linux ?
Script cross-platform (Linux + Windows)
Support natif du JSON
Pipelines plus propres
Meilleure maintenabilité pour DevOps
🤝 Contributing

Les contributions sont les bienvenues !

git fork
git checkout -b feature/new-feature
git commit -m "Add new feature"
git push origin feature/new-feature
📄 License

MIT License

👨‍💻 Auteur

Ouail Gacem
DevOps Lab — PowerShell Automation on Linux

⭐ Support

Si ce projet t’aide, n’hésite pas à laisser une ⭐ sur GitHub !
