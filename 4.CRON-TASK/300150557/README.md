# 🔍 Exercice : Scruter les logs Nginx



## 📋 Informations de l'étudiant



| Champ | Valeur |

|---|---|

| \*\*Numéro Boréal\*\* | 300150557 |

| \*\*Adresse IP de la VM\*\* | 10.7.237.234 |



---



## 🎯 Objectif



Extraire automatiquement les adresses IP des visiteurs à partir des logs Nginx, puis automatiser cette tâche grâce à `cron`.



---



## 📁 Structure du projet



```

\~/

├── scruter\_nginx.sh       # Script principal d'extraction

├── nginx\_ips.txt          # Liste des IPs extraites

├── nginx\_ips.log          # Journal d'exécution du script

└── nginx\_cron.log         # Journal des exécutions cron

```



---



## 📝 Script : `scruter\_nginx.sh`



### Création du fichier



```bash

nano /home/ubuntu/scruter\_nginx.sh

```


### Contenu du script



```bash

\#!/bin/bash

LOG\_FILE="/var/log/nginx/access.log"

OUTPUT\_FILE="/home/ubuntu/nginx\_ips.txt"



awk '{print $1}' $LOG\_FILE | sort | uniq > $OUTPUT\_FILE

echo "Script exécuté le $(date)" >> /home/ubuntu/nginx\_ips.log

```



### Attribution des permissions



```bash

chmod +x /home/ubuntu/scruter\_nginx.sh

```



---



## ⏰ Configuration Cron



Exécution automatique \*\*toutes les heures\*\* (à la minute 0) :



```bash

crontab -e

```



Ajouter la ligne suivante :



```

0 \* \* \* \* /home/ubuntu/scruter\_nginx.sh >> /home/ubuntu/nginx\_cron.log 2>\&1

```



---



## ✅ Vérification



### Consulter les tâches cron actives



```bash

crontab -l

```



### Tester le script manuellement



```bash

/home/ubuntu/scruter\_nginx.sh

```



### Afficher les IPs extraites



```bash

cat /home/ubuntu/nginx\_ips.txt

```



### Consulter le journal d'exécution



```bash

cat /home/ubuntu/nginx\_ips.log

```



---



## 🧠 Explication des commandes



| Commande | Rôle |

|---|---|

| `awk '{print $1}'` | Extrait la \*\*1ère colonne\*\* de chaque ligne (l'adresse IP) |

| `sort` | \*\*Trie\*\* les adresses IP par ordre croissant |

| `uniq` | \*\*Supprime les doublons\*\* consécutifs |

| `>> fichier` | \*\*Ajoute\*\* la sortie à la fin du fichier (sans écraser) |

| `> fichier` | \*\*Écrase\*\* le fichier avec la nouvelle sortie |



---



## 📸 Preuves



### 1. Création et contenu du script



[Création du script](images/1.png)



### 2. Permissions et test d'exécution



[Permissions et test](images/2.png)



### 3. Configuration cron



[Configuration cron](images/3.png)



### 4. Résultats — IPs extraites



[IPs extraites](images/4.png)



---



> \*Document produit dans le cadre du cours d'administration système — Collège Boréal\*

