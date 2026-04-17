#!/bin/bash

# Log file
LOG_FILE="/var/log/nginx/access.log"

# Output file
OUTPUT_FILE="/home/ubuntu/nginx_ips.txt"

# Extract unique IP addresses
awk '{print $1}' $LOG_FILE | sort | uniq > $OUTPUT_FILE

# Log execution time
echo "Script executed on $(date)" >> /home/ubuntu/nginx_ips.log
