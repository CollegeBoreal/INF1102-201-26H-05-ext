# 🛡️ NGINX LOG MONITORING PIPELINE
### 👤 Justin Sandy

![Crontab](images/Crontab.png)

---

## 🚀 Objectif du projet

Ce projet a pour but de mettre en place un **système automatisé de surveillance des logs Nginx**, permettant de :

- 👁️ Extraire les adresses IP des visiteurs
- 📊 Analyser les accès au serveur web
- 🧠 Identifier les visiteurs les plus fréquents
- ⏱️ Automatiser le traitement via `cron`
- 📁 Stocker les résultats pour audit et monitoring

---

## 🧱 Architecture du système

```text
          ┌──────────────┐
          │  Nginx Web   │
          │   Server     │
          └──────┬───────┘
                 │
                 ▼
     /var/log/nginx/access.log
                 │
                 ▼
     ┌──────────────────────┐
     │ Bash Script (AWK)    │
     │ - extraction IP      │
     │ - nettoyage          │
     │ - tri + analyse      │
     └─────────┬────────────┘
               │
               ▼
   ┌─────────────────────────┐
   │ Output Files            │
   │ - nginx_ips.txt         │
   │ - nginx_ips_freq.txt    │
   │ - logs audit            │
   └─────────┬───────────────┘
             │
             ▼
        ⏰ CRON JOB
   (exécution automatique)
