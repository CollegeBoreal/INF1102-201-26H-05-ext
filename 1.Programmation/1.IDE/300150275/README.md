# INF1102 – Configuration IDE et Git

## Validation de la configuration Git

### Vérification de l'authentification SSH

Commande utilisée :

ssh -T git@github.com

Résultat attendu :

Hi Tarik-n! You've successfully authenticated.

---

## Clonage du dépôt

Commande utilisée :

git clone https://github.com/CollegeBoreal/INF1102-201-26H-05.git

---

## Vérification du dépôt

Se placer dans le dossier du projet :

cd INF1102-201-26H-05

Vérifier l’état du dépôt :

git status

Résultat :

On branch main  
Your branch is up to date with 'origin/main'.

---

## Ajout et envoi d’un fichier

Ajouter un fichier :

git add README.md

Créer un commit :

git commit -m "Ajout README IDE"

Envoyer sur GitHub :

git push

---

## Validation

Le dépôt est correctement configuré.  
Les modifications sont envoyées sur GitHub sans erreur.