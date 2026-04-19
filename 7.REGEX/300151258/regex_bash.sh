#!/bin/bash

echo "=== Emails ==="
grep -Eo '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' notes.txt

echo
echo "=== Téléphones ==="
grep -Eo '[0-9]{3}-[0-9]{3}-[0-9]{4}' notes.txt

echo
echo "=== Dates YYYY-MM-DD ==="
grep -Eo '[0-9]{4}-[0-9]{2}-[0-9]{2}' notes.txt

echo
echo "=== Adresses IP ==="
grep -Eo '([0-9]{1,3}\.){3}[0-9]{1,3}' notes.txt

echo
echo "=== Codes d'erreur HTTP ==="
grep -Eo 'Erreur [0-9]{3}' notes.txt
