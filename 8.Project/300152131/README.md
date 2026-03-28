# 🪙 Crypto ETL — Pipeline Bitcoin avec CoinGecko API by #Calvin 

> Pipeline ETL automatisé en Bash + Python qui extrait le prix du Bitcoin en temps réel via l'API CoinGecko, le transforme, l'historise dans un CSV, génère un rapport texte et un graphique d'évolution — le tout automatisé avec CRON.

---

## 📋 Table des matières

- [Aperçu du projet](#-aperçu-du-projet)
- [Structure du projet](#-structure-du-projet)
- [Technologies utilisées](#-technologies-utilisées)
- [Phase 1 — Préparation](#phase-1--préparation-du-projet)
- [Phase 2 — Clé API CoinGecko](#phase-2--création--sécurisation-de-la-clé-api)
- [Phase 3 — Script Extract Bash](#phase-3--script-extract-bash)
- [Phase 4 — Script Transform + Load Python](#phase-4--script-transform--load-python)
- [Phase 5 — Test manuel](#phase-5--test-manuel)
- [Phase 6 — Automatisation CRON](#phase-6--automatisation-avec-cron)

---

## 🔍 Aperçu du projet

Ce projet implémente un pipeline **ETL complet** (Extract → Transform → Load) pour collecter et analyser l'évolution du prix du Bitcoin.

```
CoinGecko API
      │
      ▼
[EXTRACT — Bash]        → Appel API + récupération JSON brut
      │
      ▼
[TRANSFORM — Python]    → Parsing JSON + ajout timestamp + nettoyage
      │
      ▼
[LOAD — Python]         → Sauvegarde CSV + rapport texte + graphique PNG
      │
      ▼
[AUTOMATE — CRON]       → Exécution automatique toutes les heures
```

---

## 📁 Structure du projet

```
crypto-etl/
├── scripts/
│   ├── extract.sh            # Script Bash — appel API CoinGecko
│   └── transform_load.py     # Script Python — transformation + chargement
├── data/
│   ├── raw.json              # Données brutes reçues de l'API (généré)
│   └── historique.csv        # Historique des prix horodatés (généré)
├── output/
│   ├── report.txt            # Rapport texte avec stats (généré)
│   └── graph.png             # Graphique d'évolution du prix (généré)
├── logs/
│   └── run.log               # Journal d'exécution (généré)
├── images/                   # Captures d'écran de la démonstration
└── README.md
```

> 📌 Les dossiers `data/`, `output/` et `logs/` sont générés automatiquement à l'exécution. Leurs contenus ne sont pas versionnés (voir `.gitignore`).

---

## 🛠️ Technologies utilisées

| Outil | Rôle |
|---|---|
| **Bash** | Script d'extraction — appel API via `curl` |
| **Python 3** | Transformation, chargement, visualisation |
| **pandas** | Manipulation et sauvegarde du CSV historique |
| **matplotlib** | Génération du graphique d'évolution |
| **CoinGecko API** | Source de données — prix Bitcoin en USD |
| **CRON** | Automatisation de l'exécution toutes les heures |
| **Linux (Ubuntu)** | Environnement d'exécution |

---

## Phase 1 — Préparation du projet

Création de l'arborescence complète du projet en une seule commande :

```bash
mkdir -p ~/crypto-etl/{scripts,data,output,logs}
```

Vérification de la structure créée :

```bash
ls ~/crypto-etl
```

Résultat attendu :

```
data  logs  output  scripts
```

---

## Phase 2 — Création & Sécurisation de la clé API

La clé API CoinGecko est stockée dans un fichier `.env` caché dans le HOME, **jamais versionnée sur GitHub**.

### Étape 1 — Créer le fichier `.env` avec la clé API

```bash
nano ~/.crypto_api.env
```

Contenu à ajouter :

```
COINGECKO_API_KEY="TA_CLE_ICI"
```

Enregistrer : `CTRL+O` → `ENTER` → `CTRL+X`

![Création du fichier .env avec la clé API](images/1%20creation%20du%20fichier%20env%20avec%20cle%20api%20.png)

---

### Étape 2 — Charger la clé automatiquement dans le shell

```bash
nano ~/.bashrc
```

Ajouter à la fin du fichier :

```bash
export COINGECKO_API_KEY=$(grep COINGECKO_API_KEY ~/.crypto_api.env | cut -d '=' -f2 | tr -d '"')
```

![Ajout de la clé API dans .bashrc](images/2%20ajout%20cle%20api%20dans%20.bashrc.png)

---

### Étape 3 — Recharger le shell et vérifier

```bash
source ~/.bashrc
echo $COINGECKO_API_KEY
```

✅ Si la clé s'affiche dans le terminal → la configuration est correcte.

![Rechargement du shell et vérification de la clé](images/3%20recharge%20du%20shell.png)

> 🔒 **Sécurité** : ajoute `*.env` à ton `.gitignore` pour ne jamais exposer ta clé sur GitHub.

---

## Phase 3 — Script Extract (Bash)

### Créer et éditer le fichier

```bash
nano ~/crypto-etl/scripts/extract.sh
```

### Contenu du script

```bash
#!/bin/bash
set -e  # Arrêt immédiat en cas d'erreur

API_KEY=$COINGECKO_API_KEY
RAW_FILE="../data/raw.json"
LOG_FILE="../logs/run.log"

echo "[INFO] $(date) — Début EXTRACT" >> $LOG_FILE

curl -s -H "x-cg-demo-api-key: $API_KEY" \
  "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd" \
  > $RAW_FILE

echo "[INFO] $(date) — Données API reçues" >> $LOG_FILE

python3 ../scripts/transform_load.py $RAW_FILE

echo "[INFO] $(date) — EXTRACT terminé" >> $LOG_FILE
```

**Ce que fait ce script :**
- Appelle l'API CoinGecko avec la clé d'authentification
- Sauvegarde la réponse JSON brute dans `data/raw.json`
- Lance automatiquement le script Python de transformation
- Journalise chaque étape dans `logs/run.log`

![Script extract.sh dans l'éditeur nano](images/4%20scrips%20extract.png)

---

### Rendre le script exécutable

```bash
chmod +x ~/crypto-etl/scripts/extract.sh
ls -l ~/crypto-etl/scripts
```

![Script rendu exécutable avec chmod +x](images/5%20rendu%20du%20fichier%20executable.png)

---

## Phase 4 — Script Transform + Load (Python)

### Créer et éditer le fichier

```bash
nano ~/crypto-etl/scripts/transform_load.py
```

### Contenu du script

```python
import sys, json, pandas as pd, matplotlib.pyplot as plt
from datetime import datetime

# Lecture du fichier JSON brut
raw_file = sys.argv[1]
with open(raw_file) as f:
    data = json.load(f)

# TRANSFORM — Extraction du prix et horodatage
price = data["bitcoin"]["usd"]
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# LOAD — Ajout au CSV historique
csv_path = "../data/historique.csv"
try:
    df = pd.read_csv(csv_path)
except FileNotFoundError:
    df = pd.DataFrame(columns=["timestamp", "price"])

df.loc[len(df)] = [timestamp, price]
df.to_csv(csv_path, index=False)

# Génération du rapport texte
with open("../output/report.txt", "w") as f:
    f.write("=== Rapport Bitcoin ===\n")
    f.write(f"Date : {timestamp}\n")
    f.write(f"Prix actuel : {price} USD\n")
    f.write(f"Min historique : {df['price'].min()}\n")
    f.write(f"Max historique : {df['price'].max()}\n")

# Génération du graphique
plt.figure(figsize=(10, 5))
plt.plot(df["timestamp"], df["price"], marker="o")
plt.xticks(rotation=45)
plt.title("Évolution du prix du Bitcoin")
plt.ylabel("Prix (USD)")
plt.grid()
plt.tight_layout()
plt.savefig("../output/graph.png")

print("ETL terminé.")
```

**Ce que fait ce script :**
- **Extract** : lit le JSON brut passé en argument par `extract.sh`
- **Transform** : extrait le prix Bitcoin et ajoute un timestamp précis
- **Load** : sauvegarde dans le CSV cumulatif, génère le rapport `.txt` et le graphique `.png`

![Script transform_load.py dans l'éditeur nano](images/6%20script%20transform%20load.png)

---

## Phase 5 — Test manuel

### Lancer le pipeline ETL

```bash
cd ~/crypto-etl/scripts
./extract.sh
```

✅ Message de confirmation attendu dans le terminal :

```
ETL terminé.
```

![Exécution manuelle du pipeline — ETL terminé](images/7%20execution%20manuel%20du%20script_ETL%20Termine.png)

---

### Vérification du fichier JSON brut (`data/raw.json`)

```bash
cat ~/crypto-etl/data/raw.json
```

Contenu attendu :

```json
{"bitcoin":{"usd":84250.0}}
```

![Contenu du fichier raw.json après la première exécution](images/8%20fichier%20json%20apres%20premiere%20execution.png)

---

### Vérification du fichier CSV historique (`data/historique.csv`)

```bash
cat ~/crypto-etl/data/historique.csv
```

Contenu attendu :

```
timestamp,price
2025-03-27 15:10:22,84250.0
```

![Fichier historique.csv avec les données horodatées](images/9%20historique.png)

---

### Premier graphique généré (`output/graph.png`)

Le graphique est généré automatiquement dans `output/graph.png` à chaque exécution.

![Premier graphique d'évolution du prix Bitcoin](images/11%20photo%20du%20premier%20graph%20png.png)

---

### Journal d'exécution (`logs/run.log`)

```bash
cat ~/crypto-etl/logs/run.log
```

Contenu attendu :

```
[INFO] Thu Mar 27 15:10:20 2025 — Début EXTRACT
[INFO] Thu Mar 27 15:10:21 2025 — Données API reçues
[INFO] Thu Mar 27 15:10:22 2025 — EXTRACT terminé
```

![Journal d'exécution run.log](images/12%20premier%20log.png)

---

### Récapitulatif des fichiers générés

| Fichier | Contenu |
|---|---|
| `data/raw.json` | Réponse brute de l'API CoinGecko |
| `data/historique.csv` | Tableau cumulatif `timestamp` + `price` |
| `output/report.txt` | Prix actuel, min et max historiques |
| `output/graph.png` | Courbe d'évolution du prix Bitcoin |
| `logs/run.log` | Journaux horodatés de chaque exécution |

---

## Phase 6 — Automatisation avec CRON

### Ouvrir le crontab

```bash
crontab -e
```

### Ajouter la règle d'exécution toutes les heures

```
0 * * * * /bin/bash /home/ubuntu/crypto-etl/scripts/extract.sh
```


![Configuration de la tâche CRON pour l'automatisation](images/13%20automatisation%20avec%20cron.png)

---

### Vérifier que le service CRON est actif

```bash
systemctl status cron
```

### Résultat après automatisation — graphique enrichi

Après plusieurs exécutions automatiques, le graphique accumule les points de données et montre l'évolution réelle du prix Bitcoin dans le temps.

![Graphique d'évolution après plusieurs exécutions CRON automatiques](images/14%20graphe%20apres%20automatisation.png)

### Ensuite
![Graphique d'évolution après plusieurs exécutions CRON automatiques](images/15%20graphe%20suite.png) 

### Suite pour execution chaque 2 min 
![Graphique d'évolution après plusieurs exécutions CRON automatiques](images/16%20graphe.png) 

---

## 🔒 Sécurité & Bonnes pratiques

Créer un fichier `.gitignore` à la racine du projet :

```gitignore
# Clé API — ne jamais versionner
*.env
.crypto_api.env

# Données générées automatiquement
data/
output/
logs/
```

---

## 👤 Auteur  Calvin #300152131

Projet réalisé dans le cadre d'un exercice pratique ETL sur Linux.

---

## 📄 Licence 

Ce projet est open-source et libre d'utilisation à des fins éducatives.