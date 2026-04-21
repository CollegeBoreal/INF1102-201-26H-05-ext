<div align="center">

# 🚀 Ansible - Déploiement Nginx

### ⚡ Infrastructure as Code · Déploiement automatisé · Nginx

<br/>

[![Étudiant](https://img.shields.io/badge/👤_Étudiant-300150557-0d1117?style=for-the-badge&labelColor=00bfff&color=0d1117)](.)
[![Cours](https://img.shields.io/badge/📚_Cours-INF1102--201--26H--05-0d1117?style=for-the-badge&labelColor=059669&color=0d1117)](.)

[![Ansible](https://img.shields.io/badge/Ansible-IaC-EE0000?style=flat-square&logo=ansible)](.)
[![Nginx](https://img.shields.io/badge/Nginx-Active-009639?style=flat-square&logo=nginx)](.)
[![Ubuntu](https://img.shields.io/badge/Ubuntu-22.04_LTS-E95420?style=flat-square&logo=ubuntu)](.)
[![Status](https://img.shields.io/badge/Status-✅_Réussi-brightgreen?style=flat-square)](.)

</div>

---

## 🎯 Objectif

> **Déployer automatiquement un serveur Nginx sur une VM Ubuntu en utilisant Ansible comme outil IaC.**

On décrit *ce que l'on veut*, et Ansible s'occupe du *comment* — approche **déclarative**.

---

## 📁 Structure du projet

```
300150557/
├── inventory.ini
├── playbook.yml
├── README.md
└── files/
    └── index.html
```

---

## ⚙️ Configuration

### 📄 inventory.ini

```ini
[web]
localhost ansible_connection=local
```

> Ansible s'exécutant directement sur la VM, `ansible_connection=local` évite une connexion SSH.

### 📄 playbook.yml

```yaml
- name: Installer et configurer nginx
  hosts: web
  become: yes

  tasks:

    - name: Installer nginx
      apt:
        name: nginx
        state: present
        update_cache: yes

    - name: Copier la page HTML
      copy:
        src: files/index.html
        dest: /var/www/html/index.nginx-debian.html

    - name: Demarrer nginx
      service:
        name: nginx
        state: started
        enabled: yes
```

### 🌐 files/index.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>300150557</title>
</head>
<body>
    <h1>Deploiement reussi avec Ansible</h1>
</body>
</html>
```

---

## 🛠️ Étapes de réalisation

### Étape 1 · Installation d'Ansible

```bash
sudo apt update && sudo apt install -y ansible
ansible --version
```

### Étape 2 · Création de la structure

```bash
mkdir -p 300150557/files
touch 300150557/inventory.ini
touch 300150557/playbook.yml
touch 300150557/files/index.html
```

### Étape 3 · Exécution du Playbook

```bash
ansible-playbook -i inventory.ini playbook.yml
```

### Étape 4 · Vérification

```bash
curl http://localhost
```

---

## 🧠 Questions théoriques

**Pourquoi Ansible est-il idempotent ?**
Ansible vérifie l'état actuel avant d'agir. Si Nginx est déjà installé, il ne le réinstalle pas. On peut relancer le playbook autant de fois qu'on veut : le résultat est toujours identique.

**Différence entre `present` et `started` ?**

| Mot-clé | Cible | Action |
|---------|-------|--------|
| `present` | Paquet | S'assure qu'il est installé |
| `started` | Service | S'assure qu'il est en cours d'exécution |

**Pourquoi `become: yes` ?**
Élève les privilèges en mode sudo, nécessaire pour installer des paquets, écrire dans `/var/www/html/` et gérer des services système.

---

## 📚 Conclusion

Ce TP démontre la puissance d'Ansible pour automatiser la configuration d'un serveur. L'approche déclarative est plus fiable et reproductible qu'un script manuel.

---

<div align="center">

**300150557** · INF1102-201-26H-05 · Avril 2026

</div>
