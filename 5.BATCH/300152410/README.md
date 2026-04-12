# 🖥️ TP – Script Batch de Gestion Système

**Étudiant :** Imad Boudeuf  
**Numéro :** 300152410  
**Cours :** INF1102-201-26H-05  

## 🎯 Objectif
Automatiser des tâches d'administration système via un script PowerShell (équivalent Bash).

## 📁 Structure créée
C:\entreprise
├── data
│   ├── fichier1.txt
│   └── fichier2.txt
├── backup
│   ├── fichier1.txt
│   ├── fichier2.txt
│   └── backup_2026-04-10.zip
└── logs
└── log.txt
## ✅ Tâches réalisées
1. Vérification réseau (ping 8.8.8.8)
2. Sauvegarde des fichiers
3. Création utilisateur temporaire (employe_temp)
4. Compression archive .zip
5. Planification automatique à 2h00

## ⏰ Planification
Tâche Windows : `ScriptGestion_imadboudeuf`  
Fréquence : tous les jours à 2h00

## 🔄 Équivalences Linux → PowerShell
| Linux | PowerShell |
|---|---|
| `cp -r` | `Copy-Item` |
| `tar -czvf` | `Compress-Archive` |
| `useradd` | `New-LocalUser` |
| `crontab -e` | `Register-ScheduledTask` |
| `ping -c 4` | `ping -n 4` |
## ✅ Tâches réalisées
1. Vérification réseau (ping 8.8.8.8)
2. Sauvegarde des fichiers
3. Création utilisateur temporaire (employe_temp)
4. Compression archive .zip
5. Planification automatique à 2h00

## ⏰ Planification
Tâche Windows : `ScriptGestion_imadboudeuf`  
Fréquence : tous les jours à 2h00

## 🔄 Équivalences Linux → PowerShell
| Linux | PowerShell |
|---|---|
| `cp -r` | `Copy-Item` |
| `tar -czvf` | `Compress-Archive` |
| `useradd` | `New-LocalUser` |
| `crontab -e` | `Register-ScheduledTask` |
| `ping -c 4` | `ping -n 4` |