9️⃣ Ansible – Déploiement automatisé Nginx
👤 Informations étudiant

Champ	Détails

Nom	GACEM OUAIL
Matricule	300148094
Cours	INF1102

🎯 Objectif
Créer un système automatisé qui :

Installe nginx
Déploie une page web
Active le service

📁 Structure
300148094/ ├── inventory.ini ├── playbook.yml └── files/ └── index.html

🚀 Exécution
ansible-playbook -i inventory.ini playbook.yml

🧠 Questions
Ansible est idempotent car il vérifie l'état avant d'agir.
present = installer, started = démarrer le service.
become: yes = exécuter avec les droits sudo.

✅ Réalisations

Étape	Status
inventory.ini créé	✅
playbook.yml créé	✅
files/index.html créé	✅
