# 🌦️ PROJET_METEO

Pipeline automatisé de collecte et d'analyse de données météorologiques via l'API OpenWeatherMap.

---

## 📁 Structure du projet
```
PROJET_METEO/
├── data/
│   └── meteo.json          # Données brutes récupérées depuis l'API
├── output/
│   ├── rapport.txt         # Rapport texte généré automatiquement
│   └── meteo.png           # Graphique température / humidité
├── scripts/
│   ├── analyse.sh          # Script principal (pipeline Bash)
│   └── analyse.py          # Script d'analyse et de visualisation Python
└── README.md
```

---

## ⚙️ Fonctionnement

### 1. `analyse.sh` — Pipeline principal
1. Définit les chemins du projet dynamiquement
2. Crée les dossiers `data/` et `output/` si absents
3. Appelle l'API OpenWeatherMap pour **Toronto, CA** via `curl`
4. Vérifie que les données ont bien été récupérées
5. Lance le script Python `analyse.py`

### 2. `analyse.py` — Analyse et génération des sorties
- Extrait la **température** (°C), l'**humidité** (%) et la **ville**
- Génère un **graphique** (`output/meteo.png`) avec Matplotlib
- Produit un **rapport texte** (`output/rapport.txt`)

---

## 📊 Exemple de sortie
```
=== RAPPORT METEO ===

Ville: Toronto
Température: 1.94 °C
Humidité: 93 %
```

---

## 🚀 Utilisation
```bash
chmod +x scripts/analyse.sh
bash scripts/analyse.sh
```

---

## 🕐 Automatisation avec Cron
```cron
*/10 * * * * /home/ubuntu/PROJET_METEO/scripts/analyse.sh >> /home/ubuntu/PROJET_METEO/output/cron.log 2>&1
```

---

## 🛠️ Technologies utilisées

| Outil | Rôle |
|---|---|
| Bash | Orchestration du pipeline |
| Python 3 | Analyse des données |
| Matplotlib | Génération du graphique |
| curl | Appel à l'API REST |
| cron | Automatisation planifiée |
| OpenWeatherMap API | Source des données météo |
