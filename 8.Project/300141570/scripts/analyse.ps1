$lines = Get-Content "data/access.log"

$total = $lines.Count
$errors = 0
$errors404 = 0
$errors500 = 0

foreach ($line in $lines) {
    if ($line -match " 4\d\d " -or $line -match " 5\d\d ") {
        $errors++
    }
    if ($line -match " 404 ") {
        $errors404++
    }
    if ($line -match " 500 ") {
        $errors500++
    }
}

Write-Output "Total requêtes : $total"
Write-Output "Total erreurs : $errors"
Write-Output "Erreurs 404 : $errors404"
Write-Output "Erreurs 500 : $errors500"
