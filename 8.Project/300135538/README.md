# 🌐 Projet Monitoring Web

## 🎯 Objectif

Ce projet permet de surveiller la disponibilité de plusieurs sites web et de mesurer leur temps de réponse.

L’analyse est réalisée avec Python et automatisée avec PowerShell.

---

## ⚙️ Fonctionnement

Le projet suit les étapes suivantes :

1. Lecture des sites depuis `data/sites.txt`
2. Analyse de chaque site (statut HTTP + temps de réponse)
3. Génération automatique des résultats

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
│ └── temps_reponse.png
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

Visualisation des temps de réponse des sites analysés.

📈 Exemple de résultat

Voici le graphique généré par le script :

## 📊 Graphique

![Graphique](300135538/images/temps_reponse.png)

📓 Rapport Jupyter

Le fichier RAPPORT.ipynb contient une présentation du projet et des résultats obtenus.

👤 Auteur

300135538
