
Nom : Syphax Ouadfel

ID : 300151233

TP : Analyse des logs Nginx avec Regex

Objectif du TP

L’objectif de ce travail est de développer des scripts permettant d’analyser les fichiers de logs du serveur Nginx.
L’analyse est réalisée en utilisant des expressions régulières (Regex) avec deux langages :

PowerShell
Python

Le script doit générer automatiquement un rapport contenant des statistiques sur les requêtes HTTP.

Fichier analysé

Le fichier utilisé pour l’analyse est :

/var/log/nginx/access.log

Ce fichier contient toutes les requêtes reçues par le serveur web Nginx.

Méthodologie

Pour analyser les logs, des expressions régulières ont été utilisées pour extraire :

Les adresses IP
Les codes HTTP (200, 404, 500…)
Les pages demandées (GET)
Les erreurs (codes 4xx et 5xx)

Exemples de Regex utilisés :

IP : (\d{1,3}.){3}\d{1,3}
Code HTTP : " (\d{3})
Pages : "GET ([^ ]+)
Erreurs : ^[45]
Implémentation
Script PowerShell

Le script PowerShell permet de :

Lire le fichier de logs
Compter le nombre total de requêtes
Extraire les codes HTTP
Identifier les erreurs
Afficher les 5 IP les plus fréquentes
Afficher les 5 pages les plus demandées
Script Python

Le script Python utilise :

Le module re (expressions régulières)
Le module collections.Counter

Il permet de produire les mêmes résultats que le script PowerShell, avec une approche différente.

Résultats obtenus

Les scripts génèrent automatiquement des fichiers :

rapport_nginx_ps1_YYYY-MM-DD.txt
rapport_nginx_py_YYYY-MM-DD.txt

Ces rapports contiennent :

Nombre total de requêtes
Nombre d’erreurs HTTP
Nombre d’erreurs 404 et 500
Top 5 des adresses IP
Top 5 des pages les plus visitées
Automatisation

Une tâche planifiée (cron) a été configurée pour exécuter automatiquement le script :

crontab -e

Exemple :

0 2 * * * /usr/bin/pwsh /home/ubuntu/.../analyse_nginx.ps1

Cela permet d’exécuter l’analyse chaque jour à 2h du matin.

Problèmes rencontrés

Durant le TP, plusieurs difficultés ont été rencontrées :

Problèmes de chemins des fichiers
Accès refusé au fichier log (résolu avec sudo)
Conflits Git lors du push
Mauvaise structure des dossiers

Ces problèmes ont été corrigés en ajustant les chemins et la structure du projet.

Conclusion

Ce TP a permis de :

Comprendre l’utilisation des expressions régulières
Manipuler des logs système réels
Comparer PowerShell et Python
Automatiser des tâches avec cron
Utiliser Git pour gérer un projet

L’analyse des logs est une compétence importante pour la surveillance et la sécurité des systèmes.
