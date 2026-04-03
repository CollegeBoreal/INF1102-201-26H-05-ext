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

Le script Bash orchestre l'ensemble du pipeline :

1. Définit les chemins du projet dynamiquement (`dirname`)
2. Crée les dossiers `data/` et `output/` si absents
3. Appelle l'API OpenWeatherMap pour la ville de **Toronto, CA** via `curl`
4. Vérifie que les données ont bien été récupérées
5. Lance le script Python `analyse.py`
6. Affiche un message de succès ou d'erreur à chaque étape

### 2. `analyse.py` — Analyse et génération des sorties

Le script Python :

- Charge les données météo depuis `data/meteo.json`
- Extrait la **température** (°C), l'**humidité** (%) et le **nom de la ville**
- Génère un **graphique à barres** (`output/meteo.png`) avec Matplotlib
- Produit un **rapport texte** (`output/rapport.txt`)

---

## 📊 Exemple de sortie

### `rapport.txt`

```
=== RAPPORT METEO ===

Ville: Toronto
Température: 1.94 °C
Humidité: 93 %
```

### `meteo.png`

Graphique à barres affichant la température et l'humidité pour Toronto.

---

## 🚀 Utilisation

### Prérequis

- Python 3 avec `matplotlib` installé
- `curl` disponible sur le système
- Une clé API valide sur [OpenWeatherMap](https://openweathermap.org/api)

### Rendre le script exécutable

```bash
chmod +x scripts/analyse.sh
```

### Lancer manuellement le pipeline

```bash
cd scripts/
bash analyse.sh
```

### Résultat attendu

```
===== PIPELINE METEO =====
[1] Récupération météo...
✅ Données récupérées
[2] Lancement analyse Python...
✅ Rapport généré
✅ Pipeline terminé
```

---

## 🕐 Automatisation avec Cron

Le pipeline est planifié pour s'exécuter automatiquement **toutes les 10 minutes** via `crontab` :

```cron
*/10 * * * * /home/ubuntu/PROJET_METEO/scripts/analyse.sh >> /home/ubuntu/PROJET_METEO/output/cron.log 2>&1
```

Pour modifier la planification :

```bash
crontab -e
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
