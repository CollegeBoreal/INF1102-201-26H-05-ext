## Exercice : Scruter les logs Nginx et détecter les IP des visiteurs

Création un script shell automatisé

<img width="353" height="37" alt="image" src="https://github.com/user-attachments/assets/a5714d37-67db-44ff-b759-9fe0870918ba" />

Rendre le script exécutable

chmod +x /home/ubuntu/scruter_nginx.sh

Tester le script 

/home/ubuntu/scruter_nginx.sh
cat /home/ubuntu/nginx_ips.txt

## Automatiser avec cron (toutes les heures) 

Édit le crontab de l’utilisateur et Ajout la ligne suivante pour exécuter le script toutes les heures  :
<img width="538" height="390" alt="image" src="https://github.com/user-attachments/assets/21da1bb5-c952-486c-ab3b-91fedf224cc3" />

Vérifier que le cron est bien actif :

<img width="844" height="313" alt="image" src="https://github.com/user-attachments/assets/77fc0de6-f990-496b-a5c2-9c6130ef1724" />
##  Bonus : IP les plus fréquentes



