# 🖥️ TP – Script Batch de Gestion Système sous Linux

> **Cours : Programmation des Systèmes**  
> **Objectif :** Automatiser des tâches d'administration système via un script Bash

---

## 📋 Table des matières

1. [Environnement requis](#environnement-requis)
2. [Partie 1 – Préparation de l'environnement](#partie-1--préparation-de-lenvironnement)
3. [Partie 2 – Création du script Batch](#partie-2--création-du-script-batch)
4. [Partie 3 – Rendre le script exécutable](#partie-3--rendre-le-script-exécutable)
5. [Partie 4 – Test manuel](#partie-4--test-manuel)
6. [Partie 5 – Planification avec Cron](#partie-5--planification-avec-cron)
7. [Partie 6 – Vérification de l'exécution](#partie-6--vérification-de-lexécution)
8. [Partie 7 – Dépannage](#partie-7--dépannage)
9. [Partie 8 – Amélioration avancée](#partie-8--amélioration-avancée)
10. [Résultat attendu](#résultat-attendu)

---

## 🖥️ Environnement requis

- Distribution Linux (ex: Ubuntu Server)
- Accès `sudo`
- Terminal
- Service `cron` actif

---

## 🔹 Partie 1 – Préparation de l'environnement

Création de la structure de dossiers nécessaire :

```bash
sudo mkdir -p /entreprise/data
sudo mkdir -p /entreprise/backup
sudo mkdir -p /entreprise/logs
```

Création des fichiers de test :

```bash
echo "Fichier 1" | sudo tee /entreprise/data/fichier1.txt
echo "Fichier 2" | sudo tee /entreprise/data/fichier2.txt
```

### 📸 Capture – Préparation de l'environnement

![Préparation de l'environnement](images/PARTIE%201%20preparation%20de%20l'environnement.png)

---

## 🔹 Partie 2 – Création du script Batch

Créer le fichier script :

```bash
sudo nano /entreprise/script_gestion.sh
```

### 📄 Code complet du script

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

---

## 🔹 Partie 3 – Rendre le script exécutable

```bash
sudo chmod +x /entreprise/script_gestion.sh
```

### 📸 Capture – Rendre le script exécutable

![Rendre le script exécutable](images/Partue%203%20Rendre%20executable.png)

---

## 🔹 Partie 4 – Test manuel

Exécuter le script :

```bash
sudo /entreprise/script_gestion.sh
```

Vérifications après exécution :

```bash
# Fichiers copiés dans /entreprise/backup
ls /entreprise/backup

# Utilisateur créé
cat /etc/passwd | grep employe_temp

# Fichier log
cat /entreprise/logs/log.txt
```

### 📸 Capture – Test manuel

![Test manuel](images/partie%204%20Test%20Manuel.png)

### 📸 Capture – Test manuel (suite)

![Test manuel suite](images/PARTIE%204%20TEST%20MANUEL%20V2%20SUITE%20.png)

---

## 🔹 Partie 5 – Planification avec Cron

Éditer la crontab :

```bash
sudo crontab -e
```

Ajouter la ligne suivante :

```
0 2 * * * /entreprise/script_gestion.sh
```

> ➡️ Le script s'exécutera automatiquement **tous les jours à 2h00**

### 📸 Capture – Planification avec Cron

![Planification Cron](images/partie%205%20planification%20avec%20cron%20.png)

---

## 🔹 Partie 6 – Vérification de l'exécution

Vérifier que le service cron fonctionne :

```bash
systemctl status cron
```

### 📸 Capture – Vérification que Cron fonctionne

![Vérification Cron](images/P6%201-VERIFICATION%20CRON%20FOCNTIONNE%20.png)

Consulter les journaux système :

```bash
journalctl -u cron
# ou
cat /var/log/syslog | grep CRON
```

### 📸 Capture – Consultation des journaux

![Consultation des journaux](images/P6%202-consultation%20des%20journaux.png)

---

## 🔹 Partie 7 – Dépannage

| Problème | Cause possible | Solution |
|---|---|---|
| `Permission denied` | Script non exécutable | `chmod +x` |
| `useradd` échoue | Pas de `sudo` | Exécuter en root |
| Archive vide | Mauvais chemin | Vérifier la source |
| Cron ne lance pas | Mauvais `PATH` | Utiliser des chemins absolus |

### Erreur 1 – Retrait de la permission d'exécution (simulation)

```bash
sudo chmod -x /entreprise/script_gestion.sh
```

#### 📸 Capture – Retrait de la permission d'exécution

![Retrait permission exécution](images/P7%201-Retrait%20de%20la%20permission%20d'execution%20.png)

#### 📸 Capture – Erreur simulée

![Erreur simulée](images/P7%201%201%20ERREUR%20SIMULEE%20.png)

#### 📸 Capture – Correction de l'erreur (remise de chmod +x)

![Correction erreur](images/P7%201%201%201%20CORRECTION%20DE%20L'ERREUR.png)

---

### Erreur 2 – Création utilisateur sans `sudo`

#### 📸 Capture – Erreur useradd sans sudo

![Erreur useradd sans sudo](images/P7%202%20ERREUR%20CREATION%20USER%20SANS%20SUDO.png)

#### 📸 Capture – Correction : ajout de sudo pour useradd

![Correction sudo useradd](images/p7%202%20correction%20erreur%20ajout%20sudo%20pour%20useradd%20.png)

---

## 🔹 Partie 8 – Amélioration (niveau avancé)

### Suppression automatique de l'utilisateur temporaire

Ajouter à la fin du script :

```bash
sudo userdel -r employe_temp
```

### Gestion d'erreur

```bash
if [ $? -ne 0 ]; then
   echo "Erreur lors de la sauvegarde" >> $LOG
fi
```

### 📸 Capture – Amélioration : suppression automatique de l'utilisateur

![Amélioration suppression utilisateur](images/P8%20Amelioration%20code%20supprimer%20user%20apres%20sauvegarde.png)

---

## ✅ Résultat attendu

### Structure avant/après exécution

**Avant exécution :**

```
/entreprise/
├── data/
│   ├── fichier1.txt
│   └── fichier2.csv
├── backup/          ← vide ou ancien contenu
└── logs/
    └── log.txt
```

**Après exécution :**

```
/entreprise/
├── data/            ← inchangé
│   ├── fichier1.txt
│   └── fichier2.csv
├── backup/
│   ├── fichier1.txt                      ← copie de data/
│   ├── fichier2.csv                      ← copie de data/
│   └── backup_2026-03-21.tar.gz          ← archive compressée
└── logs/
    └── log.txt      ← journal complet de l'exécution
```

### Flux de données

```
data/  ────copie────▶  backup/
data/  ────archive──▶  backup/backup_YYYY-MM-DD.tar.gz
script ────────────▶  logs/log.txt
```

### À la fin de ce TP, l'étudiant est capable de :

- ✔️ Écrire un script Bash structuré
- ✔️ Automatiser une tâche système
- ✔️ Planifier son exécution avec `cron`
- ✔️ Lire les journaux système
- ✔️ Diagnostiquer et corriger des erreurs

---

*TP réalisé dans le cadre du cours de Programmation des Systèmes*
