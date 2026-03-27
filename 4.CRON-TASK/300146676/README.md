# 4.CRON-TASK — 300146676

## Description
Ce travail consiste à analyser les logs Nginx, extraire les adresses IP des visiteurs, enregistrer le résultat dans un fichier, puis automatiser cette tâche avec `cron`.

## Objectifs
- Lire le fichier `access.log` de Nginx
- Extraire les adresses IP des visiteurs
- Enregistrer les IP uniques dans un fichier texte
- Journaliser l’exécution du script
- Automatiser l’exécution toutes les heures avec `cron`

## Fichiers du projet
- `scruter_nginx.sh` : script shell principal
- `images/` : captures d’écran de preuve
- `README.md` : explication du travail

## Script utilisé
Le script lit le fichier `/var/log/nginx/access.log`, extrait la première colonne contenant les IP, trie les résultats, supprime les doublons et enregistre la sortie dans `nginx_ips.txt`.

Exemple de logique utilisée :

```bash
awk '{print $1}' /var/log/nginx/access.log | sort | uniq > ~/nginx_ips.txt

Automatisation avec cron

Le script a été planifié avec cron pour s’exécuter automatiquement toutes les heures avec la ligne suivante :

0 * * * * /home/aymen/scruter_nginx.sh
Vérifications effectuées

Les commandes suivantes ont permis de vérifier le bon fonctionnement :

cat ~/nginx_ips.txt
cat ~/nginx_ips.log
crontab -l
systemctl status cron
Résultat

Le script fonctionne correctement et permet :

d’extraire les IP des visiteurs
de stocker les IP uniques dans un fichier
de garder une trace d’exécution
d’automatiser la tâche avec cron
Auteur
## Numéro d’identification : 300146676

