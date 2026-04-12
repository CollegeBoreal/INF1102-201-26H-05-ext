# ============================================
# Script de gestion système - Imad Boudeuf
# 300152410
# ============================================

$LOG = "C:\entreprise\logs\log.txt"
$DATE = Get-Date

"===================================" | Out-File -Append $LOG
"Début exécution : $DATE" | Out-File -Append $LOG

# 1. Vérification réseau
"Test réseau..." | Out-File -Append $LOG
ping -n 4 8.8.8.8 | Out-File -Append $LOG

# 2. Sauvegarde des fichiers
"Sauvegarde en cours..." | Out-File -Append $LOG
Copy-Item C:\entreprise\data\* C:\entreprise\backup\
"Sauvegarde terminée." | Out-File -Append $LOG

# 3. Création utilisateur temporaire
$USER_TEMP = "employe_temp"
$UserExists = Get-LocalUser -Name $USER_TEMP -ErrorAction SilentlyContinue

if ($UserExists) {
    "Utilisateur existe déjà." | Out-File -Append $LOG
} else {
    $Password = ConvertTo-SecureString "Temp1234" -AsPlainText -Force
    New-LocalUser -Name $USER_TEMP -Password $Password -FullName "Employe Temporaire"
    "Utilisateur créé." | Out-File -Append $LOG
}

# 4. Compression archive
$ArchiveName = "C:\entreprise\backup\backup_$(Get-Date -Format 'yyyy-MM-dd').zip"
Compress-Archive -Path C:\entreprise\data\* -DestinationPath $ArchiveName -Force
"Archive créée : $ArchiveName" | Out-File -Append $LOG

"Fin exécution : $(Get-Date)" | Out-File -Append $LOG
"===================================" | Out-File -Append $LOG