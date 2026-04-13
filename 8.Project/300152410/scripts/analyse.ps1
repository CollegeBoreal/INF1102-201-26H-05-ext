# =====================================
# Projet 5 - Monitoring site web
# Auteur : Imad Boudeuf
# Boreal ID : 300152410
# =====================================

$sites = @("https://www.google.com", "https://www.github.com", "https://www.wikipedia.org")
$rapport = "C:\Users\Hocine\INF1102-201-26H-05\8.Project\300152410\output\rapport.txt"

"===== RAPPORT MONITORING SITES WEB =====" | Out-File $rapport
"Date : $(Get-Date)" | Out-File $rapport -Append
"----------------------------------------" | Out-File $rapport -Append

foreach ($site in $sites) {
    try {
        $start = Get-Date
        $response = Invoke-WebRequest -Uri $site -TimeoutSec 10 -UseBasicParsing
        $end = Get-Date
        $duration = ($end - $start).TotalMilliseconds
        "$site - Status: $($response.StatusCode) - Temps: $([math]::Round($duration))ms" | Out-File $rapport -Append
        Write-Host "OK : $site - $($response.StatusCode) - $([math]::Round($duration))ms"
    } catch {
        "$site - ERREUR : $($_.Exception.Message)" | Out-File $rapport -Append
        Write-Host "ERREUR : $site"
    }
}

"----------------------------------------" | Out-File $rapport -Append
"Fin monitoring : $(Get-Date)" | Out-File $rapport -Append

# Appel Python pour analyse
python C:\Users\Hocine\INF1102-201-26H-05\8.Project\300152410\scripts\analyse.py

Write-Host "Rapport genere : $rapport"