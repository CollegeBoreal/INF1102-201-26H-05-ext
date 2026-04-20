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
<img width="876" height="238" alt="Capture d&#39;écran 2026-04-02 145312" src="https://github.com/user-attachments/assets/7dd34348-d2c7-4866-90ef-e2ef43dcccf5" />

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


<img width="1110" height="1012" alt="Capture d&#39;écran 2026-04-02 135735" src="https://github.com/user-attachments/assets/e1433620-d644-43f1-8232-ec518aac67fb" />



Le script Python :

- Charge les données depuis `data/meteo.json`
- Extrait :
  - 🌡️ Température (°C)
  - 💧 Humidité (%)
  - 📍 Ville
- Génère :
  - 📊 Graphique (`output/meteo.png`)

 <img width="640" height="480" alt="meteo" src="https://github.com/user-attachments/assets/8a1f8aae-c983-40a2-a5f6-7fb32dd4c523" />

  - 
  - 📄 Rapport (`output/rapport.txt`)

---

## 📊 Exemple de sortie

### 📄 rapport.txt

---

<img width="1033" height="628" alt="Capture d&#39;écran 2026-04-02 142055" src="https://github.com/user-attachments/assets/61495b5f-8bff-46e6-bff8-dd25b1e385c4" />

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

## 🚀 Utilisation

### Prérequis

- Python 3 avec `matplotlib` installé
- `curl` disponible sur le système
- Une clé API valide sur [OpenWeatherMap](https://openweathermap.org/api)

### Rendre le script exécutable


<img width="1046" height="457" alt="Capture d&#39;écran 2026-04-02 140058" src="https://github.com/user-attachments/assets/5612b095-73da-48f2-8a91-ad58da370fe8" />



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

<img width="1105" height="1076" alt="Capture d&#39;écran 2026-04-02 144927" src="https://github.com/user-attachments/assets/89acff32-d532-43e6-b39a-6f88a7cbf483" />




## 🛠️ Technologies utilisées

| Outil | Rôle |
|---|---|
| Bash | Orchestration du pipeline |
| Python 3 | Analyse des données |
| Matplotlib | Génération du graphique |
| curl | Appel à l'API REST |
| cron | Automatisation planifiée |
| OpenWeatherMap API | Source des données météo |

