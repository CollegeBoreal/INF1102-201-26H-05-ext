# INF1102 – Infrastructure as Code avec OpenTofu & Proxmox

##  Étudiant
Syphax Ouadfel    
Projet : Déploiement d'une VM avec OpenTofu sur Proxmox VE 7  

##  Objectif du laboratoire

L’objectif de ce laboratoire était de :

- Utiliser OpenTofu (Infrastructure as Code)
- Se connecter à l’API Proxmox via un token
- Déployer automatiquement une machine virtuelle Ubuntu
- Utiliser Cloud-Init
- Injecter des clés SSH
- Vérifier l’accès à la VM via SSH et navigateur

##  Technologies utilisées

- OpenTofu v1.11.x
- Proxmox VE 7.4
- Provider Telmate/Proxmox v2.9.x
- Ubuntu 22.04 LTS (cloud image)
- Cloud-Init
- SSH (clé ed25519)

## Configuration

### Provider Proxmox

Connexion via API Token :

- URL : `https://10.7.237.38:8006/api2/json`
- Token ID : `tofu@pve!opentofu`
- Authentification sécurisée via token secret
- Option `pm_tls_insecure = true` activée (certificat auto-signé)


##Machine virtuelle déployée

- Nom : `vm300151233`
- Node : `labinfo`
- Template : `ubuntu-jammy-template`
- CPU : 2 cores
- RAM : 2048 MB
- Disque : 10G (local-lvm)
- Réseau : vmbr0
- IP statique : `10.7.237.235`

## Injection des clés SSH

Deux clés ont été injectées via Cloud-Init :

- Ma clé publique : `id_ed25519.pub`
- Clé publique du professeur

Configuration utilisée :

```hcl
sshkeys = <<EOF
${file("C:\\Users\\PC\\.ssh\\id_ed25519.pub")}
${file("C:\\Users\\PC\\.ssh\\cle_publique_du_prof.pub")}
EOF
🚀 Déploiement

Commandes exécutées :
tofu init
tofu plan
tofu apply
                       Résultat :                  Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
✅ Validation du fonctionnement
1️⃣ Accès SSH réussi        ssh ubuntu@10.7.237.235
2️⃣ VM visible dans Proxmox          La machine virtuelle apparaît correctement dans l’interface Web Proxmox.

🏁 Conclusion

Ce laboratoire démontre la capacité à :

- Automatiser le déploiement d’une infrastructure
- Interagir avec une API via token sécurisé
-Configurer une VM cloud-ready
- Gérer l’accès sécurisé via SSH
- L’objectif du laboratoire a été atteint avec succès.
