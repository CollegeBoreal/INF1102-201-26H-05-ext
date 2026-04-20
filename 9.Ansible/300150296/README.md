\# Ansible - 300150296



\## Étudiant

Youba Bouanani - 300150296



\## Déploiement Nginx avec Ansible



\### Structure

300150296/

├── inventory.ini

├── playbook.yml

└── files/

└── index.html
### Exécution

```bash

ansible-playbook -i inventory.ini playbook.yml

```



\### Résultat

Nginx installé et configuré automatiquement avec page personnalisée.



\### Test

```bash

curl http://10.7.237.232

```

