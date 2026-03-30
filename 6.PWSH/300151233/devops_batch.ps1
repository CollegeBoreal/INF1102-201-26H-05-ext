#!/usr/bin/env pwsh

$rapportTxt = "rapport.txt"
$rapportJson = "rapport.json"

$date = Get-Date
$user = whoami
$hostname = hostname

"===== RAPPORT DEVOPS =====" | Out-File $rapportTxt
"Date : $date" | Out-File $rapportTxt -Append
"Utilisateur : $user" | Out-File $rapportTxt -Append
"Machine : $hostname" | Out-File $rapportTxt -Append

"Top 5 CPU :" | Out-File $rapportTxt -Append
Get-Process | Sort-Object CPU -Descending | Select-Object -First 5 Name,CPU | Out-File $rapportTxt -Append

"Top 5 Mémoire :" | Out-File $rapportTxt -Append
Get-Process | Sort-Object WS -Descending | Select-Object -First 5 Name,WS | Out-File $rapportTxt -Append

"Disque :" | Out-File $rapportTxt -Append
df -h | Out-File $rapportTxt -Append

$report = @{
    Date = $date
    User = $user
    Machine = $hostname
}

$report | ConvertTo-Json | Set-Content $rapportJson

"Rapports générés"
