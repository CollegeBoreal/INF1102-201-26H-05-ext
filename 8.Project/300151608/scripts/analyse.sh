#!/bin/bash

# =====================================
# Projet Bash + Python - INF1102
# Auteur : Mohammed Aiche
# Boreal ID : 300151608
# =====================================

INPUT_FILE="$(dirname "$0")/../data/sample.log"
OUTPUT_FILE="$(dirname "$0")/../output/rapport.txt"
PYTHON_SCRIPT="$(dirname "$0")/analyse.py"

# Vérifier si le fichier existe
if [ ! -f "$INPUT_FILE" ]; then
    echo "Erreur : fichier introuvable : $INPUT_FILE"
    exit 1
fi

# Vider l'ancien rapport
> "$OUTPUT_FILE"

echo "===== RAPPORT MONITORING =====" >> "$OUTPUT_FILE"
echo "Date : $(date '+%Y-%m-%d %H:%M:%S')" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

# Afficher le contenu du log
cat "$INPUT_FILE" >> "$OUTPUT_FILE"

echo "" >> "$OUTPUT_FILE"
echo "Analyse Python en cours..." >> "$OUTPUT_FILE"

# Appel Python
python3 "$PYTHON_SCRIPT" "$INPUT_FILE" "$OUTPUT_FILE"

echo ""
echo "✅ Rapport généré : $OUTPUT_FILE"
