# 📡 Projet : Surveillance de site web

## 👤 Informations

**Nom : Syphax Ouadfel**
**ID étudiant : 300151233**

---

## 🎯 Objectif

Ce projet a pour but de vérifier la disponibilité de plusieurs sites web et de mesurer leur temps de réponse à l’aide d’un script Python exécuté depuis PowerShell.

---

## 🛠️ Technologies utilisées

* Python 3
* Module `requests`
* PowerShell
* (Optionnel) Jupyter Notebook

---

## 📁 Structure du projet

```id="7lffxg"
ton_projet/
│
├── scripts/
│   └── analyse.py        # Script principal Python
│
├── output/
│   └── rapport.txt       # Rapport généré automatiquement
│
├── RAPPORT.ipynb         # Analyse et explications
└── README.md             # Documentation du projet
```

---

## ⚙️ Fonctionnement

Le script Python :

* envoie une requête HTTP à plusieurs sites web
* récupère le code HTTP (200, 404, etc.)
* mesure le temps de réponse
* affiche les résultats
* génère un fichier `rapport.txt`

---

## ▶️ Exécution du projet

### 1. Installer la dépendance

```id="l8yfjv"
py -m pip install requests
```

### 2. Lancer le script

Depuis le dossier `scripts` :

```id="pkc1vk"
py analyse.py
```

### 3. Générer le rapport

```id="r8a2d0"
py analyse.py > ../output/rapport.txt
```

---

## 📊 Exemple de résultat

```id="rkwpd8"
===== RAPPORT DE SURVEILLANCE =====
Date: 2026-04-03
URL: https://google.com
Code HTTP: 200
Statut: OK
Temps: 0.5 secondes
```

---

## 📈 Analyse (Notebook)

Le fichier `RAPPORT.ipynb` contient :

* une description du projet
* la méthode utilisée
* des tests supplémentaires
* une analyse des résultats

---

## ✅ Résultat attendu

* Vérification de la disponibilité des sites
* Mesure des performances (temps de réponse)
* Génération automatique d’un rapport

---

## 💡 Améliorations possibles

* Ajouter plus de sites à surveiller
* Générer des graphiques (matplotlib)
* Automatiser l’exécution (cron / tâche planifiée)
