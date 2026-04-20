#  🌦️ PROJET_METEO

Pipeline automatisé de collecte et d'analyse de données météorologiques via l'API OpenWeatherMap.

---

##    Structure du projet

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

<img width="876" height="238" alt="Capture d&#39;écran 2026-04-02 145312" src="https://github.com/user-attachments/assets/7dd34348-d2c7-4866-90ef-e2ef43dcccf5" />







##  Fonctionnement

### 1. `analyse.sh` — Pipeline principal

Le script Bash orchestre l'ensemble du pipeline :

1. Définit les chemins du projet dynamiquement (`dirname`)
2. Crée les dossiers `data/` et `output/` si absents
3. Appelle l'API OpenWeatherMap pour la ville de **Toronto, CA** via `curl`
4. Vérifie que les données ont bien été récupérées
5. Lance le script Python `analyse.py`
6. Affiche un message de succès ou d'erreur à chaque étape

### 2. `analyse.py` — Analyse et génération des sorties



<img width="1110" height="1012" alt="Capture d&#39;écran 2026-04-02 135735" src="https://github.com/user-attachments/assets/e1433620-d644-43f1-8232-ec518aac67fb" />


Le script Python :

- Charge les données météo depuis `data/meteo.json`
- Extrait la **température** (°C), l'**humidité** (%) et le **nom de la ville**
- Génère un **graphique à barres** (`output/meteo.png`) avec Matplotlib
- Produit un **rapport texte** (`output/rapport.txt`)

---

##    Exemple de sortie

### `rapport.txt`


<img width="1033" height="628" alt="Capture d&#39;écran 2026-04-02 142055" src="https://github.com/user-attachments/assets/61495b5f-8bff-46e6-bff8-dd25b1e385c4" />



```

=== RAPPORT METEO ===

Ville: Toronto
Température: 1.94 °C
Humidité: 93 %
```

### `meteo.png`

Graphique à barres affichant la température et l'humidité pour Toronto.

---

##    Utilisation

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

##    Automatisation avec Cron

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




##  Technologies utilisées

| Outil | Rôle |
|---|---|
| Bash | Orchestration du pipeline |
| Python 3 | Analyse des données |
| Matplotlib | Génération du graphique |
| curl | Appel à l'API REST |
| cron | Automatisation planifiée |
| OpenWeatherMap API | Source des données météo |
>>>>>>> 94166bc7c6d4ac73240397c80ab15b055cf51ecb
