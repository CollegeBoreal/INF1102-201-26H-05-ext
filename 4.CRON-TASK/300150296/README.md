\# CRON-TASK - Surveillance Nginx - 300150296



\## 👤 Étudiant

\*\*Nom\*\* : Youba Bouanani  

\*\*ID\*\* : 300150296  

\*\*VM\*\* : vm300150296 (10.7.237.232)



\## 🎯 Objectif

Surveiller les logs Nginx et extraire automatiquement les adresses IP des visiteurs à l'aide d'un script CRON.



\## 📋 Tâches réalisées



\### 1. Installation de Nginx

```bash

sudo apt update

sudo apt install nginx -y

sudo systemctl start nginx

sudo systemctl enable nginx

```



\### 2. Création du script de surveillance

Script : `/home/ubuntu/scruter\_nginx.sh`



Le script extrait :

\- Les IP uniques dans `nginx\_ips.txt`

\- Les IP avec fréquence dans `nginx\_ips\_freq.txt`

\- Un log d'exécution dans `nginx\_ips.log`



\### 3. Automatisation avec CRON

Tâche planifiée : \*\*Toutes les heures\*\* (à la minute 0)

```bash

crontab -e

0 \* \* \* \* /home/ubuntu/scruter\_nginx.sh

```



\## 📊 Résultats



\### Nginx en fonctionnement

!\[Nginx Status](images/nginx\_status.png)



\### IP extraites

!\[IP List](images/nginx\_ips.png)



\### IP avec fréquence

!\[IP Frequency](images/nginx\_ips\_freq.png)



\### CRON configuré

!\[CRON Tab](images/crontab.png)



\## 🔧 Commandes utilisées



| Commande | Description |

|----------|-------------|

| `awk '{print $1}' access.log` | Extraire les IP |

| `sort \\| uniq` | Supprimer les doublons |

| `uniq -c` | Compter les occurrences |

| `crontab -e` | Éditer les tâches CRON |

| `systemctl status nginx` | Vérifier Nginx |



\## ✅ Vérification



Le script s'exécute automatiquement toutes les heures et met à jour les fichiers de résultats.

