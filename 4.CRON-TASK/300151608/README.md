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

## Automatisation<img width="960" height="1020" alt="mooh222" src="https://github.com/user-attachments/assets/dd5f977c-4f5f-4898-8060-003fb9055387" />
<img width="960" height="1020" alt="mooh3" src="https://github.com/user-attachments/assets/6fdf833e-7a0d-471f-a39c-27de3bb8ddab" />


0 * * * * ./scruter_nginx.sh

## Résultat

Les fichiers générés :
- nginx_ips.txt
- nginx_ips_freq.txt<img width="960" height="1020" alt="mooh" src="https://github.com/user-attachments/assets/2fc97430-740f-4700-bd40-d41032b30f57" />

