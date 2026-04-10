# Fichier des logs
$LOG_FILE = "C:\tools\nginx-1.29.8\logs\access.log"

# Fichier de sortie
$OUTPUT_FILE = "C:\Users\Hocine\nginx_ips.txt"

# Fichier de log d'exécution
$LOG_EXEC = "C:\Users\Hocine\nginx_ips.log"

# Extraire les IP uniques et les stocker
Get-Content $LOG_FILE | ForEach-Object { $_.Split(" ")[0] } | Sort-Object | Get-Unique | Out-File $OUTPUT_FILE

# Ajouter un timestamp à chaque exécution
"Script exécuté le $(Get-Date)" | Out-File -Append $LOG_EXEC