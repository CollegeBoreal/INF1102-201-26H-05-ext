#!/bin/bash
LOG="/tmp/entreprise/logs/log.txt"
DATE=$(date)
echo "===================================" >> $LOG
echo "Début exécution : $DATE" >> $LOG
echo "Test réseau..." >> $LOG
ping -c 4 8.8.8.8 >> $LOG 2>&1
echo "Sauvegarde en cours..." >> $LOG
cp -r /tmp/entreprise/data/* /tmp/entreprise/backup/ >> $LOG 2>&1
tar -czvf /tmp/entreprise/backup/backup_$(date +%F).tar.gz /tmp/entreprise/data >> $LOG 2>&1
echo "Fin exécution : $(date)" >> $LOG
echo "===================================" >> $LOG
