#!/usr/bin/env pwsh

Write-Host "=== Analyse de logs - 300150296 ===" -ForegroundColor Green

$logFile = "data/sample.log"
$outputFile = "output/rapport.txt"

"Génération du rapport..." | Out-File $outputFile
"Date: $(Get-Date)" | Out-File $outputFile -Append
"-----------------------------------" | Out-File $outputFile -Append

# Appel Python
python3 scripts/analyse.py $logFile | Out-File $outputFile -Append

Write-Host "✅ Rapport généré: $outputFile" -ForegroundColor Green