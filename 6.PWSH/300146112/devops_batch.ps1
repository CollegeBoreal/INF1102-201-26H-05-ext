#!/usr/bin/env pwsh

$rapportTxt = "/devops-batch/rapport.txt"
$rapportJson = "/devops-batch/rapport.json"

$date = Get-Date
$user = whoami
$hostname = hostname

"===== RAPPORT DEVOPS =====" | Out-File $rapportTxt
"Date : $date" | Out-File $rapportTxt -Append
"Utilisateur : $user" | Out-File $rapportTxt -Append
"Machine : $hostname" | Out-File $rapportTxt -Append

$topCPU = Get-Process | Sort-Object CPU -Descending | Select-Object -First 5
$topMem = Get-Process | Sort-Object WS -Descending | Select-Object -First 5

$topCPU | Out-File $rapportTxt -Append
$topMem | Out-File $rapportTxt -Append

df -h | Out-File $rapportTxt -Append

$report = @{
    Date = $date
    User = $user
    Host = $hostname
}

$report | ConvertTo-Json | Out-File $rapportJson
