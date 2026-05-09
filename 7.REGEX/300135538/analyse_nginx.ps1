# Analyse Regex PowerShell

$texte = @(
"192.168.1.10 GET /index.html 200",
"10.0.0.5 GET /login 404",
"172.16.0.8 GET /admin 500"
)

Write-Host "=== Analyse Logs ==="

# IP
Write-Host "`nIPs :"
$texte | ForEach-Object {
    if ($_ -match '(\d{1,3}(\.\d{1,3}){3})') {
        $matches[1]
    }
}

# Codes HTTP
Write-Host "`nCodes HTTP :"
$texte | ForEach-Object {
    if ($_ -match ' (200|404|500)$') {
        $matches[1]
    }
}

# Pages
Write-Host "`nPages :"
$texte | ForEach-Object {
    if ($_ -match 'GET ([^ ]+)') {
        $matches[1]
    }
}