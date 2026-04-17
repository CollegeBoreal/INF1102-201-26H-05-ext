\#!/usr/bin/env pwsh



$report = \[PSCustomObject]@{

&#x20;   Date      = Get-Date

&#x20;   Hostname  = hostname

&#x20;   TopMemory = Get-Process | Sort-Object WS -Descending | Select-Object -First 5 Name, WS

&#x20;   Disk      = df -h

}



$report | ConvertTo-Json -Depth 3 | Out-File report.json

Write-Host "Rapport généré : report.json"

