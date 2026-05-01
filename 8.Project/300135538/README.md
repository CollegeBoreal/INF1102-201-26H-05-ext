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

➡️ Lance automatiquement le script Python

3️⃣ Script Python
python scripts/analyse.py data/sites.txt

➡️ Analyse les sites
➡️ Génère les fichiers output

🧪 Test du script

Exécution :

python scripts/analyse.py data/sites.txt

Résultat attendu :

Analyse en cours...
Analyse terminée.
Fichiers générés dans le dossier output.
📊 Résultats
📄 Rapport texte

output/rapport.txt

Contient :

liste des sites
statut HTTP
temps de réponse
📈 Graphique

output/temps_reponse.png

➡️ Visualisation des temps de réponse

📊 CSV

output/resultats.csv

➡️ Données exploitables

🖼️ Captures

Ajoute ici tes images :

images/
   ├── execution.png
   ├── graphique.png

Exemple :

👤 Auteur
Étudiant : 300135538
Projet académique