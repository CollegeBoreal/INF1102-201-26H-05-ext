##JUSTIN 300151403
## 🎯 Objectif

Programmer un script Batch sous **Linux** permettant de :

1. Sauvegarder un dossier d’entreprise
2. Créer un utilisateur temporaire
3. Tester la connectivité réseau
4. Générer un fichier journal (log)
5. Planifier l’exécution automatique avec **cron**
6. Vérifier l’exécution et diagnostiquer les erreurs

---

# 🖥 Environnement requis

* Distribution Linux (ex: Ubuntu Server)
* Accès sudo
* Terminal
* Service cron actif

---

# 🔹 PARTIE 1 – Préparation de l’environnement

Créer la structure suivante :

```bash
mkdir -p entreprise/data
mkdir -p entreprise/backup
mkdir -p entreprise/logs
```

Créer des fichiers test :

```bash
echo "Fichier 1" | sudo tee entreprise/data/fichier1.txt
echo "Fichier 2" | sudo tee entreprise/data/fichier2.txt
```

---

# 🔹 PARTIE 2 – Création du script Batch

Créer le fichier :

```bash
nano entreprise/script_gestion.sh
```

---

## 📄 CODE COMPLET À INTÉGRER

```bash
#!/bin/bash

LOG="~/entreprise/logs/log.txt"
DATE=$(date)

echo "===================================" >> $LOG
echo "Début exécution : $DATE" >> $LOG

# 1. Vérification réseau
echo "Test réseau..." >> $LOG
ping -c 4 8.8.8.8 >> $LOG 2>&1

# 2. Sauvegarde des fichiers
echo "Sauvegarde en cours..." >> $LOG
cp -r ~/entreprise/data/* ~/entreprise/backup/ >> $LOG 2>&1

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
tar -czvf ~/entreprise/backup/backup_$(date +%F).tar.gz ~/entreprise/data >> $LOG 2>&1

echo "Fin exécution : $(date)" >> $LOG
echo "===================================" >> $LOG
```

---

# 🔹 PARTIE 3 – Rendre exécutable

```bash
chmod +x ~/entreprise/script_gestion.sh
```

---

# 🔹 PARTIE 4 – Test manuel

Exécuter :

```bash
~/entreprise/script_gestion.sh
```

Vérifier :

* Les fichiers copiés dans `~/entreprise/backup`
* L’archive `.tar.gz`
* L’utilisateur créé :

```bash
cat /etc/passwd | grep employe_temp
```

* Le fichier log :

```bash
cat ~/entreprise/logs/log.txt
```

---

# 🔹 PARTIE 5 – Planification avec Cron

Éditer la crontab :

```bash
crontab -e
```

Ajouter :

```
0 2 * * * ${HOME}/entreprise/script_gestion.sh
```

➡ Exécution tous les jours à 2h00

---

# 🔹 PARTIE 6 – Vérification de l’exécution

Vérifier que cron fonctionne :

```bash
systemctl status cron
```

Consulter les journaux :

```bash
journalctl -u cron
```

ou

```bash
cat /var/log/syslog | grep CRON
```

---

# 🔹 PARTIE 7 – Dépannage

| Problème          | Cause possible        | Solution                 |
| ----------------- | --------------------- | ------------------------ |
| Permission denied | Script non exécutable | chmod +x                 |
| Useradd échoue    | Pas sudo              | Exécuter en root         |
| Archive vide      | Mauvais chemin        | Vérifier source          |
| Cron ne lance pas | Mauvais PATH          | Utiliser chemins absolus |

---

# 🔹 PARTIE 8 – Amélioration (niveau avancé)

## Supprimer l’utilisateur après sauvegarde

Ajouter à la fin :

```bash
sudo userdel -r employe_temp
```

---

## Ajouter gestion d’erreur

Exemple :

```bash
if [ $? -ne 0 ]; then
   echo "Erreur lors de la sauvegarde" >> $LOG
fi
```

---
