# TP - Déploiement automatisé Nginx avec Ansible

## Informations générales
- Cours : INF1102
- Etudiant : 300151233
- Sujet : Déploiement automatisé d’un serveur web Nginx avec Ansible sur Ubuntu

## Objectif du travail
Ce travail a pour objectif de mettre en pratique la gestion de configuration avec Ansible dans une approche Infrastructure as Code (IaC). Le but est d’automatiser l’installation de Nginx, le déploiement d’une page HTML et l’activation du service web.

## Structure du projet
300151233/
├── README.md
├── inventory.ini
├── playbook.yml
└── files/
    └── index.html

## Description des fichiers

### inventory.ini
Ce fichier contient la machine cible sur laquelle Ansible exécute les tâches.
Il précise l’adresse IP de la VM Ubuntu, l’utilisateur SSH et la clé privée utilisée.

### playbook.yml
Ce playbook permet de :
- mettre à jour le cache APT ;
- installer nginx ;
- copier le fichier HTML vers le serveur ;
- démarrer le service nginx ;
- activer nginx au démarrage.

### files/index.html
Ce fichier représente la page web déployée automatiquement par Ansible.

## Commandes utilisées

### Vérification de l’adresse IP
```bash
ip a
