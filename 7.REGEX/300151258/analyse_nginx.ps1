$content = Get-Content ./notes.txt -Raw

$ips = [regex]::Matches($content, '(?:[0-9]{1,3}\.){3}[0-9]{1,3}')

Write-Host "IPs trouvées :"
$ips | ForEach-Object { $_.Value }

