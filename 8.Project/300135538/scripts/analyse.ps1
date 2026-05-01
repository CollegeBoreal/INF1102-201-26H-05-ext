Write-Host "=== Monitoring des sites web ==="

# Vérifier dossier output
if (!(Test-Path "../output")) {
    New-Item -ItemType Directory -Path "../output"
}

# Lancer Python
python ../scripts/analyse.py ../data/sites.txt

Write-Host "=== Analyse terminée ==="