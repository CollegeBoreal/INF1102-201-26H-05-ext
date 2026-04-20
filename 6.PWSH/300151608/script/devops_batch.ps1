#!/usr/bin/env pwsh

# =========================
# DevOps Batch Script
# =========================

$rapportTxt = "./rapport.txt"
$rapportJson = "./rapport.json"
$date = Get-Date
$user = whoami
$hostname = hostname

"===== RAPPORT DEVOPS =====" | Tee-Object $rapportTxt
"Date : $date" | Tee-Object -Append $rapportTxt
"Utilisateur : $user" | Tee-Object -Append $rapportTxt
"Machine : $hostname" | Tee-Object -Append $rapportTxt
"" | Tee-Object -Append $rapportTxt

# CPU
"Top CPU :" | Tee-Object -Append $rapportTxt
$cpu = Get-Process | Sort-Object CPU -Descending | Select -First 5
$cpu | ForEach-Object {
    "$($_.ProcessName) CPU: $($_.CPU)" | Tee-Object -Append $rapportTxt
}

# Mémoire
"" | Tee-Object -Append $rapportTxt
"Top Mémoire :" | Tee-Object -Append $rapportTxt
$mem = Get-Process | Sort-Object WS -Descending | Select -First 5
$mem | ForEach-Object {
    "$($_.ProcessName) MEM: $($_.WS)" | Tee-Object -Append $rapportTxt
}

# Disque
"" | Tee-Object -Append $rapportTxt
"Disque :" | Tee-Object -Append $rapportTxt
df -h | Tee-Object -Append $rapportTxt

# SSH test
"" | Tee-Object -Append $rapportTxt
"Test SSH :" | Tee-Object -Append $rapportTxt
ssh -o ConnectTimeout=3 localhost "echo OK" 2>&1 | Tee-Object -Append $rapportTxt

# JSON
$obj = [PSCustomObject]@{
    Date = $date
    User = $user
    Machine = $hostname
}

$obj | ConvertTo-Json | Set-Content $rapportJson

"Rapports générés : $rapportTxt et $rapportJson"
