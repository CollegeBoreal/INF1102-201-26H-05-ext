#!/usr/bin/env bash
set -euo pipefail

BASE_NET="10.7.237"
START=224
END=245

GOBUSTER="$HOME/go/bin/gobuster"
WORDLIST="/snap/seclists/current/Discovery/Web-Content/raft-medium-directories.txt"

OUTDIR="$HOME/logs/gobuster"
mkdir -p "$OUTDIR"

ts="$(date +%F_%H%M%S)"
RUNLOG="${OUTDIR}/run_${ts}.log"
SKIPLOG="${OUTDIR}/skipped_${ts}.log"

echo "$(date '+%F %T') START scan ${BASE_NET}.${START}-${END}" >> "$RUNLOG"

for i in $(seq "$START" "$END"); do
  ip="${BASE_NET}.${i}"
  url="http://${ip}"
  outfile="${OUTDIR}/dir_${ip}_${ts}.txt"

if curl -sS --max-time 2 -I "$url" >/dev/null 2>&1; then
  echo "=== SCAN $url ==="
  echo "$(date '+%F %T') SCAN $url -> $outfile" >> "$RUNLOG"

  "$GOBUSTER" dir -u "$url" -w "$WORDLIST" -x html,php,txt -t 5 --timeout 3s -q -o "$outfile" || true
else
  echo "=== SKIP $url (no HTTP response) ==="
  echo "$(date '+%F %T') SKIP $url (no HTTP response)" >> "$SKIPLOG"
fi

done

echo "$(date '+%F %T') END" >> "$RUNLOG"
