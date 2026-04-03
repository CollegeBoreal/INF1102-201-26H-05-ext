#!/bin/bash

URL="https://syphax.com"
OUTPUT="../output/rapport.txt"

python3 analyse.py "$URL" > "$OUTPUT"
