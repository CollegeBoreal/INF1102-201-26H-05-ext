# 🛠️ Système d'Automatisation et d'Administration Linux
> **Étudiant :** JUSTIN 300151403  
> **Contexte :** Projet académique de gestion de maintenance et sauvegarde.

---

## 🎯 Objectif du Projet
Développement d'un script Bash dynamique permettant l'automatisation des tâches critiques sur un serveur d'entreprise :
1. **Sécurité réseau** : Test de connectivité automatique.
2. **Gestion des données** : Sauvegarde et archivage compressé.
3. **Administration** : Gestion d'utilisateurs temporaires.
4. **Audit** : Journalisation centralisée des opérations (Logs).
5. **Ordonnancement** : Automatisation via Cron.

---

## 🖥️ Environnement Requis
* **Distribution :** Linux (Ubuntu, Debian ou CentOS)
* **Accès :** Privilèges Sudo requis
* **Services :** Cron, Tar, Bash

---

## 🔹 ÉTAPE 1 : Préparation de la Structure
Initialisation des répertoires de travail :

```bash
mkdir -p entreprise/{data,backup,logs}
echo "Données test 1" | sudo tee entreprise/data/fichier1.txt
echo "Données test 2" | sudo tee entreprise/data/fichier2.txt
