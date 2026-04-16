# 🧾 6.PWSH – DevOps PowerShell

## 🎯 Objectif  
Dans ce travail, nous avons réalisé un script PowerShell sous Linux permettant d’automatiser des tâches DevOps et de générer des rapports système.

---

## ⚙️ Script utilisé  

Le script `devops_batch.ps1` permet de :

- récupérer les informations système  
- afficher les processus CPU et mémoire  
- vérifier l’espace disque  
- tester la connexion SSH  
- générer un rapport texte et JSON  

---

## 🚀 Exécution du script  

```bash
sudo pwsh /devops-batch/devops_batch.ps1
📸 Exécution du script

🔗 Lien : images/1.png

👉 Cette capture montre :

l’exécution du script PowerShell
les informations système affichées
les résultats du traitement (CPU, mémoire, disque, SSH)
📸 Résultat JSON généré

🔗 Lien : images/2.png

👉 Cette capture montre :

le contenu du fichier rapport.json
les données structurées générées par le script
les informations sur les processus et le système
📂 Fichiers générés

Après l’exécution du script :

rapport.txt → rapport texte lisible
rapport.json → rapport structuré au format JSON
🔍 Vérification
cat rapport.txt
cat rapport.json

👉 Ces commandes permettent de vérifier les résultats générés par le script.

🧠 Conclusion

Ce travail nous a permis de :

automatiser des tâches DevOps
utiliser PowerShell sous Linux
générer des rapports structurés
manipuler des données sous forme d’objets

👉 PowerShell facilite l’automatisation grâce à son approche orientée objets.
