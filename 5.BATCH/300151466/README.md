
# TP – Automatisation d'administration avec script Batch (Linux)

**Nom :** bennacer adel
**Numéro étudiant :** 300151466

---

## 1. Objectif du TP

L’objectif de ce travail est de développer un script Bash afin d’automatiser plusieurs tâches d’administration système sous Linux.

Ce script permet de :

- sauvegarder un dossier de l’entreprise ;
- créer un utilisateur temporaire ;
- tester la connectivité réseau ;
- générer un fichier journal ;
- planifier une exécution automatique avec cron ;
- vérifier le bon fonctionnement du script ;
- simuler et corriger des erreurs ;
- ajouter une amélioration au script.

---

## 2. Préparation de l’environnement

### 2.1 Création de la structure

Pour préparer l’environnement, les dossiers suivants ont été créés :

- `/entreprise/data`
- `/entreprise/backup`
- `/entreprise/logs`

Ensuite, deux fichiers de test ont été ajoutés dans le dossier `data`.

### 2.2 Commandes utilisées

```bash
sudo mkdir -p /entreprise/data /entreprise/backup /entreprise/logs

echo "test 1" | sudo tee /entreprise/data/fichier1.txt
echo "test 2" | sudo tee /entreprise/data/fichier2.txt
<img width="593" height="218" alt="c5" src="https://github.com/user-attachments/assets/a0d8368d-8822-421e-831d-961c70bb5485" />
<img width="619" height="289" alt="c4" src="https://github.com/user-attachments/assets/977ee64b-1a3e-480d-9f3d-6198c71cc8ac" />




