#!/bin/bash

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SCRIPTS_DIR="$PROJECT_DIR/scripts"
OUTPUT_DIR="$PROJECT_DIR/output"
DATA_DIR="$PROJECT_DIR/data"

mkdir -p "$OUTPUT_DIR" "$DATA_DIR"

API_KEY="67f475e5835cd25c4201b6f01d354c66"
CITY="Toronto,CA"

echo "===== PIPELINE METEO ====="

echo "[1] Récupération météo..."

curl -s "http://api.openweathermap.org/data/2.5/weather?q=$CITY&appid=$API_KEY&units=metric" > "$DATA_DIR/meteo.json"

if [ ! -s "$DATA_DIR/meteo.json" ]; then
    echo "❌ Erreur API"
    exit 1
fi

echo "✅ Données récupérées"

echo "[2] Lancement analyse Python..."
python3 "$SCRIPTS_DIR/analyse.py"

if [ $? -ne 0 ]; then
    echo "❌ Erreur Python"
    exit 1
fi

echo "✅ Pipeline terminé"
