\# Exercice : Scruter les logs Nginx

\## 300150268



\## 🎯 Objectif

Extraire les adresses IP des visiteurs du serveur Nginx et automatiser avec cron.



\## 📁 Script : scruter\_nginx.sh



\#!/bin/bash

LOG\_FILE="/var/log/nginx/access.log"

OUTPUT\_FILE="/home/ubuntu/nginx\_ips.txt"

awk '{print $1}' $LOG\_FILE | sort | uniq > $OUTPUT\_FILE

echo "Script exécuté le $(date)" >> /home/ubuntu/nginx\_ips.log



\## ⚙️ Configuration Cron

0 \* \* \* \* /home/ubuntu/scruter\_nginx.sh >> /home/ubuntu/nginx\_cron.log 2>\&1



\## 📊 Résultats

Fichier généré : nginx\_ips.txt

IP détectée : 10.7.237.230



\## 🔍 Vérification

crontab -l

systemctl status cron

cat /home/ubuntu/nginx\_ips.txt

