Mohammed Aiche  
Numéro étudiant : 300151608  

Projet réalisé dans le cadre du cours INF1102.


<img width="960" height="1020" alt="nigx" src="https://github.com/user-attachments/assets/bc9d3c8b-25c3-43cf-8dad-1e84109459b7" />


Analyse des logs Nginx avec Regex

## 📌 Description du projet

Ce projet a pour objectif d’analyser les fichiers de logs Nginx en utilisant des expressions régulières (Regex) et de générer automatiquement des rapports.

Il permet de mieux comprendre l’activité d’un serveur web et d’identifier les erreurs ou les comportements importants.

## 🎯 Fonctionnalités

✔ Analyse des requêtes HTTP  
✔ Détection des erreurs (4xx, 5xx)  
✔ Identification des adresses IP les plus actives  
✔ Analyse des pages les plus consultées  
✔ Génération automatique de rapports  

---

## 📊 Exemple de résultat

Rapport Nginx – 2026-04-13  
----------------------------------  
Total des requêtes : 1500  
Erreurs HTTP : 120  
Erreurs 404 : 80  
Erreurs 500 : 40  

Top IP :  
120 → 192.168.1.1  
95 → 10.0.0.5  

Top pages :  
300 → /index.html  
210 → /login  

---

## 📂 Structure du projet

<img width="960" height="1020" alt="nigx2" src="https://github.com/user-attachments/assets/7fe38e35-6066-4c1a-81b3-6928bb42ce35" />


7.REGEX/300151608/
├── analyse_nginx.ps1
├── analyse_nginx.py
├── rapport_*.txt
├── images/
└── README.md


---

## 📥 Données d’entrée

Fichier analysé :


/var/log/nginx/access.log


Exemple de ligne :


192.168.1.10 - - [17/Mar/2026:14:32:10 +0000] "GET /index.html HTTP/1.1" 200 1024


---

## 📤 Résultats

Les scripts génèrent automatiquement des rapports :

- rapport_nginx_ps1_YYYY-MM-DD.txt  
- rapport_nginx_py_YYYY-MM-DD.txt  

---

## 🔍 Expressions régulières utilisées

| Élément | Regex |
|--------|------|
| Adresse IP | (\d{1,3}\.){3}\d{1,3} |
| Code HTTP | " (\d{3}) |
| Pages GET | "GET ([^ ]+) |
| Erreurs | " (4\|5)\d{2} |

---

## ⚙️ Installation

### Prérequis

- Python 3  
- PowerShell Core (pwsh)  
- Linux / Windows / WSL  

---

## ▶️ Utilisation

### PowerShell


pwsh analyse_nginx.ps1


### Python


python3 analyse_nginx.py


---

## 📊 Résumé des résultats

Chaque rapport contient :

- Nombre total des requêtes  
- Nombre d’erreurs HTTP  
- Erreurs 404 et 500  
- Top 5 des IP  
- Top 5 des pages  

---

## ⏰ Automatisation (optionnel)

Avec cron sous Linux :


crontab -e

0 2 * * * /usr/bin/pwsh /home/user/analyse_nginx.ps1


---

## 🛠️ Technologies utilisées

- Python  
- PowerShell  
- Regex  
- Linux  

---

---

## ✅ Conclusion

Ce projet permet d’automatiser l’analyse des logs Nginx et de générer des rapports utiles pour la surveillance d’un serveur.  
Il montre l’utilisation des Regex ainsi que l’intégration de Python et PowerShell dans un contexte DevOps.
