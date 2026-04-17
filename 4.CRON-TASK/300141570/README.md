# 🕒 CRON-TASK – Surveillance des logs Nginx

## 🎯 Objectif
Dans ce travail, nous avons appris à utiliser **CRON** sous Linux pour automatiser l’exécution de tâches. L’objectif est d’analyser les logs du serveur web Nginx afin d’extraire les adresses IP des visiteurs.

---

## ⚙️ Script utilisé

Nous avons créé un script nommé `scruter_nginx.sh` :

```bash
#!/bin/bash

LOG_FILE="/var/log/nginx/access.log"
OUTPUT_FILE="/home/ubuntu/nginx_ips.txt"

awk '{print $1}' $LOG_FILE | sort | uniq > $OUTPUT_FILE
echo "Script exécuté le $(date)" >> /home/ubuntu/nginx_ips.log

