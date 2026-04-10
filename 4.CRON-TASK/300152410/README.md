# 👁️ Big Brother - Surveillance Nginx

**Étudiant :** Imad Boudeuf  
**Numéro :** 300152410  
**Cours :** INF1102-201-26H-05  

## Description
Script PowerShell qui extrait automatiquement les adresses IP des visiteurs du serveur Nginx et les sauvegarde dans un fichier.

## Fichiers
| Fichier | Description |
|---|---|
| `scruter_nginx.ps1` | Script principal d'extraction des IP |
| `nginx_ips.txt` | Liste des IP uniques des visiteurs |
| `nginx_ips_freq.txt` | IP les plus fréquentes avec comptage |

## Équivalences Linux → PowerShell
| Linux | PowerShell |
|---|---|
| `awk '{print $1}'` | `ForEach-Object { $_.Split(" ")[0] }` |
| `sort \| uniq` | `Sort-Object \| Get-Unique` |
| `uniq -c \| sort -nr` | `Group-Object \| Sort-Object Count -Descending` |
| `crontab -e` | `Register-ScheduledTask` |

## Automatisation
Tâche planifiée Windows : `ScraterNginx_imadboudeuf`  
Fréquence : toutes les heures