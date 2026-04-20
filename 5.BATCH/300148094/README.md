
# 🧪 TP — Automatisation d'administration avec script Batch (Linux)

> **Nom :** Ouail Gacem  
> **Matricule :** 300148094  
> **Cours :** Programmation système — Administration Linux

---

## 📋 Table des matières

1. [Objectif du laboratoire](#objectif-du-laboratoire)
2. [Environnement utilisé](#environnement-utilisé)
3. [Travail réalisé](#travail-réalisé)
   - [Partie 1 — Préparation de l'environnement](#partie-1--préparation-de-lenvironnement)
   - [Partie 2 — Création du script Batch](#partie-2--création-du-script-batch)
   - [Partie 3 — Rendre le script exécutable](#partie-3--rendre-le-script-exécutable)
   - [Partie 4 — Test manuel](#partie-4--test-manuel)
   - [Partie 5 — Planification avec Cron](#partie-5--planification-avec-cron)
   - [Partie 6 — Vérification de l'exécution](#partie-6--vérification-de-lexécution)
   - [Partie 7 — Dépannage](#partie-7--dépannage)
   - [Partie 8 — Améliorations avancées](#partie-8--améliorations-avancées)
4. [Diagramme avant / après exécution](#diagramme-avant--après-exécution)
5. [Résumé des commandes](#résumé-des-commandes)
6. [Conclusion](#conclusion)

---

## 🎯 Objectif du laboratoire

Dans ce TP, j'ai dû programmer un **script Bash** sous Linux permettant d'automatiser plusieurs tâches d'administration système :

- Sauvegarder un dossier d'entreprise
- Créer un utilisateur temporaire
- Tester la connectivité réseau
- Générer un fichier journal (log)
- Planifier l'exécution automatique avec **cron**
- Vérifier l'exécution et diagnostiquer les erreurs

---

## 🖥️ Environnement utilisé

- Distribution : **Ubuntu Server**
- Accès : **sudo**
- Terminal Linux
- Service **cron** actif

---

## 🛠️ Travail réalisé

### Partie 1 — Préparation de l'environnement

Avant d'écrire le script, j'ai créé la structure de dossiers nécessaire :

```bash
sudo mkdir -p /entreprise/data
sudo mkdir -p /entreprise/backup
sudo mkdir -p /entreprise/logs
```

- `/entreprise/data` → contient les fichiers à sauvegarder
- `/entreprise/backup` → destination des sauvegardes
- `/entreprise/logs` → contient le fichier journal

Ensuite, j'ai créé des fichiers de test dans le dossier `data` :

```bash
echo "Fichier 1" | sudo tee /entreprise/data/fichier1.txt
echo "Fichier 2" | sudo tee /entreprise/data/fichier2.txt
```

---

### Partie 2 — Création du script Batch

J'ai créé le fichier du script avec l'éditeur `nano` :

```bash
sudo nano /entreprise/script_gestion.sh
```

Voici le code complet que j'ai intégré dans le script :

```bash
#!/bin/bash

LOG="/entreprise/logs/log.txt"
DATE=$(date)

echo "===================================" >> $LOG
echo "Début exécution : $DATE" >> $LOG

# 1. Vérification réseau
echo "Test réseau..." >> $LOG
ping -c 4 8.8.8.8 >> $LOG 2>&1

# 2. Sauvegarde des fichiers
echo "Sauvegarde en cours..." >> $LOG
cp -r /entreprise/data/* /entreprise/backup/ >> $LOG 2>&1

# 3. Création utilisateur temporaire
USER_TEMP="employe_temp"

if id "$USER_TEMP" &>/dev/null; then
    echo "Utilisateur existe déjà." >> $LOG
else
    sudo useradd $USER_TEMP
    echo "$USER_TEMP:Temp1234" | sudo chpasswd
    echo "Utilisateur créé." >> $LOG
fi

# 4. Compression archive
tar -czvf /entreprise/backup/backup_$(date +%F).tar.gz /entreprise/data >> $LOG 2>&1

echo "Fin exécution : $(date)" >> $LOG
echo "===================================" >> $LOG
```

**Explication des sections du script :**

| Section | Rôle |
|---------|------|
| `LOG` et `DATE` | Variables pour le fichier log et la date courante |
| `ping -c 4 8.8.8.8` | Teste la connectivité internet (4 paquets vers Google DNS) |
| `cp -r /entreprise/data/*` | Copie tous les fichiers de `data` vers `backup` |
| `id "$USER_TEMP"` | Vérifie si l'utilisateur existe déjà avant de le créer |
| `useradd` + `chpasswd` | Crée l'utilisateur temporaire avec son mot de passe |
| `tar -czvf` | Crée une archive compressée `.tar.gz` datée du jour |
| `>> $LOG 2>&1` | Redirige toutes les sorties (et erreurs) vers le fichier log |

---

### Partie 3 — Rendre le script exécutable

Après avoir sauvegardé le script, je lui ai donné les permissions d'exécution :

```bash
sudo chmod +x /entreprise/script_gestion.sh
```

> Sans cette commande, Linux refuse d'exécuter le fichier.

---

### Partie 4 — Test manuel

J'ai exécuté le script manuellement pour vérifier qu'il fonctionne correctement :

```bash
sudo /entreprise/script_gestion.sh
```

Puis j'ai vérifié chaque résultat :

**Fichiers copiés dans le backup :**

```bash
ls /entreprise/backup/
```

**Archive `.tar.gz` créée :**

```bash
ls /entreprise/backup/*.tar.gz
```

**Utilisateur temporaire créé :**

```bash
cat /etc/passwd | grep employe_temp
```

**Contenu du fichier log :**

```bash
cat /entreprise/logs/log.txt
```

Exemple de contenu attendu dans le log :

```
===================================
Début exécution : Mon Feb  5 15:30:00 UTC 2026
Test réseau...
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
...
Sauvegarde en cours...
Utilisateur créé.
Fin exécution : Mon Feb  5 15:30:05 UTC 2026
===================================
```

---

### Partie 5 — Planification avec Cron

Pour que le script s'exécute **automatiquement tous les jours à 2h du matin**, j'ai édité la crontab root :

```bash
sudo crontab -e
```

J'ai ajouté la ligne suivante :

```
0 2 * * * /entreprise/script_gestion.sh
```

**Décodage de l'expression cron :**

```
0  2  *  *  *
│  │  │  │  └── Jour de la semaine (tous)
│  │  │  └───── Mois (tous)
│  │  └──────── Jour du mois (tous)
│  └─────────── Heure : 2h00
└────────────── Minute : 0
```

> ➡️ Le script s'exécutera **tous les jours à 2h00 du matin**.

Pour vérifier que la tâche est enregistrée :

```bash
sudo crontab -l
```

---

### Partie 6 — Vérification de l'exécution

J'ai vérifié que le service **cron** est actif sur le système :

```bash
systemctl status cron
```

Pour consulter les journaux d'exécution de cron :

```bash
journalctl -u cron
```

Ou dans les logs système :

```bash
cat /var/log/syslog | grep CRON
```

---

### Partie 7 — Dépannage

Lors de mes tests, voici les problèmes que j'aurais pu rencontrer et leurs solutions :

| Problème | Cause possible | Solution |
|----------|---------------|----------|
| `Permission denied` | Script non exécutable | `chmod +x` |
| `useradd` échoue | Manque de privilèges | Exécuter en tant que root / sudo |
| Archive vide | Mauvais chemin source | Vérifier le chemin dans `tar` |
| Cron ne lance pas le script | Chemins relatifs dans le script | Utiliser des **chemins absolus** partout |

---

### Partie 8 — Améliorations avancées

**a) Supprimer l'utilisateur temporaire après l'exécution :**

J'ai ajouté cette ligne à la fin du script pour nettoyer l'utilisateur créé :

```bash
sudo userdel -r employe_temp
```

**b) Ajouter une gestion d'erreurs :**

Après chaque commande critique, j'ai ajouté une vérification du code de retour `$?` :

```bash
cp -r /entreprise/data/* /entreprise/backup/

if [ $? -ne 0 ]; then
    echo "Erreur lors de la sauvegarde" >> $LOG
fi
```

> `$?` contient `0` si la commande a réussi, autre chose si elle a échoué.

---

## 📊 Diagramme avant / après exécution

### Avant exécution

```
/entreprise/
│
├── data/                     # Dossier source (fichiers à sauvegarder)
│   ├── fichier1.txt
│   └── fichier2.txt
│
├── backup/                   # Vide (ou ancien backup)
│
└── logs/
    └── log.txt               # Vide ou inexistant
```

### Après exécution

```
/entreprise/
│
├── data/                     # Dossier original (inchangé)
│   ├── fichier1.txt
│   └── fichier2.txt
│
├── backup/                   # Sauvegarde complète
│   ├── fichier1.txt          ◀── copie de data/
│   ├── fichier2.txt          ◀── copie de data/
│   └── backup_2026-02-05.tar.gz  ◀── archive compressée
│
└── logs/
    └── log.txt               # Journal complet de l'exécution
```

### Flux de données

```
data/ ──────── cp -r ──────────▶ backup/
data/ ──────── tar -czvf ───────▶ backup/backup_YYYY-MM-DD.tar.gz
script ─────── echo / >> ───────▶ logs/log.txt
système ────── useradd ──────────▶ employe_temp (dans /etc/passwd)
```

---

## 📚 Résumé des commandes

### Gestion de fichiers et dossiers

| Commande | Rôle | Exemple |
|----------|------|---------|
| `mkdir -p` | Créer un dossier et ses parents | `mkdir -p /entreprise/data` |
| `cp -r` | Copier récursivement | `cp -r source/ dest/` |
| `tar -czvf` | Créer une archive compressée | `tar -czvf backup.tar.gz dossier/` |
| `tee` | Écrire dans un fichier avec sudo | `echo test \| sudo tee fichier.txt` |

### Gestion des utilisateurs

| Commande | Rôle | Exemple |
|----------|------|---------|
| `useradd` | Créer un utilisateur | `sudo useradd employe` |
| `chpasswd` | Définir un mot de passe | `echo "user:pass" \| sudo chpasswd` |
| `userdel -r` | Supprimer utilisateur + home | `sudo userdel -r employe` |
| `id` | Vérifier l'existence d'un user | `id employe` |

### Réseau, logs, cron et permissions

| Commande | Rôle |
|----------|------|
| `ping -c 4 8.8.8.8` | Tester la connectivité réseau |
| `>> fichier` | Ajouter la sortie dans un fichier log |
| `2>&1` | Rediriger les erreurs vers le log |
| `crontab -e` | Modifier les tâches planifiées |
| `systemctl status cron` | Vérifier que cron est actif |
| `chmod +x` | Rendre un script exécutable |
| `$?` | Code retour de la dernière commande |

---

<img width="1920" height="1080" alt="Screenshot (370)" src="https://github.com/user-attachments/assets/f0aa14e5-b770-497a-a266-b60ab0bf46cc" />
<img width="1920" height="1080" alt="Screenshot (369)" src="https://github.com/user-attachments/assets/dd87899e-4b41-46af-a1ed-4e6a8d91f905" />

## 💬 Conclusion

Grâce à ce TP, j'ai appris à :

- Créer une **structure de dossiers** d'entreprise sous Linux
- Écrire un **script Bash complet** avec variables, conditions et redirections
- Sauvegarder des fichiers avec `cp` et les **archiver** avec `tar`
- Créer et gérer des **utilisateurs temporaires** en ligne de commande
- **Journaliser** toutes les opérations dans un fichier log
- **Planifier** l'exécution automatique avec `cron`
- **Diagnostiquer** les erreurs et appliquer des corrections

> ✅ *Un bon script Bash = automatisation + journalisation + gestion d'erreurs.*

---

*Ouail Gacem — 300148094*
