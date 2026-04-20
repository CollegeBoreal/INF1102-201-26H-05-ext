# 🌦️ PROJET\_METEO

> Pipeline automatisé de collecte, d'analyse et de visualisation de données météorologiques via l'API OpenWeatherMap.

![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)
![Python](https://img.shields.io/badge/Python_3-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white)
![OpenWeatherMap](https://img.shields.io/badge/OpenWeatherMap_API-EB6E4B?style=for-the-badge&logo=icloud&logoColor=white)
![Cron](https://img.shields.io/badge/Cron-Automatisé-0078D4?style=for-the-badge&logo=linux&logoColor=white)

---

## 📋 Table des matières

- [Aperçu](#-aperçu)
- [Structure du projet](#-structure-du-projet)
- [Fonctionnement](#-fonctionnement)
- [Exemple de sortie](#-exemple-de-sortie)
- [Installation & Utilisation](#-installation--utilisation)
- [Automatisation avec Cron](#-automatisation-avec-cron)
- [Technologies utilisées](#-technologies-utilisées)

---

## 🔍 Aperçu

**PROJET\_METEO** est un pipeline de données léger et entièrement automatisé qui :

- 📡 **Collecte** les données météo en temps réel via l'API OpenWeatherMap
- 🐍 **Analyse** les données avec Python
- 📊 **Visualise** les résultats sous forme de graphique (`meteo.png`)
- 📝 **Génère** un rapport texte structuré (`rapport.txt`)
- ⏰ **S'exécute automatiquement** toutes les 10 minutes grâce à `cron`

---

## 📁 Structure du projet

```
PROJET_METEO/
├── data/
│   └── meteo.json          # Données brutes récupérées depuis l'API
├── output/
│   ├── rapport.txt         # Rapport texte généré automatiquement
│   ├── meteo.png           # Graphique température / humidité
│   └── cron.log            # Journal d'exécution automatique
├── scripts/
│   ├── analyse.sh          # Script principal (pipeline Bash)
│   └── analyse.py          # Script d'analyse et de visualisation Python
└── README.md
```

---

## ⚙️ Fonctionnement

Le pipeline s'articule en deux étapes complémentaires :

### 1. `analyse.sh` — Orchestration du pipeline

Le script Bash est le point d'entrée du pipeline. Il :

1. Définit les chemins du projet de manière dynamique via `dirname`
2. Crée automatiquement les dossiers `data/` et `output/` s'ils sont absents
3. Interroge l'API OpenWeatherMap pour la ville de **Toronto, CA** via `curl`
4. Vérifie l'intégrité des données récupérées
5. Délègue l'analyse au script Python `analyse.py`
6. Affiche un retour clair (✅ succès / ❌ erreur) à chaque étape

### 2. `analyse.py` — Analyse et génération des sorties

Le script Python prend le relais pour :

- Charger et parser les données météo depuis `data/meteo.json`
- Extraire la **température** (°C), l'**humidité** (%) et le **nom de la ville**
- Générer un **graphique à barres** (`output/meteo.png`) avec Matplotlib
- Produire un **rapport texte** lisible (`output/rapport.txt`)

---

## 📤 Exemple de sortie

### `rapport.txt`

```
=== RAPPORT METEO ===
Ville       : Toronto
Température : 1.94 °C
Humidité    : 93 %
```

### `meteo.png`

Graphique à barres comparant la **température** et l'**humidité** pour la ville de Toronto, généré automatiquement à chaque exécution du pipeline.

---

## 🚀 Installation & Utilisation

### Prérequis

| Dépendance | Détail |
|---|---|
| Python 3 | Avec `matplotlib` installé (`pip install matplotlib`) |
| `curl` | Disponible nativement sur Linux/macOS |
| Clé API | Créer un compte sur [OpenWeatherMap](https://openweathermap.org/api) |

### Étape 1 — Cloner le projet

```bash
git clone https://github.com/votre-utilisateur/PROJET_METEO.git
cd PROJET_METEO
```

### Étape 2 — Configurer la clé API

Dans `scripts/analyse.sh`, remplacez la valeur de `API_KEY` par votre clé personnelle :

```bash
API_KEY="votre_clé_api_ici"
```

### Étape 3 — Rendre le script exécutable

```bash
chmod +x scripts/analyse.sh
```

### Étape 4 — Lancer le pipeline manuellement

```bash
bash scripts/analyse.sh
```

### Résultat attendu dans le terminal

```
===== PIPELINE METEO =====
[1] Récupération météo...
✅ Données récupérées
[2] Lancement analyse Python...
✅ Rapport généré
✅ Pipeline terminé
```

---

## ⏰ Automatisation avec Cron

Le pipeline est planifié pour s'exécuter automatiquement **toutes les 10 minutes** via `crontab`.

### Entrée cron configurée

```cron
*/10 * * * * /home/ubuntu/PROJET_METEO/scripts/analyse.sh >> /home/ubuntu/PROJET_METEO/output/cron.log 2>&1
```

### Modifier la planification

```bash
crontab -e
```

> 💡 **Astuce :** Consultez [crontab.guru](https://crontab.guru) pour construire facilement vos expressions cron.

---

## 🛠️ Technologies utilisées

| Outil | Rôle |
|---|---|
| **Bash** | Orchestration du pipeline |
| **Python 3** | Traitement et analyse des données |
| **Matplotlib** | Génération du graphique |
| **curl** | Appel HTTP à l'API REST |
| **cron** | Automatisation planifiée |
| **OpenWeatherMap API** | Source des données météorologiques |

---

## 📄 Licence

Ce projet est distribué à des fins éducatives et personnelles. Libre d'utilisation et de modification.

---

<p align="center">
  Fait avec ☁️ et ☕ — Pipeline météo automatisé pour Toronto, CA
</p>
