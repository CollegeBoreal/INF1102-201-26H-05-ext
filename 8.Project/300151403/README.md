# 📽️Données COVID 19

**5 idées de projets Web Scraping / API / automatisation** adaptées au cours, avec **consignes, scripts, Notebook et livrables attendus**, prêts à distribuer aux étudiants.

---
# 🦠 Projet COVID-19 — Pipeline ETL automatisé

## 1. Objectif
Ce projet met en place un pipeline ETL complet qui :
- **Extrait** les données COVID-19 du Canada via une API publique
- **Transforme** les données (nettoyage, calculs, déduplication)
- **Charge** les résultats en CSV, JSON et SQLite
- **Génère** un graphique et un rapport texte automatiquement

## 2. Structure du projet
```
MonProjet/
├── scripts/
│   ├── analyse.sh        # Chef d'orchestre Bash
│   └── analyse.py        # Pipeline ETL Python
├── data/
│   ├── covid.csv         # Données transformées (CSV)
│   ├── covid.json        # Données transformées (JSON)
│   └── covid.db          # Base de données SQLite
├── output/
│   ├── rapport.txt       # Rapport généré automatiquement
│   ├── graphique_covid.png  # Graphique généré
│   └── execution.log     # Journal des exécutions
├── RAPPORT.ipynb         # Rapport Jupyter commenté
└── README.md             # Ce fichier
```

## 3. Installation
```bash
pip3 install requests matplotlib jupyter
```

## 4. Exécution
```bash
# Lancer le projet complet
bash scripts/analyse.sh

# Ou lancer Python seul
python3 scripts/analyse.py

# Ouvrir le rapport Jupyter
jupyter notebook RAPPORT.ipynb
