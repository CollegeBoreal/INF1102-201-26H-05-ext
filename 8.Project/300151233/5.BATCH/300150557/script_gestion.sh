#!/bin/bash

mkdir -p /entreprise/data
mkdir -p /entreprise/backup
mkdir -p /entreprise/logs

LOG="/entreprise/logs/log.txt"
USER_TEMP="employe_temp"
DATE=$(date '+%Y-%m-%d %H:%M:%S')

echo "===================================" >> "$LOG"
echo "Début exécution : $DATE" >> "$LOG"

echo "Test réseau..." >> "$LOG"
ping -c 4 8.8.8.8 >> "$LOG" 2>&1

echo "Sauvegarde en cours..." >> "$LOG"
cp -r /entreprise/data/* /entreprise/backup/ >> "$LOG" 2>&1

if id "$USER_TEMP" >/dev/null 2>&1; then
    echo "Utilisateur $USER_TEMP existe déjà." >> "$LOG"
else
    sudo useradd "$USER_TEMP"
    echo "$USER_TEMP:Temp1234" | sudo chpasswd
    echo "Utilisateur $USER_TEMP créé." >> "$LOG"
fi

tar -czf /entreprise/backup/backup_$(date +%F).tar.gz /entreprise/data >> "$LOG" 2>&1

if id "$USER_TEMP" >/dev/null 2>&1; then
    sudo userdel "$USER_TEMP" >> "$LOG" 2>&1
    echo "Utilisateur $USER_TEMP supprimé." >> "$LOG"
fi

echo "Fin exécution : $(date)" >> "$LOG"
echo "===================================" >> "$LOG"