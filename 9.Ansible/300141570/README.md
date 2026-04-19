- name: Installer et configurer nginx
  hosts: web
  become: yes
  tasks:
    - name: Installer nginx
      apt:
        name: nginx
        state: present
        update_cache: yes

    - name: Copier la page HTML
      copy:
        src: files/index.html
        dest: /var/www/html/index.nginx-debian.html

    - name: Démarrer nginx
      service:
        name: nginx
        state: started
        enabled: yes
🌐 Page HTML
<h1>Déploiement réussi avec Ansible</h1>
▶️ Exécution
ansible-playbook -i inventory.ini playbook.yml
🧪 Vérification
curl http://10.7.237.226/index.nginx-debian.html
📸 Capture

🧠 Réponses

1. Pourquoi Ansible est idempotent ?
Ansible applique l’état souhaité sans répéter une action déjà effectuée.

2. Différence entre present et started ?
present : le paquet est installé
started : le service est démarré

3. Pourquoi utiliser become: yes ?
Permet d’exécuter les tâches avec privilèges administrateur.

🚀 Conclusion

Ce TP montre comment utiliser Ansible pour automatiser la configuration d’un serveur web avec nginx de manière fiable et reproductible.
![Déploiement réussi](images/1.png)
