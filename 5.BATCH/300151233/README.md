# TP – Automatisation d'administration avec script Batch (Linux)

**Étudiant :** 300151233

## Objectif
Ce travail consiste à créer un script Bash sous Linux permettant d’automatiser certaines tâches d’administration système.

Le script doit :
- tester la connectivité réseau ;
- sauvegarder les fichiers d’un dossier ;
- créer un utilisateur temporaire ;
- générer un fichier journal ;
- créer une archive compressée ;
- permettre une planification automatique avec cron.

---

## Structure du projet

Ce dépôt contient les fichiers suivants :

- `README.md` : description du travail et instructions d’exécution ;
- `script_gestion.sh` : script Bash principal.

---

## Préparation de l’environnement

Créer les dossiers nécessaires :

```bash
mkdir -p ~/entreprise/data
mkdir -p ~/entreprise/backup
mkdir -p ~/entreprise/logs
echo "Fichier 1" > ~/entreprise/data/fichier1.txt
echo "Fichier 2" > ~/entreprise/data/fichier2.txt
