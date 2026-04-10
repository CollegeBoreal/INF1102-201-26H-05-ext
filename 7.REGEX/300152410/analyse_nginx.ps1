# =====================================
# Analyse logs Nginx avec Regex
# Auteur : Imad Boudeuf
# Boreal ID : 300152410
# =====================================

$logfile = "C:\tools\nginx-1.29.8\logs\access.log"
$rapport = "C:\Users\Hocine\INF1102-201-26H-05\7.REGEX\300152410\rapport_nginx_ps1_$(Get-Date -Format yyyy-MM-dd).txt"

$lines = Get-Content $logfile

"Rapport Nginx - $(Get-Date)" | Out-File $rapport
"----------------------------------" | Out-File $rapport -Append

# Total requetes
$total = $lines.Count
"Total requetes : $total" | Out-File $rapport -Append

# Codes HTTP
$codes = $lines | ForEach-Object {
    if ($_ -match '" (\d{3}) ') { $matches[1] }
}

# Erreurs 4xx et 5xx
$errors = $codes | Where-Object { $_ -match '^[45]' }
"Erreurs HTTP : $($errors.Count)" | Out-File $rapport -Append

# 404
$notfound = $codes | Where-Object { $_ -eq "404" }
"Erreurs 404 : $($notfound.Count)" | Out-File $rapport -Append

# 500
$servererr = $codes | Where-Object { $_ -eq "500" }
"Erreurs 500 : $($servererr.Count)" | Out-File $rapport -Append

# IPs
$ips = $lines | ForEach-Object {
    if ($_ -match '^(\d{1,3}(\.\d{1,3}){3})') { $matches[1] }
}

"`nTop 5 IP :" | Out-File $rapport -Append
$ips | Group-Object | Sort-Object Count -Descending | Select-Object -First 5 |
ForEach-Object {
    "$($_.Count) $($_.Name)" | Out-File $rapport -Append
}

# Pages
$pages = $lines | ForEach-Object {
    if ($_ -match '"GET ([^ ]+)') { $matches[1] }
}

"`nTop 5 pages :" | Out-File $rapport -Append
$pages | Group-Object | Sort-Object Count -Descending | Select-Object -First 5 |
ForEach-Object {
    "$($_.Count) $($_.Name)" | Out-File $rapport -Append
}

Write-Host "Rapport genere : $rapport"