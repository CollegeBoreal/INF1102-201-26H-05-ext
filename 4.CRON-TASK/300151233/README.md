Rapport – Scruter les logs Nginx avec PowerShell

Objectif



Le but de ce travail est d’analyser le fichier access.log de Nginx pour :



Extraire les adresses IP des visiteurs



Supprimer les doublons



Identifier les IP les plus fréquentes



Automatiser l’exécution toutes les heures



Fichier analysé



Le fichier utilisé est :



/var/log/nginx/access.log



Chaque ligne commence par l’adresse IP du visiteur.

Exemple :



192.168.1.15 - - \[05/Feb/2026:15:20:11 +0000] "GET /index.html HTTP/1.1" 200 1024

Script créé



Un script PowerShell nommé :



scruter\_nginx.ps1



a été créé pour :



Lire le fichier access.log



Extraire la première colonne (IP)



Supprimer les doublons



Enregistrer les IP uniques dans un fichier



Fichiers générés



Après exécution du script :



nginx\_ips.txt → contient les IP uniques



nginx\_ips\_freq.txt → contient les IP les plus fréquentes



nginx\_ips.log → contient la date et l’heure d’exécution



Exécution manuelle



Commande utilisée :



pwsh -File /home/ubuntu/scruter\_nginx.ps1

Automatisation



Le script est exécuté automatiquement toutes les heures avec cron :



0 \* \* \* \* /usr/bin/pwsh -File /home/ubuntu/scruter\_nginx.ps1

Conclusion



Ce travail permet de surveiller les visiteurs du serveur Nginx de manière automatique.



Grâce au script PowerShell et à cron, l’analyse des logs est faite chaque heure sans intervention manuelle.

