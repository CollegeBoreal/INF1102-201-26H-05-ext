# 9️⃣ Ansible — Déploiement automatisé Nginx

<div align="center">

![Ansible](https://img.shields.io/badge/Ansible-EE0000?style=for-the-badge&logo=ansible&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)
![YAML](https://img.shields.io/badge/YAML-CB171E?style=for-the-badge&logo=yaml&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complété-brightgreen?style=for-the-badge)

</div>

---

## 👤 Informations étudiant

| Champ | Détails |
|-------|---------|
| **Nom** | Gacem Ouail |
| **Matricule** | 300148094 |
| **Cours** | INF1102 |
| **Établissement** | Collège Boréal |

---

## 🎯 Objectif

Ce laboratoire consiste à créer un système **automatisé avec Ansible** qui :

- 🔧 Installe **Nginx** sur une VM distante
- 🌐 Déploie une **page web** personnalisée
- ▶️ Active et démarre le **service Nginx**
- ✅ Le tout de manière **idempotente et déclarative**

---

## 📁 Structure du projet

```
300148094/
│
├── inventory.ini          # Liste des machines cibles
├── playbook.yml           # Instructions Ansible (YAML)
└── files/
    └── index.html         # Page web déployée sur le serveur
```

---

## 📄 Fichiers du projet

### inventory.ini

Ce fichier définit les **machines cibles** sur lesquelles Ansible va agir. Il indique l'adresse IP de la VM, l'utilisateur SSH et la clé privée à utiliser.

```ini
[web]
IP_VM ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/ma_cle.pk
```

> 🔑 `IP_VM` est remplacé par l'adresse IP réelle de ma VM Proxmox.

---

### playbook.yml

Ce fichier contient les **tâches déclaratives** qu'Ansible doit exécuter sur les machines du groupe `[web]`.

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

    - name: Démarrer nginx
      service:
        name: nginx
        state: started
        enabled: yes

  handlers:
    - name: restart nginx
      service:
        name: nginx
        state: restarted
```

**Explication des tâches :**

| Tâche | Module Ansible | Rôle |
|-------|---------------|------|
| Installer nginx | `apt` | Installe le paquet nginx via APT |
| Copier la page HTML | `copy` | Envoie `index.html` vers le serveur |
| Démarrer nginx | `service` | Lance et active nginx au démarrage |
| Handler restart | `service` | Redémarre nginx si une config change |

---

### files/index.html

Page web personnalisée déployée automatiquement par Ansible sur le serveur Nginx :

```html
<!DOCTYPE html>
<html>
<head>
    <title>300148094</title>
</head>
<body>
    <h1>🚀 Déploiement réussi avec Ansible</h1>
    <p>Ouail Gacem — 300148094</p>
</body>
</html>
```

---

## 🚀 Exécution

Pour lancer le déploiement complet, j'exécute la commande suivante depuis mon répertoire `300148094/` :

```bash
ansible-playbook -i inventory.ini playbook.yml
```

**Sortie attendue dans le terminal :**

```
PLAY [Installer et configurer nginx] *****************************

TASK [Gathering Facts] *******************************************
ok: [IP_VM]

TASK [Installer nginx] *******************************************
changed: [IP_VM]

TASK [Copier la page HTML] ***************************************
changed: [IP_VM]

TASK [Démarrer nginx] ********************************************
ok: [IP_VM]

PLAY RECAP *******************************************************
IP_VM : ok=4  changed=2  unreachable=0  failed=0
```

---

## 🧪 Vérification

Après l'exécution du playbook, je vérifie que Nginx est bien en ligne avec :

```bash
curl http://IP_VM
```

Résultat attendu :

```html
<!DOCTYPE html>
<html>
<head><title>300148094</title></head>
<body>
    <h1>🚀 Déploiement réussi avec Ansible</h1>
    <p>Ouail Gacem — 300148094</p>
</body>
</html>
```

---

## 🧠 Réponses aux questions

**1. Pourquoi Ansible est-il idempotent ?**

Ansible **vérifie l'état actuel** de la machine avant d'agir. Si nginx est déjà installé et démarré, il ne refait rien. On peut exécuter le playbook plusieurs fois sans risque d'erreur ou de double installation.

**2. Différence entre `present` et `started` ?**

| Valeur | Module | Signification |
|--------|--------|---------------|
| `present` | `apt` | Installe le paquet s'il n'est pas déjà là |
| `started` | `service` | Démarre le service s'il n'est pas déjà actif |

**3. Pourquoi utiliser `become: yes` ?**

`become: yes` permet à Ansible d'exécuter les tâches avec les **droits sudo** (root). Sans cela, les commandes comme `apt install` ou `service` seraient refusées par le système.

---

## ✅ Réalisations

| Étape | Statut |
|-------|--------|
| `inventory.ini` créé | ✅ Complété |
| `playbook.yml` créé | ✅ Complété |
| `files/index.html` créé | ✅ Complété |
| Déploiement Nginx réussi | ✅ Complété |
| Vérification avec `curl` | ✅ Complété |

---

## 🛠️ Technologies utilisées

| Technologie | Rôle |
|-------------|------|
| **Ansible** | Outil IaC de gestion de configuration |
| **YAML** | Format des playbooks Ansible |
| **Nginx** | Serveur web déployé automatiquement |
| **SSH** | Protocole de connexion aux machines cibles |
| **Proxmox** | Hyperviseur hébergeant la VM cible |

---

## 💡 Ce que j'ai retenu

- **Ansible = IaC orienté configuration** — il configure l'intérieur des machines
- **Déclaratif** → on décrit l'état voulu, Ansible décide comment y arriver
- **YAML** → indentation obligatoire avec 2 espaces, pas de tabulations
- **Complémentaire à Terraform** → Terraform crée les VM, Ansible les configure

---

## 👨‍💻 Auteur

**Ouail Gacem**  
Étudiant — Collège Boréal  
Cours INF1102 — Programmation système
