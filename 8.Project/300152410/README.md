# 📽️ Projet 5 – Monitoring site web

**Étudiant :** Imad Boudeuf  
**Numéro :** 300152410  
**Cours :** INF1102-201-26H-05  

## 🎯 Objectif
Surveiller la disponibilité et le temps de réponse de sites web.

## 📁 Structure
300152410/
├── scripts/
│   ├── analyse.ps1      # Script PowerShell principal
│   ├── analyse.py       # Script Python d'analyse
│   └── requirements.txt
├── data/
│   └── sample.log
├── output/
│   ├── rapport.txt      # Rapport généré automatiquement
│   └── analyse.txt      # Analyse Python
├── images/
├── RAPPORT.ipynb
└── README.md
## 🚀 Exécution
```powershell
powershell -ExecutionPolicy Bypass -File scripts/analyse.ps1
```

## 📊 Résultats
- google.com : 200 OK - 1335ms
- github.com : 200 OK - 6242ms
- wikipedia.org : 200 OK - 506ms