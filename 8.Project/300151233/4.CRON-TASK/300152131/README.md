Scruter les logs Nginx et détecter les IP des visiteurs

🎯 Objectif

Extraire toutes les adresses IP qui visitent un site via les logs Nginx (access.log)
Stocker la liste d’IP dans un fichier
Automatiser l’exécution toutes les heures (cron)

-------------------------------------------------------------------------

📁 Structure du projet
/home/ubuntu/
├─ scruter_nginx.sh          # Script principal
├─ nginx_ips.txt             # Liste des IP uniques (sortie)
└─ nginx_ips.log             # Journal d’exécution du script (timestamp)

-------------------------------------------------------------------------

✅ Prérequis

Accès à un système Linux avec Nginx installé
Accès en lecture à /var/log/nginx/access.log
Droit d’exécuter des scripts et d’éditer la crontab utilisateur


Emplacement par défaut des logs Nginx :

access.log : /var/log/nginx/access.log
error.log  : /var/log/nginx/error.log

-------------------------------------------------------------------------

📚 Comprendre le format access.log
Exemple de ligne :
192.168.1.15 - - [05/Feb/2026:15:20:11 +0000] "GET /index.html HTTP/1.1" 200 1024 "-" "Mozilla/5.0 ..."


IP : 192.168.1.15 (1ʳᵉ colonne)
Date/heure : [05/Feb/2026:15:20:11 +0000]
Requête : GET /index.html
Code HTTP : 200
Taille : 1024

-------------------------------------------------------------------------

🚀 Installation & Mise en route

1. Créer le script
nano /home/ubuntu/scruter_nginx.sh


2. Coller le conteneu
#!/bin/bash
# Fichier des logs
LOG_FILE="/var/log/nginx/access.log"
# Fichier de sortie
OUTPUT_FILE="/home/ubuntu/nginx_ips.txt"
# Extraire les IP uniques et les stocker
awk '{print $1}' $LOG_FILE | sort | uniq > $OUTPUT_FILE
# Optionnel : ajouter un timestamp à chaque exécution
echo "Script exécuté le $(date)" >> /home/ubuntu/nginx_ips.log


3. Rendre executable le script
chmod +x /home/ubuntu/scruter_nginx.sh


4. Tester
/home/ubuntu/scruter_nginx.sh
cat /home/ubuntu/nginx_ips.txt

-------------------------------------------------------------------------

⏱️ Automatisation avec cron (toutes les heures)
Éditer la crontab utilisateur : crontab -e

Ajouter
# Exécute à la minute 0 de chaque heure
0 * * * * /home/ubuntu/scruter_nginx.sh
