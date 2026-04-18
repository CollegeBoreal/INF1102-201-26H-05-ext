<img width="1920" height="1080" alt="Screenshot (368)" src="https://github.com/user-attachments/assets/04d9d331-d4a0-4071-b141-9adb5bf83b1f" />
<img width="1920" height="1080" alt="Screenshot (367)" src="https://github.com/user-attachments/assets/b4e47ec3-2c82-4d2c-be29-804dcaa666ca" />
# 🐧 Linux — Gestionnaire de tâches & Observateur d'évènements

> **Nom :** Ouail Gacem  
> **Matricule :** 300148094  
> **Cours :** Programmation système — Administration Linux

---

## 📋 Table des matières

1. [Objectif du laboratoire](#objectif-du-laboratoire)
2. [Notions théoriques](#notions-théoriques)
3. [Travail réalisé](#travail-réalisé)
   - [Étape 1 — Comprendre le fichier access.log](#étape-1--comprendre-le-fichier-accesslog)
   - [Étape 2 — Extraire les IP avec Linux](#étape-2--extraire-les-ip-avec-linux)
   - [Étape 3 — Créer le script shell](#étape-3--créer-le-script-shell)
   - [Étape 4 — Automatiser avec cron](#étape-4--automatiser-avec-cron)
   - [Étape 5 — Bonus : IP les plus fréquentes](#étape-5--bonus--ip-les-plus-fréquentes)
4. [Résumé des commandes](#résumé-des-commandes)
5. [Conclusion](#conclusion)

---

## 🎯 Objectif du laboratoire

L'objectif de ce laboratoire est de **surveiller le système Linux en temps réel** et d'**analyser les événements après coup** à l'aide des logs.

Plus précisément, j'ai dû :

- Scruter les logs du serveur web **Nginx**
- Extraire automatiquement les **adresses IP des visiteurs**
- Stocker ces IP dans un fichier
- **Automatiser** la tâche avec **CRON** pour qu'elle s'exécute toutes les heures

---

## 📚 Notions théoriques

### 🔹 Gestionnaire de tâches (temps réel)

Pour surveiller les processus en cours d'exécution sur le système :

```bash
top          # Gestionnaire basique
htop         # Version améliorée (recommandée)
ps aux       # Liste complète des processus
```

Pour stopper un processus :

```bash
kill PID       # Arrêt normal
kill -9 PID    # Arrêt forcé
```

Pour surveiller les ressources :

```bash
uptime    # Charge du système
free -h   # Mémoire disponible
df -h     # Espace disque
```

---

### 🔹 Observateur d'événements (logs)

Les logs permettent de comprendre ce qui s'est passé **après coup**.

| Emplacement | Contenu |
|-------------|---------|
| `/var/log/syslog` | Logs système généraux |
| `/var/log/auth.log` | Authentifications / connexions SSH |
| `dmesg` | Messages du noyau Linux |
| `journalctl` | Logs des services systemd |

```bash
journalctl -u nginx    # Logs du service nginx
journalctl -xe         # Logs détaillés avec erreurs
```

---

### 🔹 CRON — Planificateur de tâches

CRON est un service Unix/Linux qui permet d'**exécuter des tâches automatiquement** à des moments précis.

**Structure d'une ligne cron :**

```
* * * * * commande
| | | | |
| | | | └── Jour de la semaine (0-7, 0=dimanche)
| | | └──── Mois (1-12)
| | └────── Jour du mois (1-31)
| └──────── Heure (0-23)
└────────── Minute (0-59)
```

**Exemples :**

```bash
15 3 * * *   /home/user/backup.sh    # Tous les jours à 3h15
*/5 * * * *  /usr/bin/script.sh     # Toutes les 5 minutes
0 * * * *    /home/user/script.sh   # Toutes les heures (à la minute 0)
```

---

## 🛠️ Travail réalisé

### Étape 1 — Comprendre le fichier access.log

Nginx enregistre toutes les requêtes dans le fichier :

```
/var/log/nginx/access.log
```

J'ai d'abord regardé le contenu du fichier pour comprendre sa structure :

```bash
cat /var/log/nginx/access.log
```

Une ligne typique ressemble à ceci :

```
192.168.1.15 - - [05/Feb/2026:15:20:11 +0000] "GET /index.html HTTP/1.1" 200 1024 "-" "Mozilla/5.0 ..."
```

| Champ | Valeur | Signification |
|-------|--------|---------------|
| `192.168.1.15` | IP | Adresse du visiteur |
| `05/Feb/2026:15:20:11` | Date/Heure | Moment de la requête |
| `GET /index.html` | Requête | Page demandée |
| `200` | Code HTTP | Succès |
| `1024` | Taille | Taille de la réponse en octets |

> 💡 Je me concentre sur la **première colonne** qui contient l'adresse IP du visiteur.

---

### Étape 2 — Extraire les IP avec Linux

**a) Extraire la première colonne (les IP) avec `awk` :**

```bash
awk '{print $1}' /var/log/nginx/access.log
```

`$1` désigne la première colonne de chaque ligne, soit l'adresse IP.

**b) Trier et supprimer les doublons :**

```bash
awk '{print $1}' /var/log/nginx/access.log | sort | uniq
```

- `sort` → trie les IP par ordre alphabétique
- `uniq` → supprime les adresses IP en double

**c) Sauvegarder dans un fichier :**

```bash
awk '{print $1}' /var/log/nginx/access.log | sort | uniq > /home/ubuntu/nginx_ips.txt
```

J'ai ensuite vérifié le contenu du fichier créé :

```bash
cat /home/ubuntu/nginx_ips.txt
```

---

### Étape 3 — Créer le script shell

Pour automatiser l'extraction, j'ai créé un script shell :

```bash
nano /home/ubuntu/scruter_nginx.sh
```

Voici le contenu du script que j'ai écrit :

```bash
#!/bin/bash

# Fichier des logs Nginx
LOG_FILE="/var/log/nginx/access.log"

# Fichier de sortie pour les IP
OUTPUT_FILE="/home/ubuntu/nginx_ips.txt"

# Extraire les IP uniques et les stocker
awk '{print $1}' $LOG_FILE | sort | uniq > $OUTPUT_FILE

# Ajouter un timestamp à chaque exécution dans un fichier de journal
echo "Script exécuté le $(date)" >> /home/ubuntu/nginx_ips.log
```

Ensuite, j'ai rendu le script **exécutable** :

```bash
chmod +x /home/ubuntu/scruter_nginx.sh
```

J'ai testé le script manuellement pour vérifier qu'il fonctionne :

```bash
/home/ubuntu/scruter_nginx.sh
cat /home/ubuntu/nginx_ips.txt
```

---

### Étape 4 — Automatiser avec cron

Pour que le script s'exécute **toutes les heures automatiquement**, j'ai ouvert l'éditeur de crontab :

```bash
crontab -e
```

J'ai ajouté la ligne suivante à la fin du fichier :

```
0 * * * * /home/ubuntu/scruter_nginx.sh
```

> `0 * * * *` signifie : à la **minute 0** de chaque heure → toutes les heures.

Pour vérifier que la tâche est bien enregistrée :

```bash
crontab -l
```

Pour vérifier que le service cron est actif :

```bash
systemctl status cron
```

---

### Étape 5 — Bonus : IP les plus fréquentes

Pour identifier les visiteurs les plus actifs (et détecter d'éventuels robots ou attaques), j'ai utilisé :

```bash
awk '{print $1}' /var/log/nginx/access.log | sort | uniq -c | sort -nr > /home/ubuntu/nginx_ips_freq.txt
```

- `uniq -c` → compte le nombre d'apparitions de chaque IP
- `sort -nr` → trie par fréquence, du plus grand au plus petit

Résultat dans le fichier `nginx_ips_freq.txt` — exemple de contenu :

```
  152 10.7.237.226
   87 192.168.1.15
   34 172.16.0.5
    3 10.0.0.1
```

> La première IP a visité le site 152 fois — à surveiller !

---

## 📊 Résumé des commandes

| Commande | Description |
|----------|-------------|
| `awk '{print $1}' access.log` | Extraire la première colonne (IP) |
| `sort \| uniq` | Trier et supprimer les doublons |
| `uniq -c` | Compter les occurrences de chaque IP |
| `sort -nr` | Trier par fréquence décroissante |
| `chmod +x script.sh` | Rendre un script exécutable |
| `crontab -e` | Modifier les tâches planifiées |
| `crontab -l` | Afficher les tâches planifiées |
| `systemctl status cron` | Vérifier l'état du service cron |
| `journalctl -u nginx` | Voir les logs du service Nginx |

---

## ✅ Méthode de dépannage

| Étape | Outil utilisé |
|-------|---------------|
| Observer en temps réel | `top`, `htop` |
| Vérifier un service | `systemctl status nginx` |
| Analyser la cause | `journalctl`, `/var/log/nginx/` |
| Corriger le problème | Modifier la config, redémarrer le service |

---

## 💬 Conclusion

Grâce à ce laboratoire, j'ai appris à :

- Lire et analyser les **logs Nginx** pour identifier les visiteurs
- Utiliser **`awk`, `sort`, `uniq`** pour extraire et filtrer des données
- Écrire un **script shell** automatisé et le rendre exécutable
- Planifier l'exécution automatique avec **CRON**
- Détecter les IP les plus fréquentes pour surveiller l'activité du serveur

> 🔑 *Temps réel = performance* | *Logs = diagnostic* | *Toujours utiliser les deux ensemble.*

---

*Ouail Gacem — 300148094*
