# TP - Déploiement automatisé Nginx avec Ansible

## Informations générales

- **Cours** : INF1102 - Gestion de configuration avec Ansible (IaC)
- **Étudiant** : 300150395
- **Sujet** : Déploiement automatisé d'un site web statique avec Nginx et Ansible

## Objectif du TP

Ce travail a pour objectif de mettre en pratique **Ansible** comme outil de **gestion de configuration** dans une approche **Infrastructure as Code (IaC)**. Le but principal est d'automatiser le déploiement d'un serveur web **Nginx** ainsi que la publication d'un site statique composé de fichiers **HTML, CSS et JavaScript**.

À la fin du TP, le système doit être capable de :

- Installer automatiquement **nginx** ;
- Copier les fichiers du site web vers le serveur distant ;
- Démarrer et activer le service **nginx** ;
- Rendre le site accessible à partir d'un navigateur.

## Structure du projet

La structure utilisée pour ce TP est la suivante :

```text
300150395/
├── inventory.ini
├── playbook.yml
└── files/
    ├── index.html
    ├── style.css
    └── script.js
```

## Description des fichiers

### `inventory.ini`

Ce fichier permet de décrire la machine cible sur laquelle Ansible doit exécuter les tâches.

```ini
[web]
10.7.237.233 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/id_rsa
```

### `playbook.yml`

Le playbook contient les tâches d'automatisation exécutées par Ansible.

Il permet de :

- mettre à jour le cache APT ;
- installer **nginx** ;
- copier les fichiers du site (`index.html`, `style.css`, `script.js`) ;
- démarrer le service nginx ;
- activer nginx au démarrage du système.

### `files/index.html`, `files/style.css`, `files/script.js`

Ces trois fichiers constituent le site web statique déployé par le playbook.

- **index.html** : structure du site ;
- **style.css** : apparence graphique ;
- **script.js** : comportements dynamiques et effets côté client.

## Exécution du playbook

La commande utilisée pour lancer le déploiement est la suivante :

```bash
ansible-playbook -i inventory.ini playbook.yml
```

Cette commande exécute toutes les tâches décrites dans le playbook sur la machine définie dans l'inventaire.

## Vérification du déploiement

Après l'exécution du playbook, la vérification a été faite de deux façons :

### 1. Vérification via Ansible

Le récapitulatif montre que les tâches ont été exécutées correctement :

- `ok=4`
- `changed=1`
- `unreachable=0`
- `failed=0`

Cela confirme que la machine cible a bien reçu la configuration demandée.

### 2. Vérification via navigateur

Le site a ensuite été testé dans le navigateur avec l'adresse suivante :

```text
http://10.7.237.233
```

L'affichage du site confirme que le déploiement automatique a réussi.

## Réponses aux questions théoriques

### Pourquoi Ansible est-il idempotent ?

Ansible est dit **idempotent** parce qu'il peut exécuter plusieurs fois le même playbook sans modifier inutilement le système si l'état désiré est déjà atteint. Par exemple, si **nginx** est déjà installé et démarré, Ansible ne refera pas l'installation de manière inutile.

### Différence entre `present` et `started`

- **`present`** : assure qu'un paquet ou une ressource est installé(e) ou existe ;
- **`started`** : assure qu'un service est en cours d'exécution.

Ainsi, `present` agit sur l'existence du paquet, tandis que `started` agit sur l'état du service.

### Pourquoi utiliser `become: yes` ?

`become: yes` permet d'exécuter les tâches avec des privilèges administrateur. Cela est nécessaire pour :

- installer des paquets ;
- écrire dans `/var/www/html/` ;
- démarrer ou redémarrer un service système comme nginx.

## Difficultés rencontrées

Pendant la réalisation du TP, plusieurs problèmes ont été rencontrés :

- erreur de chemin lors de l'exécution du playbook depuis le mauvais dossier ;
- problème de clé SSH dans `inventory.ini` ;
- erreurs de syntaxe YAML dans `playbook.yml` ;
- ancien site encore affiché dans le navigateur à cause du cache ;
- absence des fichiers `style.css` et `script.js` au moment du déploiement.

Ces problèmes ont été corrigés progressivement, ce qui a permis d'obtenir un déploiement fonctionnel.

## Résultat final

Le résultat final est un site statique moderne déployé automatiquement avec **Ansible** sur un serveur **Nginx**. Le site présente le sujet du TP, soit la gestion de configuration avec Ansible et l'approche Infrastructure as Code.

Ce projet démontre qu'Ansible permet de :

- automatiser la configuration d'un serveur ;
- reproduire facilement un déploiement ;
- simplifier l'administration système ;
- réduire les erreurs manuelles.

## Captures d'écran

### Figure 1 - Exécution du playbook Ansible

![Figure 1 - Exécution du playbook](images/1.jpg)

### Figure 2 - Contenu du fichier inventory.ini

![Figure 2 - Fichier inventory.ini](images/2.jpg)

### Figure 3 - Résultat du site web dans le navigateur

![Figure 3 - Site déployé dans le navigateur](images/3.jpg)

## Conclusion

Ce TP m'a permis de comprendre concrètement comment **Ansible** peut être utilisé pour automatiser le déploiement et la configuration d'un serveur web. J'ai appris à utiliser un inventaire, à écrire un playbook YAML, à copier des fichiers vers une machine distante et à gérer le service nginx.

Cette activité m'a aussi permis de mieux comprendre la différence entre une approche manuelle et une approche déclarative. Grâce à Ansible, le déploiement devient plus rapide, plus fiable, plus structuré et plus reproductible.
