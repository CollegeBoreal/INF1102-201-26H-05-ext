# 🚀 Projet Ansible – Déploiement automatique de Nginx

## 📌 Description
Ce projet utilise Ansible sur WSL (Ubuntu) pour automatiser le déploiement et la configuration d’un serveur web Nginx sur une machine virtuelle distante.

---

## 🧱 Architecture
- 🖥️ Machine locale : Windows + WSL (Ubuntu)
- 🎯 Machine cible : VM Ubuntu (10.7.237.238)
- ⚙️ Outil d’automatisation : Ansible
- 🌐 Serveur web : Nginx

---

## ⚙️ Fonctionnalités
- Installation automatique de Nginx
- Démarrage et activation du service
- Déploiement d’une page HTML personnalisée
- Accès au site via l’adresse IP de la VM

---

## 📁 Structure du projet
/9.Ansible/300151403  
│── inventory.ini  
│── playbook.yml  
│── files/  
│   └── index.html  
│── images/  

---

## 📜 Playbook Ansible
Le playbook automatise :
- Installation de Nginx
- Copie d’une page web personnalisée
- Démarrage et activation du service

---

## 🚀 Déploiement

### 1. Exécuter le playbook
```bash
ansible-playbook -i inventory.ini playbook.yml
