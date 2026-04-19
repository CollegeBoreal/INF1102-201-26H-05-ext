$input = "..\data\300146112.log"
$output = "..\output\rapport.txt"

Write-Output "Analyse du fichier log" | Out-File $output

python "$PSScriptRoot\analyse.py" $input >> $output
