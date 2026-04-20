$logfile = "/var/log/nginx/access.log"
$rapport = "rapport_nginx_ps1.txt"

$lines = Get-Content $logfile

"Rapport Nginx" | Out-File $rapport

$total = $lines.Count
"Total : $total" | Out-File $rapport -Append

$codes = $lines | ForEach-Object {
    if ($_ -match '" (\d{3}) ') { $matches[1] }
}

$errors = $codes | Where-Object { $_ -match '^[45]' }
"Erreurs : $($errors.Count)" | Out-File $rapport -Append

Write-Host "Rapport généré"
