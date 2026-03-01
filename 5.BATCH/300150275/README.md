# TP – Automatisation d’administration avec script Bash (Linux)

## Étudiant
300150275

## Objectif du TP
Ce travail consiste à automatiser des tâches d’administration sous Linux à l’aide d’un script Bash.

Le script permet de :

- Sauvegarder le dossier `/entreprise/data`
- Tester la connectivité réseau (ping 8.8.8.8)
- Créer un utilisateur temporaire
- Générer un fichier journal (log)
- Compresser les données en archive `.tar.gz`
- Planifier l’exécution automatique avec cron
- Vérifier et diagnostiquer les erreurs

## Planification Cron
Le script est planifié pour s’exécuter tous les jours à 02:00 :

0 2 * * * /entreprise/script_gestion.sh

## Preuves d’exécution
Les captures d’écran démontrant le fonctionnement du script se trouvent dans le dossier `images/`.

## Conclusion
Le script fonctionne correctement.  
Les sauvegardes sont créées, l’utilisateur temporaire est généré, le log est mis à jour et la planification cron est active.
