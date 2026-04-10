#!/bin/bash
# =====================================
# Monitoring Web - INF1102
# Auteur : 300150268
# =====================================

LOG="data/sample.log"
RAPPORT="output/rapport.txt"
DATE=$(date "+%Y-%m-%d %H:%M:%S")

SITES=(
    "https://google.com"
    "https://github.com"
    "https://collegeboreal.ca"
    "https://example.com"
    "https://httpstat.us/404"
)

echo "===== RAPPORT MONITORING =====" > $RAPPORT
echo "Date : $DATE" >> $RAPPORT
echo "" >> $RAPPORT

> $LOG

for SITE in "${SITES[@]}"; do
    START=$(date +%s%3N)
    HTTP_CODE=$(curl -o /dev/null -s -w "%{http_code}" --max-time 10 "$SITE")
    END=$(date +%s%3N)
    DURATION=$((END - START))

    if [ "$HTTP_CODE" == "200" ] || [ "$HTTP_CODE" == "301" ] || [ "$HTTP_CODE" == "302" ]; then
        STATUS="OK"
    else
        STATUS="ERREUR"
    fi

    echo "$DATE | $SITE | $HTTP_CODE | ${DURATION}ms | $STATUS" | tee -a $LOG >> $RAPPORT
done

echo "" >> $RAPPORT
echo "===== ANALYSE PYTHON =====" >> $RAPPORT
python3 scripts/analyse.py $LOG >> $RAPPORT

echo ""
echo "Rapport généré : $RAPPORT"
cat $RAPPORT