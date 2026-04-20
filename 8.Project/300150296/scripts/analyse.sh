#!/bin/bash

echo "=== Analyse de logs - 300150296 ==="

LOG_FILE="../data/sample.log"
OUTPUT_FILE="../output/rapport.txt"

echo "Génération du rapport..." > $OUTPUT_FILE
echo "Date: $(date)" >> $OUTPUT_FILE
echo "-----------------------------------" >> $OUTPUT_FILE

# Appel Python
python3 scripts/analyse.py $LOG_FILE >> $OUTPUT_FILE

echo "✅ Rapport généré: $OUTPUT_FILE"