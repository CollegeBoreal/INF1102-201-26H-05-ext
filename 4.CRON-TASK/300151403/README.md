#JUSTIN SANDY
![Crontab](images/Crontab.png)
# Exercice : Scruter les logs Nginx et détecter les IP des visiteurs

## 1️⃣ 👁️ Big Brother

Nginx, serveur web très populaire, enregistre toutes les requêtes dans des **fichiers de logs**. Il existe principalement deux types de logs :

* **access.log** : contient toutes les requêtes reçues (pages visitées, adresses IP, statut HTTP…).
* **error.log** : contient les erreurs du serveur.

**Objectif de l'exercice :**

* Extraire toutes les **adresses IP** qui visitent le site.
* Stocker ces IP dans un fichier.
* Automatiser la tâche pour qu’elle s’exécute **toutes les heures**.

---

## 2️⃣ Comprendre le fichier `access.log`

Le fichier se trouve généralement ici :

```bash
/var/log/nginx/access.log
```

Un exemple de ligne typique :

```
192.168.1.15 - - [05/Feb/2026:15:20:11 +0000] "GET /index.html HTTP/1.1" 200 1024 "-" "Mozilla/5.0 ..."
```

* **10.7.237.226** → adresse IP du visiteur
* **[05/Feb/2026:15:20:11 +0000]** → date et heure
* **GET /index.html** → ressource demandée
* **200** → code HTTP
* **1024** → taille de la réponse

On se concentre sur **la première colonne**, qui est l’IP.

---

## 3️⃣ Extraire les IP avec Linux

### a) Utilisation de `awk`

```bash
awk '{print $1}' /var/log/nginx/access.log
```

* `$1` → première colonne (IP)

### b) Filtrer les doublons avec `sort` et `uniq`

```bash
awk '{print $1}' /var/log/nginx/access.log | sort | uniq
```

* `sort` → trie les IP
* `uniq` → supprime les doublons

### c) Ajouter à un fichier

```bash
awk '{print $1}' /var/log/nginx/access.log | sort | uniq > /home/ubuntu/nginx_ips.txt
```

Maintenant, toutes les IP uniques sont dans `nginx_ips.txt`.

---

## 4️⃣ Créer un script shell automatisé

1. Créer un fichier `scruter_nginx.sh` :

```bash
nano /home/ubuntu/scruter_nginx.sh
```

2. Ajouter le contenu suivant :

```bash
#!/bin/bash

# Fichier des logs
LOG_FILE="/var/log/nginx/access.log"

# Fichier de sortie
OUTPUT_FILE="/home/ubuntu/nginx_ips.txt"

# Extraire les IP uniques et les stocker
awk '{print $1}' $LOG_FILE | sort | uniq > $OUTPUT_FILE

# Optionnel : ajouter un timestamp à chaque exécution
echo "Script exécuté le $(date)" >> /home/ubuntu/nginx_ips.log
```

3. Rendre le script exécutable :

```bash
chmod +x /home/ubuntu/scruter_nginx.sh
```

4. Tester le script :

```bash
/home/ubuntu/scruter_nginx.sh
cat /home/ubuntu/nginx_ips.txt
```

---

## 5️⃣ Automatiser avec cron (toutes les heures)

1. Éditer le crontab de l’utilisateur :

```bash
crontab -e
```

2. Ajouter la ligne suivante pour exécuter le script toutes les heures :

```cron
0 * * * * /home/ubuntu/scruter_nginx.sh
```

* `0 * * * *` → à la minute 0 de chaque heure
* `/home/ubuntu/scruter_nginx.sh` → chemin du script

3. Vérifier que le cron est bien actif :

```bash
systemctl status cron
```

---

## 6️⃣ Bonus : IP les plus fréquentes

Pour détecter les **visiteurs les plus actifs** :

```bash
awk '{print $1}' /var/log/nginx/access.log | sort | uniq -c | sort -nr > /home/ubuntu/nginx_ips_freq.txt
```

* `uniq -c` → compte le nombre d’occurrences
* `sort -nr` → trie par fréquence décroissante

---

## 7️⃣ Résumé des commandes clés

| Commande                      | Description                          |                                 |
| ----------------------------- | ------------------------------------ | ------------------------------- |
| `awk '{print $1}' access.log` | Extraire la première colonne (IP)    |                                 |
| `sort                         | uniq`                                | Trier et supprimer les doublons |
| `uniq -c`                     | Compter les occurrences              |                                 |
| `crontab -e`                  | Programmer le script automatiquement |                                 |
| `chmod +x script.sh`          | Rendre le script exécutable          |                                 |




