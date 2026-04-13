<img width="2249" height="1155" alt="Capture d&#39;écran 2026-04-12 183533" src="https://github.com/user-attachments/assets/ad3ab9c2-3907-4c36-be85-7def5d61d2b1" />
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


<img width="2249" height="1155" alt="Capture d&#39;écran 2026-04-12 183533" src="https://github.com/user-attachments/assets/cd4239aa-56c9-4dde-a01f-0e9ffdac9352" />

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

```

<img width="1916" height="296" alt="Capture d&#39;écran 2026-04-12 190946" src="https://github.com/user-attachments/assets/0f27f7c0-f27b-4a64-8576-c5b0dff3b89f" />


