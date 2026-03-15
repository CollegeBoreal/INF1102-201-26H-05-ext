# TP – Batch DevOps PowerShell sous Linux

## Informations générales

- **Nom :** Tarik Tidjet
- **Boréal ID :** 300150275
- **Cours :** INF1102
- **Environnement :** Ubuntu 22.04 LTS
- **Shell utilisé :** PowerShell 7.5.5

## Objectif du laboratoire

L’objectif de ce laboratoire est d’installer PowerShell sur Ubuntu 22.04 et de réaliser un script DevOps capable d’automatiser certaines tâches d’administration système.  
Le script doit vérifier l’état du système, tester la connectivité SSH et générer des rapports exploitables.

## Travail réalisé

Le fichier `devops_batch.ps1` a été créé et exécuté dans un environnement Ubuntu 22.04.  
Ce script permet de :

- récupérer la date d’exécution
- identifier l’utilisateur connecté
- récupérer le nom de la machine
- afficher les 5 processus les plus consommateurs en CPU
- afficher les 5 processus les plus consommateurs en mémoire
- afficher l’utilisation du disque
- tester la connectivité SSH vers `127.0.0.1`
- générer un rapport texte
- générer un rapport JSON

## Installation de PowerShell

Les commandes suivantes ont été utilisées pour installer PowerShell sur Ubuntu 22.04 :

```bash
sudo apt update
sudo apt install -y wget apt-transport-https software-properties-common
wget https://packages.microsoft.com/config/ubuntu/22.04/packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
sudo apt update
sudo apt install -y powershell