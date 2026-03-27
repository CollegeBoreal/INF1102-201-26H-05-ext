#!/bin/bash
LOG_FILE="/var/log/nginx/access.log"
OUTPUT_FILE="/home/aymen/nginx_ips.txt"

awk '{print $1}' $LOG_FILE | sort | uniq > $OUTPUT_FILE
echo "Script exécuté le $(date)" >> ~/nginx_ips.log
