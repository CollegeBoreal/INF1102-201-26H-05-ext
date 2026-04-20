# ==========================================
# 🌦️ Projet : Suivi météo quotidienne
# PowerShell Script
# ==========================================

Write-Host "🌍 Récupération des données météo..."

# 🔧 CONFIGURATION
$city = "Toronto,CA"
$apiKey = "67f475e5835cd25c4201b6f01d354c66"   # ⚠️ Remplacer par ta clé OpenWeather
$jsonFile = "data/meteo.json"
$logFile = "output/errors.log"

# 📁 Créer dossiers si inexistants
if (!(Test-Path "data")) { New-Item -ItemType Directory -Path "data" }
if (!(Test-Path "output")) { New-Item -ItemType Directory -Path "output" }

# 🌐 URL API
$url = "http://api.openweathermap.org/data/2.5/weather?q=$city&appid=$apiKey&units=metric"

try {
    # 📡 Appel API
    $response = Invoke-RestMethod -Uri $url -Method Get

    # 💾 Sauvegarde JSON
    $response | ConvertTo-Json -Depth 5 | Out-File $jsonFile

    Write-Host "✅ Données météo récupérées et sauvegardées"

    # 🐍 Appel script Python
    Write-Host "📊 Analyse en cours..."
    python scripts/analyse.py $jsonFile

    Write-Host "🎉 Projet terminé avec succès !"
}
catch {
    # 💥 Gestion des erreurs
    $errorMessage = "[$(Get-Date)] ERREUR : $($_.Exception.Message)"
    $errorMessage | Out-File $logFile -Append

    Write-Host "💥 Erreur détectée ! Voir output/errors.log"
}
