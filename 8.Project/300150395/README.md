
### Description des fichiers clés

| Fichier | Type | Description |
|---------|------|-------------|
| `scripts/analyse.ps1` | PowerShell | **Script principal** — orchestre tout le pipeline (scraping → analyse → rapport) |
| `scripts/analyse.py` | Python | Charge les données JSONL, analyse statistique, génère figures PNG |
| `scripts/news_spider.py` | Python/Scrapy | Spider Scrapy — extrait les citations de quotes.toscrape.com |
| `data/articles.jsonl` | JSONL | Données brutes (généré automatiquement) — 100 citations au format JSON Lines |
| `output/rapport.txt` | Texte | Rapport formaté avec top 10 mots et statistiques (généré) |
| `output/top_words.png` | PNG | Histogramme matplotlib — top 10 des mots (généré) |
| `output/wordcloud.png` | PNG | Wordcloud — visualisation nuage de mots (généré) |
| `RAPPORT.ipynb` | Jupyter | Notebook complet : code, outputs, texte explicatif, figures intégrées |

---

## ✅ Bonnes pratiques implémentées

| Pratique | Statut | Détails |
|----------|--------|---------|
| **Structure claire** | ✅ | Dossiers `scripts/`, `data/`, `output/`, séparation des responsabilités |
| **Automatisation** | ✅ | Script PowerShell qui orchestre tout le pipeline |
| **Données générées** | ✅ | Pas de fichiers "magiques" — tout est produit par les scripts |
| **Documentation** | ✅ | README complet, comments dans le code, rapport Jupyter |
| **Rapports visuels** | ✅ | Histogramme + Wordcloud + rapport texte formaté |
| **User-Agent réaliste** | ✅ | Scrapy configuré avec User-Agent authentique |
| **Gestion des erreurs** | ✅ | Try/catch dans les scripts Python |
| **Virtualenv** | ✅ | Environnement isolé avec `venv/` |

---

## 🌐 Projets complémentaires

### Projet 5 — Monitoring de sites web
**Emplacement** : `autres-projets/projet5-monitoring/`

**Objectif** : Vérifier la disponibilité de plusieurs sites web et mesurer les temps de réponse.

**Exécution** :
```bash
bash autres-projets/projet5-monitoring/scripts/analyse.sh
```

**Livrables** :
- `data/sample.log` — Logs de monitoring
- `output/rapport.txt` — Rapport de disponibilité
- `RAPPORT.ipynb` — Analyse Jupyter

---

### Projet Gobuster — VM Scanner
**Emplacement** : `autres-projets/projet-gobuster/`

**Objectif** : Scanner les VMs du réseau Proxmox (`10.7.237.224-245`) pour détecter serveurs web et fichiers accessibles.

**Exécution** :
```bash
bash autres-projets/projet-gobuster/scripts/gobuster_all_vms.sh
```

**Livrables** :
- `data/sample.log` — Résultats du scan
- `output/rapport.txt` — Résumé des IP scannées et pages trouvées
- `RAPPORT.ipynb` — Analyse détaillée

---

## 📝 Fichiers importants

### `requirements.txt`
```txt
scrapy>=2.8.0
matplotlib>=3.7.0
numpy>=1.24.0
wordcloud>=1.9.0
pillow>=9.0.0
notebook>=6.5.0
pandas>=1.5.0
requests>=2.28.0
```

### `scripts/analyse.ps1` (aperçu)
```powershell
# Scraping avec Scrapy
scrapy runspider scripts/news_spider.py -O data/articles.jsonl

# Analyse et visualisation
python scripts/analyse.py data/articles.jsonl

# Génération du notebook (optionnel)
python scripts/create_rapport.py
```

---

## 🎓 Ce que le projet démontre

✨ **Compétences acquises** :
- Scraping web avec **Scrapy** (framework professionnel)
- Traitement et analyse de texte avec **Python**
- Visualisation de données avec **Matplotlib** et **Wordcloud**
- Génération de rapports programmés
- Automatisation avec **PowerShell** et **Bash**
- Documentation technique complète

---

## 📞 Support

Pour questions ou problèmes :
1. Vérifier que toutes les dépendances sont installées : `pip list`
2. S'assurer que l'environnement virtuel est activé
3. Vérifier la connexion Internet (scraping en ligne)
4. Consulter les logs en cas d'erreur Scrapy

---

## 📄 Licence & Crédits

**Projet académique** — INF1102 Programmation système, Université du Québec à Montréal (UQAM)

**Données** : [Quotes to Scrape](https://quotes.toscrape.com) — site officiel d'entraînement au web scraping

**Auteur** : Ismail Trache (300150395)

**Date** : 2026-04-10 ⌛ 23h03

---

<div align="center">

**✨ Merci d'avoir consulté ce projet ! ✨**

</div>
