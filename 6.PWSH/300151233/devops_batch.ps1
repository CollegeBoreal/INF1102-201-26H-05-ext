#!/usr/bin/env pwsh

<<<<<<< HEAD
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
=======
$rapportTxt  = "$HOME/devops-batch/rapport.txt"
$rapportJson = "$HOME/devops-batch/rapport.json"

if (-not (Test-Path "$HOME/devops-batch")) {
    New-Item -ItemType Directory -Path "$HOME/devops-batch" | Out-Null
}

$date     = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$hostname = hostname
$user     = whoami

Write-Output "===== RAPPORT DEVOPS =====" | Tee-Object -FilePath $rapportTxt
Write-Output "Date : $date" | Tee-Object -FilePath $rapportTxt -Append
Write-Output "Utilisateur : $user" | Tee-Object -FilePath $rapportTxt -Append
Write-Output "Machine : $hostname" | Tee-Object -FilePath $rapportTxt -Append
Write-Output "" | Tee-Object -FilePath $rapportTxt -Append

Write-Output "Top 5 processus par CPU :" | Tee-Object -FilePath $rapportTxt -Append
$topCPU = Get-Process | Sort-Object CPU -Descending | Select-Object -First 5
foreach ($p in $topCPU) {
    Write-Output ("{0} - CPU: {1}" -f $p.ProcessName, $p.CPU) | Tee-Object -FilePath $rapportTxt -Append
}

Write-Output "" | Tee-Object -FilePath $rapportTxt -Append
Write-Output "Top 5 processus par mémoire :" | Tee-Object -FilePath $rapportTxt -Append
$topMem = Get-Process | Sort-Object WS -Descending | Select-Object -First 5
foreach ($p in $topMem) {
    Write-Output ("{0} - Mémoire: {1}" -f $p.ProcessName, $p.WorkingSet) | Tee-Object -FilePath $rapportTxt -Append
}

Write-Output "" | Tee-Object -FilePath $rapportTxt -Append
Write-Output "Espace disque :" | Tee-Object -FilePath $rapportTxt -Append
$disk = df -h
Write-Output $disk | Tee-Object -FilePath $rapportTxt -Append

Write-Output "" | Tee-Object -FilePath $rapportTxt -Append
$sshHost = "127.0.0.1"
Write-Output "Test SSH vers $sshHost :" | Tee-Object -FilePath $rapportTxt -Append
try {
    $result = ssh -o BatchMode=yes -o ConnectTimeout=5 $sshHost "echo OK" 2>&1
    Write-Output "Résultat : $result" | Tee-Object -FilePath $rapportTxt -Append
}
catch {
    Write-Output "SSH échoué vers $sshHost" | Tee-Object -FilePath $rapportTxt -Append
}

Write-Output "" | Tee-Object -FilePath $rapportTxt -Append

$reportObj = [PSCustomObject]@{
    Date        = $date
    Utilisateur = $user
    Machine     = $hostname
    TopCPU      = $topCPU | ForEach-Object {
        [PSCustomObject]@{ Process = $_.ProcessName; CPU = $_.CPU }
    }
    TopMemory   = $topMem | ForEach-Object {
        [PSCustomObject]@{ Process = $_.ProcessName; Memory = $_.WorkingSet }
    }
    Disk        = $disk
}

$reportObj | ConvertTo-Json -Depth 5 | Set-Content $rapportJson

Write-Output ""
Write-Output "Rapports générés : $rapportTxt et $rapportJson"
>>>>>>> d4ba147 (Ajout du script devops_batch.ps1)
