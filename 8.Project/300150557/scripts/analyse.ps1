# ============================================
# analyse.ps1 — Suivi météo quotidienne
# Étudiant : Hani Damouche (300150557)
# Cours : INF1102 — Programmation système
# ============================================

$city = "Toronto,CA"
$apiKey = "4724a9add622fc59143cd5a5e66d5aae"
$dataDir = "$PSScriptRoot\..\data"
$outputDir = "$PSScriptRoot\..\output"

Write-Host "=== Récupération météo pour $city ==="

# Récupérer les données JSON de l'API
$response = Invoke-RestMethod -Uri "http://api.openweathermap.org/data/2.5/weather?q=$city&appid=$apiKey&units=metric&lang=fr"
$response | ConvertTo-Json | Out-File -Encoding utf8 "$dataDir\sample.log"

if (Test-Path "$dataDir\sample.log") {
    Write-Host "✅ Données récupérées avec succès"
} else {
    Write-Host "❌ Erreur lors de la récupération"
    exit 1
}

# Lancer l'analyse Python
Write-Host "=== Lancement de l'analyse Python ==="
python "$PSScriptRoot\analyse.py" "$dataDir\sample.log"

Write-Host "=== Terminé ==="
