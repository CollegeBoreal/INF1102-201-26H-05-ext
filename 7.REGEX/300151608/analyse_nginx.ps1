$logfile = "data/sample.log"
$rapport = "output/rapport_ps1.txt"

$lines = Get-Content $logfile

"Rapport Nginx" | Out-File $rapport
"----------------" | Out-File $rapport -Append

# Total
$total = $lines.Count
"Total requêtes : $total" | Out-File $rapport -Append

# Codes HTTP
$codes = $lines | ForEach-Object {
    if ($_ -match '" (\d{3}) ') { $matches[1] }
}

# Erreurs
$errors = $codes | Where-Object { $_ -match '^[45]' }
"Erreurs HTTP : $($errors.Count)" | Out-File $rapport -Append

# IP
$ips = $lines | ForEach-Object {
    if ($_ -match '^(\d{1,3}(\.\d{1,3}){3})') { $matches[1] }
}

"`nTop 3 IP :" | Out-File $rapport -Append
$ips | Group-Object | Sort-Object Count -Descending | Select-Object -First 3 |
ForEach-Object {
    "$($_.Count) - $($_.Name)" | Out-File $rapport -Append
}

Write-Host "OK"
