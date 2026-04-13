# 📊 Nginx Log Analyzer

### 🔍 Analyse automatisée des logs Nginx avec Regex (PowerShell & Python)

![GitHub repo size](https://img.shields.io/github/repo-size/TON-USERNAME/nginx-log-analyzer)
![GitHub stars](https://img.shields.io/github/stars/TON-USERNAME/nginx-log-analyzer?style=social)
![GitHub last commit](https://img.shields.io/github/last-commit/TON-USERNAME/nginx-log-analyzer)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![PowerShell](https://img.shields.io/badge/PowerShell-Core-blue)

---

## 🎯 Objectif

Ce projet permet d’analyser les fichiers de logs **Nginx** à l’aide d’**expressions régulières (Regex)**, puis de générer automatiquement des rapports détaillés.

✔ Analyse des requêtes HTTP
✔ Détection des erreurs (4xx, 5xx)
✔ Identification des IP les plus actives
✔ Analyse des pages les plus visitées
✔ Automatisation possible (cron)

---

## 📸 Aperçu du rapport

```text
📊 Rapport Nginx - 2026-04-13
----------------------------------
Total requêtes : 1500
Erreurs HTTP : 120
Erreurs 404 : 80
Erreurs 500 : 40

Top 5 IP :
120 192.168.1.1
95 10.0.0.5

Top 5 pages :
300 /index.html
210 /login
```

---

## 📂 Structure du projet

```bash
nginx-log-analyzer/
├── REGEX/
│   ├── analyse_nginx.ps1
│   ├── analyse_nginx.py
│   └── rapport_*.txt
│
├── logs/
│   └── access.log
│
├── README.md
└── .gitignore
```

---

## 📥 Entrée

Fichier de logs Nginx :

```bash
/var/log/nginx/access.log
```

Exemple de ligne :

```text
192.168.1.10 - - [17/Mar/2026:14:32:10 +0000] "GET /index.html HTTP/1.1" 200 1024
```

---

## 📤 Sortie

Rapports générés automatiquement :

```bash
REGEX/rapport_nginx_ps1_YYYY-MM-DD.txt
REGEX/rapport_nginx_py_YYYY-MM-DD.txt
```

---

## 🧠 Regex utilisées

| Élément      | Expression régulière    |
| ------------ | ----------------------- |
| Adresse IP   | `(\d{1,3}\.){3}\d{1,3}` |
| Code HTTP    | `" (\d{3}) `            |
| Pages GET    | `"GET ([^ ]+)`          |
| Erreurs HTTP | `" (4\|5)\d{2} `        |

---

## ⚡ Installation

### 🔧 Prérequis

* Python 3.x
* PowerShell Core (`pwsh`)
* Linux / Windows / WSL

---

## ▶️ Utilisation

### 🟦 PowerShell

```bash
pwsh ./REGEX/analyse_nginx.ps1
```

### 🐍 Python

```bash
python3 REGEX/analyse_nginx.py
```

---

## 📊 Résultats générés

Chaque rapport contient :

* 📌 Total des requêtes
* ⚠️ Nombre d’erreurs HTTP
* ❌ Erreurs 404
* 💥 Erreurs 500
* 🌐 Top 5 IP
* 📄 Top 5 pages

---

## ⏰ Automatisation

### 🔁 Linux (cron)

```bash
crontab -e
```

```bash
0 2 * * * /usr/bin/pwsh /home/user/REGEX/analyse_nginx.ps1
```

---

## 🔍 Vérification

```bash
grep CRON /var/log/syslog
```

---

## 🚀 Roadmap

* [ ] Export CSV / JSON
* [ ] Graphiques (matplotlib)
* [ ] Interface Web (Flask / FastAPI)
* [ ] Analyse temps réel
* [ ] Détection d’attaques (DDoS, brute force)

---

## 🛠️ Technologies

* 🐍 Python 3
* 💻 PowerShell
* 🔍 Regex
* 🐧 Linux / Cron

---

## 🤝 Contribution

Les contributions sont les bienvenues !

1. Fork le projet
2. Crée une branche (`feature/ma-feature`)
3. Commit (`git commit -m "Ajout feature"`)
4. Push (`git push origin feature/ma-feature`)
5. Ouvre une Pull Request

---

## 📄 Licence

Ce projet est sous licence **MIT**.

---

## 👨‍💻 Auteur

Projet réalisé dans le cadre d’un TP en administration système & automatisation.

---

## ⭐ Support

Si ce projet t’aide, laisse une ⭐ sur GitHub !

---
