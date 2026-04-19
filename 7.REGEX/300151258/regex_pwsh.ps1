$text = Get-Content ./notes.txt -Raw

Write-Host "=== Emails ==="
[regex]::Matches($text, '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}') | ForEach-Object { $_.Value }

Write-Host "`n=== Téléphones ==="
[regex]::Matches($text, '[0-9]{3}-[0-9]{3}-[0-9]{4}') | ForEach-Object { $_.Value }

Write-Host "`n=== Dates ==="
[regex]::Matches($text, '[0-9]{4}-[0-9]{2}-[0-9]{2}') | ForEach-Object { $_.Value }

Write-Host "`n=== IP ==="
[regex]::Matches($text, '([0-9]{1,3}\.){3}[0-9]{1,3}') | ForEach-Object { $_.Value }
