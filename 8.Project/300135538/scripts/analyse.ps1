Write-Host "=== Monitoring des sites web ==="

# Aller dans le bon dossier
Set-Location $PSScriptRoot

# Lancer le script Python avec le bon chemin
python analyse.py ../data/sites.txt

Write-Host "=== Analyse terminée ==="