#!/bin/bash

LOG_FILE="./access.log"
OUTPUT_FILE="./nginx_ips.txt"

awk '{print $1}' "$LOG_FILE" | sort | uniq > "$OUTPUT_FILE"
awk '{print $1}' "$LOG_FILE" | sort | uniq -c | sort -nr > ./nginx_ips_freq.txt

echo "Script exécuté le $(date)" >> ./scruter_nginx.log
