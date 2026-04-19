# 📽️ Projet Monitoring Web — INF1102

<div align="center">

![PowerShell](https://img.shields.io/badge/PowerShell-5391FE?style=for-the-badge&logo=powershell&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Status](https://img.shields.io/badge/Status-Complété-brightgreen?style=for-the-badge)

</div>

---

## 👤 Informations étudiant

| Champ | Détails |
|-------|---------|
| **Nom** | Ouail Gacem |
| **Matricule** | 300148094 |
| **Cours** | INF1102 |
| **Établissement** | Collège Boréal |

---

## 🎯 Objectif

Ce projet consiste à développer un outil de **monitoring web automatisé** capable de :

- 🌐 Vérifier la **disponibilité** de plusieurs sites web
- ⏱️ Mesurer les **temps de réponse** de chaque site
- ⚠️ Détecter les **erreurs HTTP** éventuelles
- 📄 Générer un **rapport d'analyse automatisé** en format texte

---

## 📁 Structure du projet

```
8.Project/300148094/
│
├── scripts/
│   ├── analyse.ps1          # Script de monitoring PowerShell
│   └── analyse.py           # Script de monitoring Python
│
├── data/
│   └── sample.log           # Fichier de logs d'exemple
│
├── output/
│   └── rapport.txt          # Rapport généré automatiquement
│
└── README.md                # Ce fichier
```

---

## 🚀 Exécution

### 🟦 PowerShell

```bash
pwsh scripts/analyse.ps1
```

### 🐍 Python

```bash
python3 scripts/analyse.py
```

---

## 📊 Résultat

Les scripts génèrent le fichier suivant :

```
output/rapport.txt
```

Ce rapport contient :

- 📌 **Disponibilité des sites** — statut en ligne / hors ligne pour chaque URL
- ⏱️ **Temps de réponse** — durée mesurée en millisecondes pour chaque requête
- ⚠️ **Détection des erreurs** — codes HTTP anormaux (4xx, 5xx) identifiés et signalés

**Exemple de contenu du rapport :**

```
📊 Rapport Monitoring Web — 2026-02-05 02:00:00
--------------------------------------------------
https://www.google.com       ✅  200  112ms
https://www.github.com       ✅  200  245ms
https://www.example.com      ✅  200  189ms
https://www.site-down.com    ❌  503  timeout
--------------------------------------------------
Sites vérifiés  : 4
Sites en ligne  : 3
Sites en erreur : 1
Temps moyen     : 182ms
```

---

## ✅ Réalisations

| Étape | Statut |
|-------|--------|
| Script PowerShell | ✅ Complété |
| Script Python | ✅ Complété |
| Rapport TXT généré | ✅ Complété |
| Structure du projet | ✅ Complété |

---

## 🛠️ Technologies utilisées

| Technologie | Usage |
|-------------|-------|
| 💻 **PowerShell (pwsh)** | Script de monitoring et génération du rapport |
| 🐍 **Python 3** | Script alternatif avec module `requests` / `re` |
| 🌐 **HTTP Monitoring** | Vérification de la disponibilité des URLs |
| 📄 **Traitement de logs** | Analyse du fichier `sample.log` avec regex |

---

## 💡 Améliorations possibles

- 📦 **Export JSON / CSV** — pour intégration avec d'autres outils
- 📧 **Ajout d'alertes** — notification par email si un site tombe
- 📈 **Dashboard Grafana** — visualisation graphique des métriques
- ⏰ **Monitoring en temps réel** — via cron ou boucle continue

---

## 👨‍💻 Auteur

**Ouail Gacem**  
Étudiant — Collège Boréal  
Cours INF1102 — Programmation système

---

<div align="center">

⭐ Si ce projet t'aide, laisse une étoile sur GitHub !

</div>
