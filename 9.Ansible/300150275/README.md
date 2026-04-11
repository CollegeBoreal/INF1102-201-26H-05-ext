# 🚀 TP Ansible - Déploiement automatisé Nginx

**Étudiant :** 300150275  
**Cours :** INF1102-201-26H-05  
**Date :** Avril 2026  

---

## 📋 Description

Ce TP consiste à déployer automatiquement un serveur **Nginx** sur une machine virtuelle Ubuntu en utilisant **Ansible**, un outil d'Infrastructure as Code (IaC).

---

## 📁 Structure du projet
300150275/
├── inventory.ini
├── playbook.yml
├── README.md
└── files/
└── index.html
---

## 🛠️ Étapes réalisées

### 1️⃣ Installation d'Ansible

```bash
sudo apt update && sudo apt install -y ansible
```

![ansible-version](images/ansible-version.png)

---

### 2️⃣ Structure des fichiers

![structure-fichiers](images/structure-fichiers.png)

---

### 3️⃣ Exécution du Playbook

```bash
ansible-playbook -i inventory.ini playbook.yml
```

![playbook-execution](images/playbook-execution.png)

---

### 4️⃣ Vérification

```bash
curl http://10.7.237.231
```

![curl-verification](images/curl-verification.png)

---

## 🧠 Réponses aux questions

### 1. Pourquoi Ansible est-il idempotent ?
Ansible vérifie l'état actuel avant d'agir. Si Nginx est déjà installé, il ne le réinstalle pas.

### 2. Différence entre `present` et `started`
- **`present`** → le paquet est installé
- **`started`** → le service est en cours d'exécution

### 3. Pourquoi `become: yes` ?
Pour exécuter les commandes en mode **sudo** (administrateur).

---

## ✅ Résultat

- ✔ Ansible installé
- ✔ Nginx déployé automatiquement
- ✔ Page HTML accessible via `http://10.7.237.231`
