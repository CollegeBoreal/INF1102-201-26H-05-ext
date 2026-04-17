# 6️⃣ PWSH – Batch DevOps PowerShell

**Étudiant :** Imad Boudeuf  
**Numéro :** 300152410  
**Cours :** INF1102-201-26H-05  
**Environnement :** Windows 11 + PowerShell  

## 🎯 Objectifs
1. Créer un script batch PowerShell
2. Vérifier l'état du système (CPU, mémoire, disque)
3. Vérifier la connectivité réseau (SSH)
4. Générer un rapport texte et JSON

## 📁 Structure
C:\devops-batch
├── rapport.txt       # Rapport texte généré
└── rapport.json      # Rapport JSON généré
## 🚀 Exécution
```powershell
powershell -ExecutionPolicy Bypass -File devops_batch.ps1
```

## 📊 Résultat obtenu
- Top 5 CPU : sqlservr, dwm, services, System, SSMS
- Top 5 mémoire : chrome, vmmem, MsMpEng
- Disque C: 82GB utilisés / 45GB libres

## 🔄 Comparatif Bash vs PowerShell
| Bash | PowerShell |
|---|---|
| `ps aux` | `Get-Process` |
| `df -h` | `Get-PSDrive` |
| `grep` | `Where-Object` |
| `jq` | `ConvertTo-Json` |