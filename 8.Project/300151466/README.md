# 🌐 Projet Monitoring Web Automatisé

**Cours** : INF1102-201-26H-05  
**Étudiant** : Adel Bennacer  
**Matricule** : 300151466  
**Date** : 2026-04-12  

---

## 🎯 Objectif du projet

Ce projet a pour but de surveiller automatiquement plusieurs sites web afin de vérifier :

- leur disponibilité (status HTTP)
- leur temps de réponse

Les données sont enregistrées et analysées pour produire un rapport et un graphique.

---

## ⚙️ Principe de fonctionnement

Le système fonctionne en plusieurs étapes :

1. Envoi de requêtes HTTP vers différents sites
2. Mesure du temps de réponse
3. Sauvegarde des résultats dans un fichier CSV
4. Génération d’un rapport texte
5. Création d’un graphique avec matplotlib
6. Exécution automatique avec cron

---

## 📁 Organisation des fichiers

300151466/
├── scripts/
│ ├── analyse.sh # Script Bash pour lancer le projet
│ └── analyse.py # Script Python principal
├── data/
│ └── monitoring.csv # Données collectées
├── output/
│ ├── rapport.txt # Résultats du monitoring
│ └── graphique_evolution.png # Graphique généré
├── images/ # Captures d'écran du projet
└── README.md


---

01- Connexion à la machine

```bash
ssh -i ~/.ssh/ma_cle \
  -o StrictHostKeyChecking=no \
  -o UserKnownHostsFile=/tmp/ssh_known_hosts_empty \
  ubuntu@10.7.237.239
<img width="458" height="428" alt="ssh" src="https://github.com/user-attachments/assets/bf5ab009-09e0-4ccf-9c9b-bf7d1847b404" />

02- Lancement du script
Ce script exécute automatiquement le programme Python et génère les fichiers de sortie:
bash scripts/analyse.sh
<img width="506" height="119" alt="image" src="https://github.com/user-attachments/assets/210cae89-1576-4585-ad9f-fa7ad484941f" />

03-Automatisation avec Cron

Le script est programmé pour s’exécuter toutes les 3 minutes :

*/3 * * * * bash /home/ubuntu/INF1102-201-26H-05/8.Project/300151466/scripts/analyse.sh

Cela permet de collecter les données en continu sans intervention manuelle.

<img width="1000" height="600" alt="graphique_evolution" src="https://github.com/user-attachments/assets/957b2879-005a-46b6-b143-6e3978f8a6de" />

04- rapport généré:
<img width="889" height="441" alt="installer " src="https://github.com/user-attachments/assets/21cbbe31-de53-4aad-815d-8e4bb9d479ba" />

04:Résultats obtenus

Le projet génère automatiquement :

un fichier CSV contenant toutes les données
un rapport texte avec les résultats
un graphique représentant l’évolution des performances

05:Déploiement sur GitHub

Les fichiers ont été ajoutés et envoyés vers le dépôt GitHub avec les commandes suivantes :

git add .
git commit -m "Projet monitoring web"
git push
06:Conclusion

Ce projet démontre l’importance de l’automatisation dans la surveillance des systèmes.

Il permet :

de suivre les performances des sites web
de détecter les erreurs rapidement
d’analyser les données de manière visuelle

C’est une solution simple et efficace pour le monitoring en environnement Linux.




