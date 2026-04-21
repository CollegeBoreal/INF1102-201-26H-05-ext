#!/bin/bash
# ============================================
# analyse.sh — Suivi météo quotidienne
# Étudiant : Hani Damouche (300150557)
# Cours : INF1102 — Programmation système
# ============================================

CITY="Toronto,CA"
API_KEY="4724a9add622fc59143cd5a5e66d5aae"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
OUTPUT_DIR="$SCRIPT_DIR/../output"
DATA_DIR="$SCRIPT_DIR/../data"

echo "=== Récupération météo pour $CITY ==="

# Récupérer les données JSON de l'API
curl -s "http://api.openweathermap.org/data/2.5/weather?q=$CITY&appid=$API_KEY&units=metric&lang=fr" \
    -o "$DATA_DIR/sample.log"

# Vérifier que le fichier a été créé
if [ -s "$DATA_DIR/sample.log" ]; then
    echo "✅ Données récupérées avec succès"
    echo "📂 Fichier sauvegardé : $DATA_DIR/sample.log"
else
    echo "❌ Erreur lors de la récupération"
    exit 1
fi

# Lancer l'analyse Python
echo "=== Lancement de l'analyse Python ==="
python3 "$SCRIPT_DIR/analyse.py" "$DATA_DIR/sample.log"

echo "=== Terminé ==="