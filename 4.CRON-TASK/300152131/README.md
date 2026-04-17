# 👤 Informations étudiant

| Champ | Détails |
|-------|---------|
| **Nom** | Calvin |
| **Matricule** | 300152131 |
| **Cours** | Programmation des systèmes |

---

# 🔍 Scruter les logs Nginx et détecter les IP des visiteurs

## 🎯 Objectif

> Extraire automatiquement toutes les adresses IP qui visitent un site via les logs Nginx, stocker les résultats et automatiser l'exécution toutes les heures.

| Fonctionnalité | Détail |
|----------------|--------|
| 📄 Source | `/var/log/nginx/access.log` |
| 💾 Sortie | Liste d'IP uniques dans un fichier texte |
| ⏱️ Automatisation | Cron — toutes les heures |

---

## 📁 Structure du projet

```
/home/ubuntu/
├── scruter_nginx.sh       # Script principal
├── nginx_ips.txt          # Liste des IP uniques (sortie)
└── nginx_ips.log          # Journal d'exécution (timestamps)
```

---

## ✅ Prérequis

- Système Linux avec **Nginx** installé
- Accès en lecture à `/var/log/nginx/access.log`
- Droits d'exécuter des scripts et d'éditer la crontab

> **Emplacements des logs Nginx :**
> - `access.log` → `/var/log/nginx/access.log`
> - `error.log` → `/var/log/nginx/error.log`

---

## 📚 Format du fichier `access.log`

Exemple de ligne de log :

```
192.168.1.15 - - [05/Feb/2026:15:20:11 +0000] "GET /index.html HTTP/1.1" 200 1024 "-" "Mozilla/5.0 ..."
```

| Champ | Valeur |
|-------|--------|
| 🌐 IP | `192.168.1.15` (1ʳᵉ colonne) |
| 📅 Date/Heure | `05/Feb/2026:15:20:11 +0000` |
| 📨 Requête | `GET /index.html` |
| ✅ Code HTTP | `200` |
| 📦 Taille | `1024 octets` |

---

## 🚀 Installation & Mise en route

### Étape 1 — Créer le script

```bash
nano /home/ubuntu/scruter_nginx.sh
```

Coller le contenu suivant :

```bash
#!/bin/bash
# Fichier des logs
LOG_FILE="/var/log/nginx/access.log"
# Fichier de sortie
OUTPUT_FILE="/home/ubuntu/nginx_ips.txt"

# Extraire les IP uniques et les stocker
awk '{print $1}' $LOG_FILE | sort | uniq > $OUTPUT_FILE

# Ajouter un timestamp à chaque exécution
echo "Script exécuté le $(date)" >> /home/ubuntu/nginx_ips.log
```

---

### Étape 2 — Rendre le script exécutable

```bash
chmod +x /home/ubuntu/scruter_nginx.sh
```

---

### Étape 3 — Tester le script

```bash
/home/ubuntu/scruter_nginx.sh
cat /home/ubuntu/nginx_ips.txt
```

---

## ⏱️ Automatisation avec Cron

### Étape 4 — Configurer la crontab

Ouvrir la crontab :

```bash
crontab -e
```

Ajouter la ligne suivante pour exécuter le script **toutes les heures** :

```cron
# Exécute à la minute 0 de chaque heure
0 * * * * /home/ubuntu/scruter_nginx.sh
```

![Code ajouté dans crontab](images/code%20dans%20crontab.png)

---

### Étape 5 — Copie du script dans le répertoire

Vérification que le fichier `.sh` est bien présent dans le répertoire de travail :

![Copie du fichier .sh dans le répertoire](images/copie%20du%20fichier%20.sh%20dans%20mon%20repertoire.png)

---

### Étape 6 — Vérification du service Cron

Confirmer que le service `cron` est actif et tourne correctement :

```bash
systemctl status cron
```

![Service cron bien actif](images/Service%20cron%20bien%20actif.png)

---

## 🧠 Résumé des commandes clés

| Commande | Rôle |
|----------|------|
| `crontab -e` | Éditer les tâches planifiées |
| `chmod +x script.sh` | Rendre un script exécutable |
| `systemctl status cron` | Vérifier l'état du service cron |
| `awk '{print $1}'` | Extraire la 1ʳᵉ colonne (IP) du log |
| `sort \| uniq` | Dédoublonner les IP |
