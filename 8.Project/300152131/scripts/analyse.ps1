Write-Host "=== DÉMARRAGE DE L'ANALYSE CRYPTO ==="

$scriptPath = Join-Path $PSScriptRoot "analyse.py"
python $scriptPath

Write-Host "=== ANALYSE TERMINÉE ==="
