# 🚀 Projets INF1102 — Ismail Trache (300150395)


# INF1102 — Projet Scrapy News — Ismail Trache (300150395)

## 1. Objectif

Ce projet utilise le framework **Scrapy** pour scraper des citations sur le site de démonstration `https://quotes.toscrape.com`, puis analyse les mots les plus fréquents avec un script **Python**.  
Le projet génère automatiquement :
- un fichier **JSONL** `articles.jsonl` avec les données brutes,
- un **rapport texte** `rapport.txt`,
- une **figure** `top_words.png`,
- un **rapport Jupyter** `RAPPORT.ipynb` avec visualisations et commentaires.

## 2. Structure du projet

À la racine de `8.Project/300150395` :

- `news_spider.py` : spider Scrapy (collecte des données)
- `analyse.py` : script Python d’analyse (statistiques + figure)
- `analyse.ps1` : script principal (Scrapy + analyse)
- `articles.jsonl` : données scrapées (généré automatiquement)
- `rapport.txt` : rapport texte (généré automatiquement)
- `top_words.png` : graphique des mots fréquents (généré automatiquement)
- `RAPPORT.ipynb` : rapport Jupyter (analyses + graphiques)
- `requirements.txt` : dépendances Python (scrapy, matplotlib, …)
- `images/` : captures d’écran (exécution, Notebook, etc.)

## 3. Installation

```bash
cd INF1102-201-26H-05/8.Project/300150395
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 4. Exécution

### 4.1 Script principal

```bash
pwsh ./analyse.ps1
```

ou étape par étape :

```bash
scrapy runspider news_spider.py -O articles.jsonl
python analyse.py articles.jsonl
```

### 4.2 Rapport Jupyter

Ouvrir le fichier `RAPPORT.ipynb` avec **Jupyter Notebook** ou **Jupyter Lab** pour consulter les graphiques et l’analyse écrite.

## 5. Résultats obtenus (exemple)

Après exécution :

- `Nombre d’éléments scrapés` : 100
- Top 10 des mots les plus fréquents :
  - you : 103
  - not : 36
  - that : 31
  - but : 26
  - love : 23
  - can : 21
  - your : 18
  - who : 18
  - will : 18
  - have : 17

## 6. Bonnes pratiques

- Scripts lisibles et commentés.
- Respect de la structure de fichiers demandée dans le cours.
- Rapport Jupyter avec texte explicatif + figures.
- Captures d’écran dans `images/` (exécution, contenu de `rapport.txt`, Notebook, etc.).























**Environnement :** Ubuntu 22.04 LTS | **Cours :** INF1102

---

## 📋 Sommaire

| Projet | Description |
|--------|-------------|
| [Projet 5 — Monitoring Web](#projet-5--monitoring-de-sites-web) | Vérifie la disponibilité de sites web et mesure le temps de réponse |
| [Projet Gobuster — VM Scanner](#projet-gobuster--vm-scanner) | Scanner automatique des VMs Proxmox avec Gobuster |

---

# Projet 5 — Monitoring de sites web

## 1. Objectif
Ce projet vérifie la **disponibilité de plusieurs sites web** et mesure leur **temps de réponse** via Bash + Python.

Il génère automatiquement :
- un fichier log (`data/sample.log`)
- un rapport texte (`output/rapport.txt`)
- une analyse statistique complète via Python

## 2. Structure
```plaintext
projet5-monitoring/
├── scripts/
│   ├── analyse.sh       # Script Bash principal
│   └── analyse.py       # Script Python appelé par Bash
├── data/
│   └── sample.log       # Log généré automatiquement
├── output/
│   └── rapport.txt      # Rapport généré automatiquement
└── RAPPORT.ipynb        # Rapport Jupyter avec analyse et graphique
```

## 3. Sites testés
- `https://google.com`
- `https://github.com`
- `https://collegeboreal.ca`
- `https://example.com`
- `https://httpstat.us/404`

## 4. Exécution
```bash
bash projet5-monitoring/scripts/analyse.sh
```

![Script analyse.sh](images/1.png)
![Script analyse.py](images/2.png)
![Exécution](images/3.png)

## 5. Résultats obtenus
```
===== RAPPORT MONITORING =====
Date : 2026-03-27 03:22:34

2026-03-27 03:22:34 | https://google.com       | 301 | 339ms  | ✅ OK
2026-03-27 03:22:34 | https://github.com       | 200 | 489ms  | ✅ OK
2026-03-27 03:22:34 | https://collegeboreal.ca | 200 | 218ms  | ✅ OK
2026-03-27 03:22:34 | https://example.com      | 200 | 190ms  | ✅ OK
2026-03-27 03:22:34 | https://httpstat.us/404  | 000 | 236ms  | ❌ ERREUR

===== ANALYSE PYTHON =====
Total sites vérifiés : 5
Sites OK (200)       : 3
Sites en erreur      : 2
Temps moyen          : 294.4 ms
Temps le plus rapide : 190 ms
Temps le plus lent   : 489 ms
```

![Rapport](images/4.png)

## 6. Codes HTTP

| Code | Signification |
|------|---------------|
| `200` | Site accessible ✅ |
| `301` | Redirection permanente (normal) |
| `000` | Timeout / bloqué depuis la VM |

## 7. Cron
```bash
0 * * * * bash /home/ubuntu/INF1102-201-26H-05/8.Project/300150395/projet5-monitoring/scripts/analyse.sh
```

---

# Projet Gobuster — VM Scanner

## 1. Objectif
Scanner automatiquement les VMs du réseau Proxmox (`10.7.237.224-245`) avec **Gobuster** pour détecter les serveurs web exposés et les fichiers accessibles.

## 2. Structure
```plaintext
projet-gobuster/
├── scripts/
│   ├── gobuster_all_vms.sh      # Script principal v2
│   └── gobuster_all_vms_v1.sh  # Version 1
├── data/
│   └── sample.log               # Rapport de scan réel
└── output/
    └── rapport.txt              # Résumé généré
```

## 3. Exécution
```bash
bash projet-gobuster/scripts/gobuster_all_vms.sh
```

![Scan Gobuster](images/5.png)
![Résultats](images/6.png)
![Rapport Gobuster](images/7.png)

## 4. Résultats obtenus

| IP | Statut | Fichiers trouvés |
|----|--------|-----------------|
| 10.7.237.226 | ✅ SCAN | index.html (200) |
| 10.7.237.229 | ✅ SCAN | index.html (200) |
| 10.7.237.230 | ✅ SCAN | index.html (200) |
| 10.7.237.233 | ✅ SCAN | index.html, script.js (200) |
| 10.7.237.234 | ✅ SCAN | index.html (200) |
| 10.7.237.236 | ✅ SCAN | index.html (200) |
| 10.7.237.237 | ✅ SCAN | (aucun résultat) |
| 10.7.237.238 | ✅ SCAN | index.html (200) |
| 10.7.237.240 | ✅ SCAN | index.html (200) |
| 10.7.237.242 | ✅ SCAN | index.html (200) |
| 10.7.237.224/225/227/228... | ❌ SKIP | Pas de réponse HTTP |

## 5. Configuration du scan
- **Réseau :** `10.7.237.224` → `10.7.237.245`
- **Wordlist :** `raft-medium-directories.txt`
- **Extensions :** `html, php, txt, js, json, xml, bak, old`
- **Threads :** 20
- **Timeout :** 5s

---

# 📚 Références Bash

## Gestion fichiers
| Commande | Rôle |
|----------|------|
| `mkdir -p` | Créer dossier (et parents) |
| `cp -r` | Copier récursivement |
| `tar -czvf` | Créer archive compressée |

## Réseau & Scan
| Commande | Rôle |
|----------|------|
| `ping -c 4` | Tester connectivité |
| `curl --max-time` | Tester HTTP avec timeout |
| `gobuster dir` | Scanner répertoires web |

## Planification
| Commande | Rôle |
|----------|------|
| `crontab -e` | Modifier tâches planifiées |
| `systemctl status cron` | Vérifier service cron |

## Journalisation
| Élément | Rôle |
|---------|------|
| `>>` | Ajouter dans un fichier log |
| `2>&1` | Rediriger erreurs vers log |
| `date` | Inscrire horodatage |
