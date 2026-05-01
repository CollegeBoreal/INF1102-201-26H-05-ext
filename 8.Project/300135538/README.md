# 🌐 Projet Monitoring Web — Analyse de disponibilité des sites

Projet réalisé avec Python et PowerShell pour analyser la disponibilité de sites web, mesurer le temps de réponse et générer un rapport automatique.

---

## 📋 Table des matières

- Aperçu du projet
- Structure du projet
- Technologies utilisées
- Fonctionnement
- Test du script
- Résultats
- Auteur

---

## 🔍 Aperçu du projet

Ce projet permet de surveiller plusieurs sites web et d’analyser :

- ✔ disponibilité des sites  
- ✔ temps de réponse  
- ✔ statut HTTP  

Pipeline :


data/sites.txt
↓
[ analyse.ps1 ]
↓
[ analyse.py ]
↓
output/
├── rapport.txt
├── resultats.csv
└── temps_reponse.png


---

## 📁 Structure du projet


300135538/
├── data/
│ └── sites.txt
├── scripts/
│ ├── analyse.ps1
│ ├── analyse.py
│ └── requirements.txt
├── output/
│ ├── rapport.txt
│ ├── resultats.csv
│ └── temps_reponse.png
├── images/
├── RAPPORT.ipynb
└── README.md


---

## 🛠️ Technologies utilisées

| Outil | Rôle |
|------|------|
| Python | Analyse des données |
| PowerShell | Automatisation |
| CSV | Stockage des résultats |
| Notebook Jupyter | Rapport |

---

## ⚙️ Fonctionnement

### 1️⃣ Lecture des sites

Le fichier `data/sites.txt` contient la liste des sites :


https://www.google.com

https://www.github.com

https://error.com


---

### 2️⃣ Script PowerShell

```powershell
.\scripts\analyse.ps1

# 🌐 Projet Monitoring Web

## 🎯 Objectif

Ce projet permet de surveiller la disponibilité de plusieurs sites web et de mesurer leur temps de réponse.

L’analyse est réalisée avec Python et automatisée avec PowerShell.

---

## ⚙️ Fonctionnement

Le projet suit les étapes suivantes :

1. Lecture d’une liste de sites web (`data/sites.txt`)
2. Analyse de chaque site (statut + temps de réponse)
3. Génération des résultats dans le dossier `output`

---

## 📁 Structure du projet


300135538/
├── data/
│ └── sites.txt
├── scripts/
│ ├── analyse.ps1
│ └── analyse.py
├── output/
│ ├── rapport.txt
│ ├── resultats.csv
│ └── temps_reponse.png
├── images/
├── RAPPORT.ipynb
└── README.md


---

## 🚀 Exécution

### ▶️ PowerShell

```powershell
.\scripts\analyse.ps1
▶️ Python
python scripts/analyse.py data/sites.txt
📊 Résultats

Après exécution, les fichiers suivants sont générés :

📄 Rapport texte

output/rapport.txt

Contient :

liste des sites
statut HTTP
disponibilité
temps de réponse
📊 Données CSV

output/resultats.csv

Permet d’exploiter les résultats sous forme de tableau.

📈 Graphique

output/temps_reponse.png

Visualisation des temps de réponse des sites.

🖼️ Exemple de résultat

📓 Rapport Jupyter

Le fichier RAPPORT.ipynb contient une présentation du projet et des résultats obtenus.




👤 Auteur
Étudiant : 300135538
Projet académique