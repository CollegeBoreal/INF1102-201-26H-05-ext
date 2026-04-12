# Ansible - Deploiement Nginx

**Etudiant :** Imad Boudeuf
**Numero :** 300152410
**Cours :** INF1102-201-26H-05

## Objectif
Deployer automatiquement Nginx avec Ansible.

## Structure
300152410/
├── inventory.ini
├── playbook.yml
└── files/
└── index.html

## Execution
```bash
ansible-playbook -i inventory.ini playbook.yml
```

## Verification
```bash
curl http://10.7.237.245
```

## Reponses aux questions

### Pourquoi Ansible est idempotent ?
Ansible peut executer plusieurs fois le meme playbook sans modifier
le systeme si l'etat desire est deja atteint.

### Difference entre present et started
- present : assure qu'un paquet est installe
- started : assure qu'un service est en cours d'execution

### Pourquoi utiliser become: yes ?
Pour executer les taches avec des privileges administrateur.