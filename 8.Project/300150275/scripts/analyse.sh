#!/bin/bash

# ============================================
# Projet 5 : Monitoring de sites web
# Auteur : Tarik Tidjet - 300150275
# Date : $(date +%Y-%m-%d)
# ============================================

SITES=("https://www.google.com" "https://www.github.com" "https://www.wikipedia.org" "https://www.youtube.com" "https://www.amazon.com")
OUTPUT="$(dirname "$0")/../output/rapport.txt"
LOG="$(dirname "$0")/../data/sample.log"

mkdir -p "$(dirname "$OUTPUT")"
mkdir -p "$(dirname "$LOG")"

echo "📊 Rapport Monitoring - $(date)" > "$OUTPUT"
echo "===========================================" >> "$OUTPUT"

for site in "${SITES[@]}"; do
    START=$(date +%s%3N)
    HTTP_CODE=$(curl -o /dev/null -s -w "%{http_code}" --max-time 10 "$site")
    END=$(date +%s%3N)
    RESPONSE_TIME=$((END - START))

    if [ "$HTTP_CODE" -eq 200 ]; then
        STATUS="✅ EN LIGNE"
    else
        STATUS="❌ HORS LIGNE"
    fi

    echo "$site | $HTTP_CODE | ${RESPONSE_TIME}ms | $STATUS" | tee -a "$OUTPUT" "$LOG"
done

echo "" >> "$OUTPUT"
echo "===========================================" >> "$OUTPUT"
echo "✅ Rapport généré : $OUTPUT"

# Appel Python pour analyse
python3 "$(dirname "$0")/analyse.py" "$LOG"
