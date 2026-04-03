#!/bin/bash

# Fichier des logs Nginx
LOG_FILE="/var/log/nginx/access.log"

# Fichier de sortie contenant les IP uniques
OUTPUT_FILE="/home/ubuntu/nginx_ips.txt"

# Extraire les adresses IP uniques
awk '{print $1}' $LOG_FILE | sort | uniq > $OUTPUT_FILE

# Ajouter une trace d’exécution avec la date
echo "Script exécuté le $(date)" >> /home/ubuntu/nginx_ips.log