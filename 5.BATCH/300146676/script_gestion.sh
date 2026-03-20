#!/bin/bash

LOG="$HOME/entreprise/logs/log.txt"
DATE=$(date)

echo "===================================" >> $LOG
echo "Début exécution : $DATE" >> $LOG

# 1. Vérification réseau
echo "Test réseau..." >> $LOG
ping -c 4 8.8.8.8 >> $LOG 2>&1
if [ $? -ne 0 ]; then
    echo "Erreur : réseau inaccessible" >> $LOG
fi

# 2. Sauvegarde des fichiers
echo "Sauvegarde en cours..." >> $LOG
cp -r $HOME/entreprise/data/* $HOME/entreprise/backup/ >> $LOG 2>&1
if [ $? -ne 0 ]; then
    echo "Erreur lors de la sauvegarde" >> $LOG
fi

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
tar -czvf $HOME/entreprise/backup/backup_$(date +%F).tar.gz $HOME/entreprise/data >> $LOG 2>&1
if [ $? -ne 0 ]; then
    echo "Erreur lors de la compression" >> $LOG
fi

# 5. Suppression utilisateur temporaire
sudo userdel -r $USER_TEMP >> $LOG 2>&1
if [ $? -ne 0 ]; then
    echo "Erreur lors de la suppression de l'utilisateur" >> $LOG
else
    echo "Utilisateur $USER_TEMP supprimé." >> $LOG
fi

echo "Fin exécution : $(date)" >> $LOG
echo "===================================" >> $LOG
