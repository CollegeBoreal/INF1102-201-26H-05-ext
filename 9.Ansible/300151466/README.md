
 lecon: Gestion de configuration avec Ansible (IaC)
  nom:adel bennacer 
  id:300151466

## 🎯 Objectif

> Déployer automatiquement un serveur **Nginx** sur une machine Ubuntu à l’aide de **Ansible**.

Ce TP démontre l’approche **Infrastructure as Code (IaC)** où l’on automatise la configuration d’un serveur.

```
Machine locale (VM)
        │
        │ ansible-playbook
        ▼
Serveur Nginx → http://10.7.237.239
```

---

## 📁 Structure du projet

```
300151466/
│
├── inventory.ini
├── playbook.yml
├── README.md
│
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

---

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

    - name: Démarrer nginx
      service:
        name: nginx
        state: started
        enabled: yes
```

---

### 📄 index.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>300151466</title>
</head>
<body>
    <h1>Déploiement réussi avec Ansible</h1>
</body>
</html>
```

---

## 🛠️ Étapes de réalisation

### 1️⃣ Installation d’Ansible

```bash
sudo apt update && sudo apt install -y ansible
ansible --version
```

<img width="620" height="111" alt="installer ansible" src="https://github.com/user-attachments/assets/cc6bcb7f-7142-4f24-9184-799425eb2e31" />


---

### 2️⃣ Création du projet

```bash
mkdir -p 300151466/files
touch inventory.ini playbook.yml files/index.html
```

<img width="278" height="121" alt="creation de la structure" src="https://github.com/user-attachments/assets/96e9879c-25a4-42e4-a58d-0a444e66897c" />


### 3️⃣ Exécution du playbook

```bash
ansible-playbook -i inventory.ini playbook.yml
```
<img width="819" height="231" alt="lancer playbok" src="https://github.com/user-attachments/assets/b52c6d21-0d23-4358-a207-d2ee4861aadd" />



### 4️⃣ Vérification

```bash
curl http://10.7.237.239
```

Résultat attendu :

```
Déploiement réussi avec Ansible
```

<img width="330" height="131" alt="verification finale" src="https://github.com/user-attachments/assets/7daf953a-fe1c-40f2-94af-cec26341ebed" />


## ⚠️ Difficultés rencontrées

| Problème       | Solution                                  |
| -------------- | ----------------------------------------- |
| Erreur SSH     | Utilisation de `ansible_connection=local` |
| Git conflit    | `git pull --rebase`                       |
| Dossier absent | Création avec `mkdir`                     |

---

## ✅ Résultat

```
Ansible installé ✔
Nginx fonctionnel ✔
Page web accessible ✔
```

---

## 📚 Conclusion

Ce TP m’a permis de comprendre :

* L’automatisation avec Ansible
* Le principe de l’Infrastructure as Code
* Le déploiement automatique de services

Ansible permet de gagner du temps et d’éviter les erreurs humaines dans la configuration.




