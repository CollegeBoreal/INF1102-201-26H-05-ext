$log = Get-Content /var/log/nginx/access.log
$ips = $log | ForEach-Object {
    if ($_ -match '^(\d+\.\d+\.\d+\.\d+)') {
        $matches[1]
    }
}

$result = $ips | Group-Object | Sort-Object Count -Descending | Select-Object -First 10

$output = "REGEX/rapport_nginx_ps1_2026-03-31.txt"

$result | ForEach-Object {
    "$($_.Name) - $($_.Count)" | Out-File -Append $output
}

Write-Host "Rapport généré : $output"
