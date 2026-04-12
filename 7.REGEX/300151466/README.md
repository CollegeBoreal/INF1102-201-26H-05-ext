
# Expressions Régulières — Analyse des logs Nginx 📊

**Cours** : INF1102-201-26H-05  
**Étudiant** : adel bennacer 
**Matricule** : 300151466

---

## 📋 Description

Ce travail pratique consiste à analyser les logs du serveur web Nginx à l'aide d'expressions régulières (Regex), en utilisant deux langages de script : PowerShell et Python. Les scripts génèrent automatiquement un rapport détaillé contenant les statistiques des requêtes HTTP.

---

## 🖥️ 1. Connexion SSH à la VM

Connexion sécurisée à la machine virtuelle `vm300151466` via SSH à l'adresse `10.7.237.239`.
```bash
ssh -i ~/.ssh/ma_cle \
  -o StrictHostKeyChecking=no \
  -o UserKnownHostsFile=/tmp/ssh_known_hosts_empty \
  ubuntu@10.7.237.239
```
<img width="425" height="91" alt="c1" src="https://github.com/user-attachments/assets/9d5a07e4-582e-4245-b5da-e003f0c6ad44" />



---

## 📁 2. Structure du projet

Création de la structure de dossiers et vérification de la présence des logs Nginx.
```bash
mkdir -p ~/REGEX/images
ls /var/log/nginx/
```

<img width="269" height="61" alt="c2" src="https://github.com/user-attachments/assets/86c347a9-753f-46b8-981e-1bc82ad2dce0" />


---

## ⚡ 3. Scripts d'analyse

### Script PowerShell — `analyse_nginx.ps1`

Analyse le fichier `/var/log/nginx/access.log` à l'aide d'expressions régulières PowerShell et génère un rapport texte contenant :
- Le nombre total de requêtes
- Les erreurs HTTP (4xx et 5xx)
- Le top 5 des adresses IP
- Le top 5 des pages visitées

### Script Python — `analyse_nginx.py`

Même analyse réalisée avec le module `re` de Python et la classe `Counter` pour le classement des résultats.

<img width="326" height="259" alt="c3" src="https://github.com/user-attachments/assets/4c545733-0f76-4c18-8700-c78ac40be3b9" />


---

## 🚀 4. Déploiement sur GitHub

Envoi des fichiers sur le dépôt GitHub du cours via `git push`.
```bash
git add 7.REGEX/300151466/
git commit -m "Ajout scripts REGEX - 300151466"
git push
```


<img width="365" height="161" alt="c5" src="https://github.com/user-attachments/assets/08621de2-46de-461d-bda1-63fa456cdc6a" />

---

## 🧠 Expressions régulières utilisées

| Élément | Regex |
|---|---|
| Adresse IP | `(\d{1,3}\.){3}\d{1,3}` |
| Code HTTP | `" (\d{3}) "` |
| Page GET | `"GET ([^ ]+)` |
| Erreurs 4xx/5xx | `^[45]` |

---

## ✅ Résultat

Les deux scripts développés (PowerShell et Python) ont été exécutés avec succès.

Ils ont permis de générer automatiquement les rapports suivants :

rapport_nginx_ps1_2026-03-31.txt
rapport_nginx_py_2026-03-31.txt

Ces fichiers contiennent les adresses IP les plus fréquentes extraites des logs NGINX, ainsi que leur nombre d’occurrences.

Les résultats obtenus sont cohérents entre les deux méthodes, ce qui valide le bon fonctionnement des scripts et de l’analyse par expressions régulières.
