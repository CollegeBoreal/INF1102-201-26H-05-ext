# 🧪 TP : Déploiement automatisé Nginx avec Ansible

# 👤 Informations étudiant

| Champ | Détails |
|-------|---------|
| **Nom** | Calvin |
| **Matricule** | 300152131 |
| **Cours** | Programmation des systèmes |

---

## 🎯 Objectif

Créer un système automatisé qui :
- Installe **nginx**
- Déploie une **page web**
- Active le **service**

---

## 📁 Structure des fichiers

```
🆔/
├── inventory.ini
├── playbook.yml
└── files/
    └── index.html
```

---

## 📋 Étapes réalisées

### Étape 1 — Création du fichier `inventory.ini`

Le fichier `inventory.ini` définit la machine cible (la VM) et les paramètres de connexion SSH :

```ini
[web]
IP_VM ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/ma_cle.pk
```

> Remplacer `IP_VM` par l'adresse IP réelle de la VM.

![Création du fichier inventory](images/1%20bon%20creation%20inventory%20file.png)


> Se Rassurer d'avoir le fichier `ma_cle.pk` a l'emplacement indiquee ou alors adapter a son cas.
---

### Étape 2 — Création du fichier `playbook.yml`

Le playbook Ansible décrit les tâches à exécuter sur la machine cible :
- Installer nginx
- Copier la page HTML
- Démarrer et activer le service nginx

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
```

![Création du playbook YAML](images/2%20creation%20du%20playbookyaml.png)

---

### Étape 3 — Création du fichier `files/index.html`

La page HTML personnalisée qui sera déployée sur le serveur :

```html
<!DOCTYPE html>
<html>
<head>
    <title>🆔 : 300152131 by #Calvin</title>
</head>
<body>
    <h1>🚀 Déploiement réussi avec Ansible</h1>
</body>
</html>
```

![Création du fichier index.html](images/3%20creation%20du%20fichier%20index.png)

---

### Étape 4 — Exécution du playbook

Lancement du playbook avec la commande :

```bash
ansible-playbook -i inventory.ini playbook.yml
```

![Exécution réussie du playbook Ansible](images/4%20execution%20reussi%20ansible.png)

---

### Étape 5 — Vérification du déploiement

Test du site avec `curl` pour confirmer que nginx sert bien la page HTML déployée :

```bash
curl http://<IP_VM>
```

![Site déployé avec succès](images/5%20test%20site%20deploye%20avec%20succes%20.png)

---

## 🧠 Questions

### 1. Pourquoi Ansible est-il idempotent ?

Ansible est **idempotent** car exécuter un playbook plusieurs fois produit toujours le même résultat. Si une tâche est déjà dans l'état souhaité (ex. : nginx déjà installé), Ansible ne refait pas l'action. Cela évite les effets de bord et rend les déploiements sûrs à répéter.

### 2. Différence entre `present` et `started`

| Valeur | Module | Signification |
|--------|--------|---------------|
| `present` | `apt` | Le paquet doit être **installé** (s'il ne l'est pas, Ansible l'installe) |
| `started` | `service` | Le service doit être **en cours d'exécution** (s'il est arrêté, Ansible le démarre) |

### 3. Pourquoi utiliser `become: yes` ?

`become: yes` permet à Ansible d'exécuter les tâches avec les **privilèges superutilisateur (sudo)**. C'est nécessaire pour des actions système comme installer des paquets ou gérer des services, qui requièrent des droits root.
