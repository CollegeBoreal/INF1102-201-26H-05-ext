#!/bin/bash

# ============================================
# Projet 5 : Monitoring de sites web
# Auteur : Tarik Tidjet - 300150275
# ============================================

SCRIPT_DIR="$(dirname "$0")"
PYTHON_SCRIPT="$SCRIPT_DIR/analyse.py"
LOG="$SCRIPT_DIR/../output/rapport.txt"

echo "🚀 Démarrage du monitoring - $(date)" | tee -a "$LOG"
python3 "$PYTHON_SCRIPT"
echo "✅ Collecte terminée - $(date)" | tee -a "$LOG"
