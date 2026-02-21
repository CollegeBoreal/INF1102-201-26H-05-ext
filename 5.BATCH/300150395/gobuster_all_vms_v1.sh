cat > ~/scripts/gobuster_all_vms.sh <<'EOF'
#!/usr/bin/env bash
set -euo pipefail

BASE_NET="10.7.237"
START=224
END=245

GOBUSTER="${GOBUSTER:-$HOME/go/bin/gobuster}"
WORDLIST="${WORDLIST:-/snap/seclists/current/Discovery/Web-Content/raft-medium-directories.txt}"
EXTENSIONS="html,php,txt,js,json,xml,bak,old"
THREADS=20
TIMEOUT="5s"

OUTDIR="$HOME/logs/gobuster"
mkdir -p "$OUTDIR"

ts="$(date +%F_%H%M%S)"
RUNLOG="${OUTDIR}/run_${ts}.log"
SKIPLOG="${OUTDIR}/skipped_${ts}.log"

echo "$(date '+%F %T') START scan ${BASE_NET}.${START}-${END}" | tee -a "$RUNLOG"

for i in $(seq "$START" "$END"); do
  ip="${BASE_NET}.${i}"
  url="http://${ip}"
  outfile="${OUTDIR}/dir_${ip}_${ts}.txt"

  if curl -sS --max-time 3 -I "$url" >/dev/null 2>&1; then
    echo "=== SCAN $url ===" | tee -a "$RUNLOG"
    "$GOBUSTER" dir \
      -u "$url" \
      -w "$WORDLIST" \
      -x "$EXTENSIONS" \
      -t "$THREADS" \
      --timeout "$TIMEOUT" \
      --no-error \
      -o "$outfile" || true
    echo "--- Résultats $ip ---"
    grep "Status:" "$outfile" 2>/dev/null | head -20 || echo "(aucun résultat)"
  else
    echo "=== SKIP $url (no HTTP response) ===" | tee -a "$SKIPLOG"
  fi
done

echo "$(date '+%F %T') END" | tee -a "$RUNLOG"
EOF

chmod +x ~/scripts/gobuster_all_vms.sh
./gobuster_all_vms.sh

