#!/usr/bin/env pwsh
$logfile = "/var/log/nginx/access.log"
$rapportDir = "$HOME/INF1102-201-26H-05/7.REGEX/300152260"
$rapport = "$rapportDir/rapport_nginx_ps1_$(Get-Date -Format yyyy-MM-dd).txt"

if (-not (Test-Path $logfile)) {
    Write-Host "Fichier log introuvable : $logfile"
    exit 1
}

$lines = Get-Content $logfile
"Rapport Nginx PowerShell - $(Get-Date)" | Out-File $rapport
"----------------------------------" | Out-File $rapport -Append
"Total requetes : $($lines.Count)" | Out-File $rapport -Append

$codes = $lines | ForEach-Object { if ($_ -match '" (\d{3}) ') { $matches[1] } }
$errors = $codes | Where-Object { $_ -match '^[45]' }
$notfound = $codes | Where-Object { $_ -eq "404" }
$servererr = $codes | Where-Object { $_ -eq "500" }

"Erreurs HTTP : $($errors.Count)" | Out-File $rapport -Append
"Erreurs 404 : $($notfound.Count)" | Out-File $rapport -Append
"Erreurs 500 : $($servererr.Count)" | Out-File $rapport -Append

$ips = $lines | ForEach-Object { if ($_ -match '^(\d{1,3}(\.\d{1,3}){3})') { $matches[1] } }
"`nTop 5 IP :" | Out-File $rapport -Append
$ips | Group-Object | Sort-Object Count -Descending | Select-Object -First 5 |
    ForEach-Object { "$($_.Count) $($_.Name)" | Out-File $rapport -Append }

$pages = $lines | ForEach-Object { if ($_ -match '"GET ([^ ]+)') { $matches[1] } }
"`nTop 5 pages :" | Out-File $rapport -Append
$pages | Group-Object | Sort-Object Count -Descending | Select-Object -First 5 |
    ForEach-Object { "$($_.Count) $($_.Name)" | Out-File $rapport -Append }

Write-Host "Rapport genere : $rapport"