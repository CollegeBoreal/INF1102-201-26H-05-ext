# TP CRON – Analyse des logs Nginx

## Objectif
Extraire les adresses IP des visiteurs à partir du fichier access.log et automatiser la tâche.

## Script
Le script `scruter_nginx.sh` permet :
- d’extraire les IP
- supprimer les doublons
- compter les IP fréquentes

## Commandes utilisées

awk '{print $1}' /var/log/nginx/access.log | sort | uniq

## Automatisation

0 * * * * ./scruter_nginx.sh

## Résultat

Les fichiers générés :
- nginx_ips.txt
- nginx_ips_freq.txt
