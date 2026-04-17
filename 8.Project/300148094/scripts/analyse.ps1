#!/usr/bin/env pwsh

$sites = @(
    "https://google.com",
    "https://github.com",
    "https://youtube.com",
    "https://wikipedia.org",
    "https://stackoverflow.com"
)

$rapport = "output/rapport.txt"

"Rapport Monitoring PowerShell - $(Get-Date)" | Out-File $rapport
"----------------------------------" | Out-File $rapport -Append

foreach ($site in $sites) {
    try {
        $start = Get-Date
        $response = Invoke-WebRequest -Uri $site -TimeoutSec 5 -UseBasicParsing
        $end = Get-Date
        $temps = ($end - $start).TotalSeconds
        $status = $response.StatusCode
        "OK $status - $([math]::Round($temps,2))s - $site" | Out-File $rapport -Append
        Write-Host "OK $status - $([math]::Round($temps,2))s - $site"
    } catch {
        "ERREUR - $site" | Out-File $rapport -Append
        Write-Host "ERREUR - $site"
    }
}

Write-Host "Rapport genere : $rapport"
python3 scripts/analyse.py
