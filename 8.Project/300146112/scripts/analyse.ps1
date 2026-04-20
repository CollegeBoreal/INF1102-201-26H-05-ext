$input = "..\data\300146112.log"
$output = "..\output\rapport.txt"

Write-Output "" | Out-File $output
python .\scripts\analyse.py $input >> $output
