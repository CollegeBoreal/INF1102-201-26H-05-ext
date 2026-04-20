# 🌦️ PROJET_METEO

<p align="center">
  <img src="https://img.shields.io/badge/Bash-Pipeline-blue?style=for-the-badge&logo=gnu-bash">
  <img src="https://img.shields.io/badge/Python-Analysis-yellow?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/API-OpenWeather-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Automation-Cron-success?style=for-the-badge&logo=linux">
</p>

<p align="center">
  <b>Pipeline automatisé de collecte et d'analyse de données météorologiques</b><br>
  Bash • Python • API • Data Visualization • Automation
</p>

---

## 🎬 Demo du pipeline

<p align="center">
  <img src="https://media.giphy.com/media/coxQHKASG60HrHtvkt/giphy.gif" width="700">
</p>

<p align="center">
⚡ Collecte → Analyse → Rapport → Graphique
</p>

---

## 🚀 Présentation

**PROJET_METEO** est un pipeline automatisé permettant de :

- 📡 Collecter des données météo en temps réel
- ⚙️ Analyser les données avec Python
- 📊 Générer des visualisations
- 📄 Produire des rapports automatisés
- ⏱️ Automatiser l’exécution avec cron

👉 Objectif : démontrer un **workflow DevOps appliqué à la data**.

---

## 🧠 Architecture du pipeline

---

## ⚙️ Fonctionnement

### 🔹 1. Pipeline Bash — `analyse.sh`

Le script Bash orchestre l'ensemble du pipeline :

- Détection des chemins dynamiques (`dirname`)
- Création des dossiers `data/` et `output/`
- Appel API OpenWeatherMap (Toronto, CA) via `curl`
- Vérification de la récupération des données
- Exécution du script Python
- Logs avec statuts clairs ✅ / ❌

---

### 🔹 2. Analyse Python — `analyse.py`

Le script Python :

- Charge les données depuis `data/meteo.json`
- Extrait :
  - 🌡️ Température (°C)
  - 💧 Humidité (%)
  - 📍 Ville
- Génère :
  - 📊 Graphique (`output/meteo.png`)
  - 📄 Rapport (`output/rapport.txt`)

---

## 📊 Exemple de sortie

### 📄 rapport.txt

---

### 📈 meteo.png

Graphique à barres affichant :
- Température
- Humidité

---

## 🛠️ Installation & utilisation

### 📌 Prérequis

- Python 3
- matplotlib
- curl
- Clé API OpenWeatherMap

---

### 🔧 Installation

```bash
pip install matplotlib
