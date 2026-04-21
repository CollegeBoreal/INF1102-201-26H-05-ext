# 🌤️ Suivi Météo Quotidienne — Projet INF1102

**Étudiant** : Hani Damouche (300150557)  
**Cours** : INF1102 — Programmation système  
**Environnement** : Ubuntu 22.04 LTS / Windows PowerShell  
**Date** : 2026-04-21
 
---

## 1. Objectif

Ce projet consiste à récupérer les données météo d'une ville via l'API **OpenWeatherMap** et à générer :
- Un **fichier texte** (`output/rapport.txt`) automatique avec les statistiques
- Un **graphique** (`output/meteo.png`) des conditions météo
- Un **rapport Jupyter** (`RAPPORT.ipynb`) avec visualisations et commentaires

## 2. Structure du projet

```
300150557/
├── scripts/
│   ├── analyse.sh         # Script Bash principal (appel API + lancement Python)
│   ├── analyse.py         # Script Python (analyse JSON + graphique)
│   └── requirements.txt   # Dépendances Python
├── data/
│   └── sample.log         # Données JSON récupérées de l'API
├── output/
│   ├── rapport.txt        # Rapport texte généré automatiquement
│   └── meteo.png          # Graphique généré automatiquement
├── RAPPORT.ipynb           # Rapport Jupyter avec visualisations
└── README.md               # Ce fichier
```

## 3. Installation

### Prérequis
- Python >= 3.8
- Bash (Linux/WSL) ou PowerShell (Windows)
- `curl` (pour le script Bash)
- Jupyter Notebook

### Dépendances Python
```bash
pip install -r scripts/requirements.txt
```

## 4. Exécution

### Méthode 1 : Script Bash (Linux / WSL)
```bash
bash scripts/analyse.sh
```

### Méthode 2 : PowerShell (Windows)
```powershell
# Récupérer les données météo
Invoke-RestMethod -Uri "http://api.openweathermap.org/data/2.5/weather?q=Toronto,CA&appid=VOTRE_API_KEY&units=metric&lang=fr" | ConvertTo-Json | Out-File -Encoding utf8 .\data\sample.log

# Lancer l'analyse Python
python .\scripts\analyse.py .\data\sample.log
```

### Méthode 3 : Python seul
```bash
python3 scripts/analyse.py data/sample.log
```

### Ouvrir le rapport Jupyter
```bash
jupyter notebook RAPPORT.ipynb
```

## 5. Résultat attendu

- `output/rapport.txt` : statistiques principales (température, humidité, vent, pression)
- `output/meteo.png` : graphique à barres des données météo
- `RAPPORT.ipynb` : explications, visualisations multiples, analyse approfondie

## 6. API utilisée

- **OpenWeatherMap** : https://openweathermap.org/api
- Endpoint : `http://api.openweathermap.org/data/2.5/weather`
- Paramètres : ville, clé API, unités métriques, langue française

## 7. Bonnes pratiques

- ✅ Scripts lisibles et commentés
- ✅ Structure de dossiers respectée
- ✅ Rapport Jupyter avec texte explicatif et graphiques
- ✅ Données générées automatiquement par les scripts
- ✅ Gestion des erreurs dans le code Python
- ✅ Encodage UTF-8 pour les caractères français
