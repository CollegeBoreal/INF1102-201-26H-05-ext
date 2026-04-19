#!/bin/bash

LOG="/var/log/nginx/access.log"
OUT="$HOME/nginx_ips.txt"

echo "Extraction des IPs..."

awk '{print $1}' $LOG | sort | uniq > $OUT

echo "Résultat sauvegardé dans $OUT"