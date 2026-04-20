# 🚀 TP Ansible - Déploiement Nginx

**Étudiant : Kahina Zerkani 300151556**

---

## 🎯 Objectif

Ce projet consiste à automatiser le déploiement d’un serveur web **Nginx** avec **Ansible** en utilisant le principe de **Infrastructure as Code (IaC)**.

---

## ⚙️ Technologies utilisées

* Ansible
* Nginx
* YAML
* Linux (Ubuntu)
* GitHub

---

## 📁 Structure du projet

```
300151556/
├── README.md
├── inventory.ini
├── playbook.yml
└── images/
```

---

## 🧾 Description des fichiers

### 📄 inventory.ini

Fichier qui définit les machines cibles.

```ini
[web]
localhost ansible_connection=local
```

---

### 📜 playbook.yml

Playbook Ansible permettant de :

* Installer Nginx
* Déployer une page HTML
* Démarrer et activer le service

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

    - name: Creer page HTML
      copy:
        content: "<h1>Deploiement Ansible reussi - 300151556</h1>"
        dest: /var/www/html/index.nginx-debian.html

    - name: Demarrer nginx
      service:
        name: nginx
        state: started
        enabled: yes
```

---

## ▶️ Exécution

Commande utilisée :

```bash
ansible-playbook -i inventory.ini playbook.yml
```

---

## 🖼️ Résultats

### 🔹 Exécution du playbook
<img width="959" height="461" alt="1" src="https://github.com/user-attachments/assets/130c44c0-6cea-4570-833c-baeaa1781123" />


---

### 🔹 Résultat dans le navigateur
<img width="832" height="257" alt="2e" src="https://github.com/user-attachments/assets/03fe2901-4d33-42b6-ac8a-77cb4fdc7243" />



---

## ✅ Vérification

```bash
http://10.7.237.240/
```

---

## 🧠 Concepts appris

* Gestion de configuration
* Infrastructure as Code (IaC)
* Différence entre approche impérative et déclarative
* Utilisation d’Ansible avec YAML
* Automatisation du déploiement

---

## 💡 Conclusion

Ansible permet de :

✔ Automatiser les tâches
✔ Éviter les erreurs humaines
✔ Assurer la reproductibilité
✔ Gérer efficacement les configurations système

---

## 👩‍💻 Auteur

**Kahina Zerkani**
Étudiante en Techniques des systèmes informatiques
Collège Boréal

