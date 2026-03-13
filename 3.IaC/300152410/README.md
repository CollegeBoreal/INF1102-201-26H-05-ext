# INF1102 – Proxmox VM avec OpenTofu

**Nom :** Imad Boudeuf  
**ID :** 300152410  
**Repo GitHub :** imadboud / INF1102-Proxmox-OpenTofu

## Commandes utilisées
- tofu init
- tofu plan
- tofu apply

## Résumé
VM créée sur Proxmox avec Cloud-Init (template Ubuntu Jammy) et configuration IP via `ipconfig0`.

## Sécurité
Le fichier `terraform.tfvars` n’est pas versionné (token secret).
Un exemple est fourni : `terraform.tfvars.example`.

## Preuve (capture)
Ajouter une capture dans le dossier `images/`.
## Capture VM

![VM](images/vm.jpeg)

