#!/usr/bin/env pwsh

$rapportTxt = "/devops-batch/rapport.txt"
$rapportJson = "/devops-batch/rapport.json"

$date = Get-Date
$user = whoami
$machine = hostname

"===== RAPPORT DEVOPS =====" | Set-Content $rapportTxt
"Date : $date" | Add-Content $rapportTxt
"Utilisateur : $user" | Add-Content $rapportTxt
"Machine : $machine" | Add-Content $rapportTxt
"" | Add-Content $rapportTxt

"Top 5 processus par CPU :" | Add-Content $rapportTxt
$topCPU = Get-Process | Sort-Object CPU -Descending | Select-Object -First 5
foreach ($p in $topCPU) {
    "$($p.ProcessName) - CPU: $($p.CPU)" | Add-Content $rapportTxt
}

"" | Add-Content $rapportTxt
"Top 5 processus par mémoire :" | Add-Content $rapportTxt
$topMemory = Get-Process | Sort-Object WS -Descending | Select-Object -First 5
foreach ($p in $topMemory) {
    "$($p.ProcessName) - Mémoire: $($p.WorkingSet)" | Add-Content $rapportTxt
}

"" | Add-Content $rapportTxt
"Espace disque :" | Add-Content $rapportTxt
$disk = df -h
$disk | Add-Content $rapportTxt

"" | Add-Content $rapportTxt
"Test SSH vers 127.0.0.1 :" | Add-Content $rapportTxt

try {
    $sshResult = ssh -o BatchMode=yes -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null 127.0.0.1 "echo OK" 2>&1
    "Résultat : $sshResult" | Add-Content $rapportTxt
}
catch {
    "Résultat : SSH échoué" | Add-Content $rapportTxt
}

$report = [PSCustomObject]@{
    Date        = $date
    Utilisateur = $user
    Machine     = $machine
    TopCPU      = $topCPU | ForEach-Object {
        [PSCustomObject]@{
            Process = $_.ProcessName
            CPU     = $_.CPU
        }
    }
    TopMemory   = $topMemory | ForEach-Object {
        [PSCustomObject]@{
            Process = $_.ProcessName
            Memory  = $_.WorkingSet
        }
    }
    Disk        = $disk
    SSHTest     = $sshResult
}

$report | ConvertTo-Json -Depth 5 | Set-Content $rapportJson

"Rapports générés : $rapportTxt et $rapportJson" | Add-Content $rapportTxt
Write-Output "Rapports générés : $rapportTxt et $rapportJson"
