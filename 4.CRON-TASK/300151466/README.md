# Exercice : Scruter les logs Nginx

## 🎯 Objectif
Extraire les adresses IP des visiteurs du serveur Nginx et automatiser cette tâche avec cron.

## 📁 Fichier du script

### Contenu de `scruter_nginx.sh`
\`\`\`bash
#!/bin/bash

LOG_FILE="/var/log/nginx/access.log"
OUTPUT_FILE="/home/ubuntu/nginx_ips.txt"

awk '{print $1}' $LOG_FILE | sort | uniq > $OUTPUT_FILE
echo "Script exécuté le $(date)" >> /home/ubuntu/nginx_ips.log
\`\`\`

## ⚙️ Configuration Cron

Exécution toutes les heures (minute 0) :

0 * * * * /home/ubuntu/scruter_nginx.sh >> /home/ubuntu/nginx_cron.log 2>&1


## 📊 Résultats

### Fichier généré : `nginx_ips.txt`
Contient la liste des IP uniques ayant visité le serveur.

### Commandes utilisées
- `awk '{print $1}'` : extrait la première colonne (IP)
- `sort` : trie les IP
- `uniq` : supprime les doublons

## 🔍 Vérification

```bash
# Vérifier le cron
crontab -l

# Tester le script manuellement
./scruter_nginx.sh

# Voir le résultat
cat /home/ubuntu/nginx_ips.txt
```




