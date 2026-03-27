#!/bin/bash

# =====================================
# Monitoring site web - INF1102
# Auteur : ISMAIL TRACHE
# Boreal ID : 300150395
# =====================================

SITES=("https://google.com" "https://github.com" "https://collegeboreal.ca" "https://example.com" "https://httpstat.us/404")
OUTPUT="$(dirname "$0")/../output/rapport.txt"
DATA="$(dirname "$0")/../data/sample.log"
DATE=$(date '+%Y-%m-%d %H:%M:%S')

echo "===== RAPPORT MONITORING =====" > "$OUTPUT"
echo "Date : $DATE" >> "$OUTPUT"
echo "" >> "$OUTPUT"

# Vider le log précédent
> "$DATA"

for SITE in "${SITES[@]}"; do
    START=$(date +%s%N)
    HTTP_CODE=$(curl -o /dev/null -s -w "%{http_code}" --max-time 10 "$SITE")
    END=$(date +%s%N)
    ELAPSED=$(( (END - START) / 1000000 ))

if [ "$HTTP_CODE" -eq 200 ] || [ "$HTTP_CODE" -eq 301 ] || [ "$HTTP_CODE" -eq 302 ]; then
        STATUS="✅ OK"
    else
        STATUS="❌ ERREUR"
    fi

    echo "$DATE | $SITE | $HTTP_CODE | ${ELAPSED}ms | $STATUS" | tee -a "$DATA"
    echo "$DATE | $SITE | $HTTP_CODE | ${ELAPSED}ms | $STATUS" >> "$OUTPUT"
done

echo "" >> "$OUTPUT"
echo "Analyse Python en cours..." >> "$OUTPUT"

# Appel Python pour analyse
python3 "$(dirname "$0")/analyse.py" "$DATA" "$OUTPUT"

echo ""
echo "✅ Rapport généré : $OUTPUT"
