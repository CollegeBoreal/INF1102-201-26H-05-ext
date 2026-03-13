## Preuve d'exécution
- VM créée sur Proxmox (node labinfo)
- VM ID: 103
- Nom: vm300152260
- Statut: Running

# IaC - OpenTofu / Proxmox

## Étudiant
- ID Boréal: 300152260

## Objectif
Créer une VM Ubuntu sur Proxmox avec OpenTofu (IaC).

## Résultat
- VM créée avec succès
- Proxmox Node: labinfo
- Proxmox VMID: 103
- Nom VM: vm300152260
- Statut: Running

## Paramètres (sans secrets)
pm_vm_name   = "vm300152260"  
pm_ipconfig0 = "ip=10.7.237.243/23,gw=10.7.237.1"  
pm_nameserver= "10.7.237.3"  
pm_url       = "https://10.7.237.38:8006/api2/json"  
pm_token_id  = "tofu@pve!opentofu"  

