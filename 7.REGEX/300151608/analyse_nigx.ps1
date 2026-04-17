$logfile = "/var/log/nginx/access.log"
$rapport = "rapport_nginx_ps1_$(Get-Date -Format yyyy-MM-dd).txt"

# Lire le fichier log
$lines = Get-Content $logfile

# En-tête du rapport
"Rapport Nginx PowerShell - $(Get-Date)" | Out-File $rapport
"--------------------------------------" | Out-File $rapport -Append

# Total des requêtes
$total = $lines.Count
"Total des requêtes : $total" | Out-File $rapport -Append

# Extraire les codes HTTP
$codes = $lines | ForEach-Object {
    if ($_ -match '" (\d{3}) ') {
        $matches[1]
    }
}

# Nombre total d'erreurs HTTP
$errors = $codes | Where-Object { $_ -match '^[45]' }
"Total des erreurs HTTP : $($errors.Count)" | Out-File $rapport -Append

# Nombre d'erreurs 404
$notFound = $codes | Where-Object { $_ -eq "404" }
"Nombre d'erreurs 404 : $($notFound.Count)" | Out-File $rapport -Append

# Nombre d'erreurs 500
$serverError = $codes | Where-Object { $_ -eq "500" }
"Nombre d'erreurs 500 : $($serverError.Count)" | Out-File $rapport -Append

# Extraire les adresses IP
$ips = $lines | ForEach-Object {
    if ($_ -match '^(\d{1,3}(\.\d{1,3}){3})') {
        $matches[1]
    }
}

"" | Out-File $rapport -Append
"Top 5 des adresses IP :" | Out-File $rapport -Append
$ips |
    Group-Object |
    Sort-Object Count -Descending |
    Select-Object -First 5 |
    ForEach-Object {
        "$($_.Count) - $($_.Name)" | Out-File $rapport -Append
    }

# Extraire les pages demandées en GET
$pages = $lines | ForEach-Object {
    if ($_ -match '"GET ([^ ]+)') {
        $matches[1]
    }
}

"" | Out-File $rapport -Append
"Top 5 des pages visitées :" | Out-File $rapport -Append
$pages |
    Group-Object |
    Sort-Object Count -Descending |
    Select-Object -First 5 |
    ForEach-Object {
        "$($_.Count) - $($_.Name)" | Out-File $rapport -Append
    }

Write-Host "Rapport généré avec succès : $rapport"
