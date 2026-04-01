#!/bin/bash

# Fichier des logs Nginx
LOG_FILE="/var/log/nginx/access.log"

# Fichier de sortie avec les IP
OUTPUT_FILE="/home/ubuntu/nginx_ips.txt"

# Extraire les IP uniques et les stocker
awk '{print $1}' $LOG_FILE | sort | uniq > $OUTPUT_FILE

# Ajouter un timestamp à chaque exécution
echo "Script exécuté le $(date)" >> /home/ubuntu/nginx_ips.log

