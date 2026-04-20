# 🧾 7.REGEX – Analyse des logs Nginx

## 🎯 Objectif  
Ce travail consiste à analyser les logs Nginx en utilisant des expressions régulières (Regex) avec PowerShell et Python.

---

## ⚙️ Scripts utilisés  

Deux scripts ont été développés :

### 🔹 PowerShell
- `analyse_nginx.ps1`

### 🔹 Python
- `analyse_nginx.py`

Ces scripts permettent de :

- analyser le fichier `/var/log/nginx/access.log`  
- calculer le nombre total de requêtes  
- identifier les erreurs HTTP (4xx, 5xx)  
- compter les erreurs 404 et 500  
- afficher les 5 IP les plus actives  
- afficher les 5 pages les plus demandées  

---

## 🚀 Exécution des scripts  

### PowerShell
```bash
pwsh analyse_nginx.ps1
```

### Python
```bash
python3 analyse_nginx.py
```

---

## 📸 Capture d’exécution  

![Execution](images/1.png)

👉 Cette capture montre :
- l’exécution des scripts PowerShell et Python  
- la génération des rapports  
- le bon fonctionnement des Regex  

---

## 📂 Fichiers générés  

Après exécution :

- `rapport_nginx_ps1_YYYY-MM-DD.txt`  
- `rapport_nginx_py_YYYY-MM-DD.txt`  

Ces fichiers contiennent :
- statistiques globales  
- erreurs HTTP  
- top IP  
- top pages  

---

## 🔍 Vérification  

```bash
cat rapport_nginx_ps1_*.txt
cat rapport_nginx_py_*.txt
```

---

## 🧠 Conclusion  

Ce travail nous a permis de :

- utiliser les expressions régulières (Regex)  
- analyser des logs web réels  
- automatiser l’analyse avec PowerShell et Python  
- extraire des informations utiles à partir de données texte  

👉 Les Regex sont essentielles pour le traitement et l’analyse de logs en cybersécurité et DevOps.
