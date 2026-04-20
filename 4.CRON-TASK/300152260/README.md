# 🔍 Scruter les logs Nginx — CRON-TASK

## 👤 Informations étudiant
| Champ | Détails |
|-------|---------|
| **Nom** | Mohib |
| **Matricule** | 300152260 |
| **Cours** | Programmation des systèmes |

## 🎯 Objectif
Extraire automatiquement toutes les adresses IP qui visitent un site via les logs Nginx, stocker les résultats et automatiser l'exécution toutes les heures.

## 📁 Structure du projet
/home/ubuntu/
├── scruter_nginx.sh
├── nginx_ips.txt
└── nginx_ips.log

## 🚀 Commandes
nano /home/ubuntu/scruter_nginx.sh
chmod +x /home/ubuntu/scruter_nginx.sh
/home/ubuntu/scruter_nginx.sh
crontab -e

## ⏱️ Cron configuré
0 * * * * /home/ubuntu/scruter_nginx.sh

## ✅ Réalisations
| Étape | Status |
|-------|--------|
| Script scruter_nginx.sh créé | ✅ |
| Script rendu exécutable | ✅ |
| Script testé | ✅ |
| Cron configuré toutes les heures | ✅ |
| Service cron actif | ✅ |