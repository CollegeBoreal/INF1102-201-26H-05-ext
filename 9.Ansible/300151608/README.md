📁 Structure du projet
300151608/Mohammed aiche
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
