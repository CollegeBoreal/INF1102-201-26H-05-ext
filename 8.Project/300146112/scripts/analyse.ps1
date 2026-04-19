$input = "../data/sample.log"
$output = "../output/rapport.txt"

Write-Output "Analyse du fichier log" | Out-File $output

python ../scripts/analyse.py $input >> $output