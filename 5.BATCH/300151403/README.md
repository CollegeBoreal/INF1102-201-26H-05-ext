# 🛠️ Système d'Automatisation et d'Administration Linux
> **Étudiant :** JUSTIN 300151403  
> **Contexte :** Projet académique de gestion de maintenance et sauvegarde.

---

## 🎯 Objectif du Projet
Développement d'un script Bash dynamique permettant l'automatisation des tâches critiques sur un serveur d'entreprise :
1. **Sécurité réseau** : Test de connectivité automatique.
2. **Gestion des données** : Sauvegarde et archivage compressé.
3. **Administration** : Gestion d'utilisateurs temporaires.
4. **Audit** : Journalisation centralisée des opérations (Logs).##JUSTIN 300151403
## 🎯 Objectif

Programmer un script Batch sous **Linux** permettant de :

1. Sauvegarder un dossier d’entreprise
2. Créer un utilisateur temporaire
3. Tester la connectivité réseau
4. Générer un fichier journal (log)
5. Planifier l’exécution automatique avec **cron**
6. Vérifier l’exécution et diagnostiquer les erreurs

---

# 🖥 Environnement requis

* Distribution Linux (ex: Ubuntu Server)
* Accès sudo
* Terminal
* Service cron actif

---

# 🔹 PARTIE 1 – Préparation de l’environnement

Créer la structure suivante :

```bash
mkdir -p entreprise/data
mkdir -p entreprise/backup
mkdir -p entreprise/logs
```

Créer des fichiers test :

```bash
echo "Fichier 1" | sudo tee entreprise/data/fichier1.txt
echo "Fichier 2" | sudo tee entreprise/data/fichier2.txt
```

---

# 🔹 PARTIE 2 – Création du script Batch

Créer le fichier :

```bash
nano entreprise/script_gestion.sh
```

---

## 📄 CODE COMPLET À INTÉGRER

```bash
#!/bin/bash

LOG="~/entreprise/logs/log.txt"
DATE=$(date)

echo "===================================" >> $LOG
echo "Début exécution : $DATE" >> $LOG

# 1. Vérification réseau
echo "Test réseau..." >> $LOG
ping -c 4 8.8.8.8 >> $LOG 2>&1

# 2. Sauvegarde des fichiers
echo "Sauvegarde en cours..." >> $LOG
cp -r ~/entreprise/data/* ~/entreprise/backup/ >> $LOG 2>&1

# 3. Création utilisateur temporaire
USER_TEMP="employe_temp"

if id "$USER_TEMP" &>/dev/null; then
    echo "Utilisateur existe déjà." >> $LOG
else
    sudo useradd $USER_TEMP
    echo "$USER_TEMP:Temp1234" | sudo chpasswd
    echo "Utilisateur créé." >> $LOG
fi

# 4. Compression archive
tar -czvf ~/entreprise/backup/backup_$(date +%F).tar.gz ~/entreprise/data >> $LOG 2>&1

echo "Fin exécution : $(date)" >> $LOG
echo "===================================" >> $LOG
```

---

# 🔹 PARTIE 3 – Rendre exécutable

```bash
chmod +x ~/entreprise/script_gestion.sh
```

---

# 🔹 PARTIE 4 – Test manuel

Exécuter :

```bash
~/entreprise/script_gestion.sh
```

Vérifier :

* Les fichiers copiés dans `~/entreprise/backup`
* L’archive `.tar.gz`
* L’utilisateur créé :

```bash
cat /etc/passwd | grep employe_temp
```
<img width="1149" height="63" alt="Capture d&#39;écran 2026-04-13 111527" src="https://github.com/user-attachments/assets/b5c04693-5a45-40a5-9589-e87f1463db8b" />


* Le fichier log :

```bash
cat ~/entreprise/logs/log.txt
```

<img width="2251" height="1290" alt="Capture d&#39;écran 2026-04-13 111612" src="https://github.com/user-attachments/assets/027c226f-a74b-405d-8bd2-9081b4c01e0f" />


---

# 🔹 PARTIE 5 – Planification avec Cron

Éditer la crontab :

```bash
crontab -e
```

Ajouter :

```
0 2 * * * ${HOME}/entreprise/script_gestion.sh
```

➡ Exécution tous les jours à 2h00

---

# 🔹 PARTIE 6 – Vérification de l’exécution

Vérifier que cron fonctionne :

```bash
systemctl status cron
```

<img width="2239" height="656" alt="Capture d&#39;écran 2026-04-13 111656" src="https://github.com/user-attachments/assets/f71be251-bdbf-4d02-9a9d-399fc20a8907" />


Consulter les journaux :

```bash
journalctl -u cron
```
<img width="2121" height="1302" alt="Capture d&#39;écran 2026-04-13 111736" src="https://github.com/user-attachments/assets/3aa7581e-5df5-4244-a3ed-34b24c3fadae" />


ou

```bash
cat /var/log/syslog | grep CRON
```
<img width="2251" height="1290" alt="Capture d&#39;écran 2026-04-13 111612" src="https://github.com/user-attachments/assets/b7f3f312-d777-488d-86a0-4d6ea8165815" />


---

# 🔹 PARTIE 7 – Dépannage

| Problème          | Cause possible        | Solution                 |
| ----------------- | --------------------- | ------------------------ |
| Permission denied | Script non exécutable | chmod +x                 |
| Useradd échoue    | Pas sudo              | Exécuter en root         |
| Archive vide      | Mauvais chemin        | Vérifier source          |
| Cron ne lance pas | Mauvais PATH          | Utiliser chemins absolus |

---

# 🔹 PARTIE 8 – Amélioration (niveau avancé)

## Supprimer l’utilisateur après sauvegarde

Ajouter à la fin :

```bash
sudo userdel -r employe_temp
```

---

## Ajouter gestion d’erreur

Exemple :

```bash
if [ $? -ne 0 ]; then
   echo "Erreur lors de la sauvegarde" >> $LOG
fi
```

---

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
