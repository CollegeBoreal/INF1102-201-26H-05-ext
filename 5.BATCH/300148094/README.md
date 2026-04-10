
##ouail gacem 300148094

🎯 Objectif
Programmer un script Batch sous Linux permettant de :

Sauvegarder un dossier d’entreprise
Créer un utilisateur temporaire
Tester la connectivité réseau
Générer un fichier journal (log)
Planifier l’exécution automatique avec cron
Vérifier l’exécution et diagnostiquer les erreurs
🖥 Environnement requis
Distribution Linux (ex: Ubuntu Server)
Accès sudo
Terminal
Service cron actif
🔹 PARTIE 1 – Préparation de l’environnement
Créer la structure suivante :

mkdir -p entreprise/data
mkdir -p entreprise/backup
mkdir -p entreprise/logs
Créer des fichiers test :

echo "Fichier 1" | sudo tee entreprise/data/fichier1.txt
echo "Fichier 2" | sudo tee entreprise/data/fichier2.txt
🔹 PARTIE 2 – Création du script Batch
Créer le fichier :

nano entreprise/script_gestion.sh
📄 CODE COMPLET À INTÉGRER
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
🔹 PARTIE 3 – Rendre exécutable
chmod +x ~/entreprise/script_gestion.sh
🔹 PARTIE 4 – Test manuel
Exécuter :

~/entreprise/script_gestion.sh
Vérifier :

Les fichiers copiés dans ~/entreprise/backup
L’archive .tar.gz
L’utilisateur créé :
cat /etc/passwd | grep employe_temp
Le fichier log :
cat ~/entreprise/logs/log.txt
🔹 PARTIE 5 – Planification avec Cron
Éditer la crontab :

crontab -e
Ajouter :

0 2 * * * ${HOME}/entreprise/script_gestion.sh
➡ Exécution tous les jours à 2h00

🔹 PARTIE 6 – Vérification de l’exécution
Vérifier que cron fonctionne :

systemctl status cron
Consulter les journaux :

journalctl -u cron
ou

cat /var/log/syslog | grep CRON
