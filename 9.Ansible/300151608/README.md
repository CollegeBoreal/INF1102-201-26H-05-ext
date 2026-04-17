9️⃣ Ansible – Déploiement automatisé Nginx
👤 Informations étudiant

Champ	Détails
Nom	Mohammed Aiche
Matricule	300151608
Cours	INF1102 – Programmation de systèmes
🎯 Objectif





Créer un système automatisé avec Ansible qui permet de :

Installer Nginx automatiquement
Déployer une page web personnalisée
Démarrer et activer le service



📁 Structure du projet
300151608/
├── inventory.ini
├── playbook.yml
└── files/
    └── index.html



    
🚀 Exécution
ansible-playbook -i inventory.ini playbook.yml


🧠 Concepts clés
Idempotence : Ansible vérifie l’état avant d’exécuter une action
present : assure l’installation du paquet
started : démarre le service
become: yes : exécution avec privilèges administrateur (sudo)



✅ Réalisations
Étape	Statut
inventory.ini créé	✅
playbook.yml créé	✅
files/index.html créé	✅

