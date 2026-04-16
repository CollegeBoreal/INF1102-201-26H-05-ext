# 🧾 5.BATCH – Script de gestion système

**Étudiant : 300151258**

---

# 🎯 Objectif

Dans ce travail, nous avons réalisé un script **Bash** permettant d'automatiser plusieurs tâches d'administration système dans le dossier `/entreprise`.

Ce script permet de :

- tester la connectivité réseau
- sauvegarder des fichiers
- créer un utilisateur temporaire
- générer un fichier journal (log)
- compresser les données

---

# ⚙️ Script utilisé

Le script **script_gestion.sh** permet de :

- tester la connectivité réseau avec `ping`
- sauvegarder les fichiers du dossier `/entreprise/data`
- créer un utilisateur temporaire `employe_temp`
- compresser les données dans une archive `.tar.gz`
- enregistrer toutes les opérations dans un fichier log

---

# 📂 Structure du projet

![Structure du projet](images/1.png)

Cette capture montre :

- le dossier `images`
- le fichier `README.md`
- le fichier `script_gestion.sh`

---

# 🚀 Exécution du script

Pour exécuter le script :

```bash
sudo /entreprise/script_gestion.sh
