\# TP - Déploiement automatisé Nginx avec Ansible



\## Informations générales



\- \*\*Cours\*\* : INF1102 - Gestion de configuration avec Ansible (IaC)

\- \*\*Étudiant\*\* : 300150268

\- \*\*Sujet\*\* : Déploiement automatisé d'un site web statique avec Nginx et Ansible



\## Objectif du TP



Ce travail a pour objectif de mettre en pratique Ansible comme outil de gestion de configuration dans une approche Infrastructure as Code (IaC). Le but est d'automatiser le déploiement d'un serveur web Nginx ainsi que la publication d'un site statique.



A la fin du TP, le système doit être capable de :



\- Installer automatiquement nginx

\- Copier les fichiers du site web vers le serveur distant

\- Démarrer et activer le service nginx

\- Rendre le site accessible à partir d'un navigateur



\## Structure du projet



300150268/

├── inventory.ini

├── playbook.yml

├── images/

└── files/

&#x20;   ├── index.html

&#x20;   ├── style.css

&#x20;   └── script.js



\## Exécution du playbook



ansible-playbook -i inventory.ini playbook.yml



\## Vérification



\### 1. Exécution du playbook

!\[Exécution du playbook](images/playbook\_execution.png)



\### 2. Site dans le navigateur

!\[Site déployé](images/site\_navigateur.png)



\### 3. Structure des fichiers

!\[Structure](images/structure\_fichiers.png)



\## Réponses aux questions



\### Pourquoi Ansible est-il idempotent ?

Ansible peut exécuter plusieurs fois le même playbook sans modifier le système si l'état désiré est déjà atteint.



\### Différence entre present et started

\- present : assure qu'un paquet est installé

\- started : assure qu'un service est en cours d'exécution



\### Pourquoi utiliser become: yes ?

Pour exécuter les tâches avec des privilèges administrateur.



\## Conclusion



Ce TP m'a permis de comprendre comment Ansible automatise le déploiement d'un serveur web. Le déploiement devient plus rapide, plus fiable et plus reproductible.

