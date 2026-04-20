# 🛡️ LINUX ENTERPRISE AUTOMATION PIPELINE ⚡
### 👤 Justin Sandy | ID: 300151403 | DevOps / System Automation Project

<p align="center">
  <img src="https://media.giphy.com/media/3o7aD2saalBwwftBIY/giphy.gif" width="150"/>
  <img src="https://media.giphy.com/media/kH1DBkPNyZPOk0BxrM/giphy.gif" width="150"/>
  <img src="https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif" width="150"/>
</p>

---

## 🎯 OBJECTIF DU PROJET

Ce projet consiste à créer un **système d’automatisation Linux en environnement entreprise** permettant de :

- 📦 Sauvegarder automatiquement des fichiers critiques
- 👤 Créer et gérer un utilisateur temporaire
- 🌐 Tester la connectivité réseau
- 📊 Générer un fichier journal (log)
- ⏰ Automatiser les tâches avec `cron`
- 🧠 Diagnostiquer les erreurs système

---

## 🚀 ARCHITECTURE DU SYSTÈME

```text
🖥 Linux Server
      │
      ▼
📁 entreprise/data
      │
      ▼
🐚 Bash Automation Script
      │
 ┌────┼───────────────┬───────────────┐
 ▼    ▼               ▼               ▼
📦 Backup   👤 User Mgmt   🌐 Network Test   📊 Logs
      │
      ▼
⏰ Cron Scheduler (Automation)
