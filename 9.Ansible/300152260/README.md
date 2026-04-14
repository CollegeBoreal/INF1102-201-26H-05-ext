# 9️⃣ Ansible – Déploiement automatisé Nginx

## 👤 Informations étudiant
| Champ | Détails |
|-------|---------|
| **Nom** | Mohib |
| **Matricule** | 300152260 |
| **Cours** | INF1102 |

## 🎯 Objectif
Créer un système automatisé qui :
- Installe nginx
- Déploie une page web
- Active le service

## 📁 Structure
300152260/
├── inventory.ini
├── playbook.yml
└── files/
    └── index.html

## 🚀 Exécution
ansible-playbook -i inventory.ini playbook.yml

## 🧠 Questions
1. Ansible est idempotent car il vérifie l'état avant d'agir.
2. present = installer, started = démarrer le service.
3. become: yes = exécuter avec les droits sudo.

## ✅ Réalisations
| Étape | Status |
|-------|--------|
| inventory.ini créé | ✅ |
| playbook.yml créé | ✅ |
| files/index.html créé | ✅ |