# 🏗️ Infrastructure as Code (IaC) — OpenTofu + Proxmox By #Calvin 300152131

> **Cours : Programmation des Systèmes**  
> **Environnement :** Ubuntu 22.04 / PowerShell  
> **Outils :** OpenTofu, Proxmox VE 7

---

## 📋 Table des matières

1. [Résumé théorique](#résumé-théorique)
2. [Expérimentation – Mise en place](#expérimentation--mise-en-place)
3. [Étape 1 – Installer OpenTofu](#étape-1--installer-opentofu)
4. [Étape 2 – Structure du projet](#étape-2--structure-du-projet)
5. [Étape 3 – Configuration du provider](#étape-3--configuration-du-provider-providertf)
6. [Étape 4 – Ressource VM](#étape-4--ressource-vm-maintf)
7. [Étape 5 – Variables](#étape-5--variables-variablestf)
8. [Étape 6 – Secrets](#étape-6--secrets-terraformtfvars)
9. [Étape 7 – Initialiser et appliquer](#étape-7--initialiser-et-appliquer)
10. [Étape 8 – Tester la VM](#étape-8--tester-la-vm)
11. [Résultats](#résultats)

---

## 📖 Résumé théorique

L'**Infrastructure as Code (IaC)** est une approche moderne qui consiste à gérer les ressources informatiques (serveurs, réseaux, services, utilisateurs) à l'aide de **fichiers de configuration versionnés**, plutôt que par des actions manuelles.

| Approche classique | Approche IaC |
|---|---|
| Installation manuelle | Déploiement automatisé |
| Configuration "à la souris" | Code versionné sur Git |
| Environnements difficiles à reproduire | Reproductibilité totale |
| Documentation incomplète | Le code = la documentation |

L'IaC se positionne entre le shell/API OS et les services applicatifs. Elle est un **pilier du DevOps** : sans IaC, le déploiement continu à grande échelle n'est pas viable.

> *"L'Infrastructure as Code transforme l'administration système en une discipline de programmation structurée, reproductible et industrielle."*

---

## Étape 1 – Installer OpenTofu

**Windows 🪟**
```powershell
choco install opentofu
```

**Mac 🍎**
```bash
brew install opentofu
```

Vérifier l'installation :

```bash
tofu version
```

---

## Étape 2 – Structure du projet

**Linux 🐧**
```bash
touch provider.tf main.tf variables.tf terraform.tfvars
```

**PowerShell 🪟**
```powershell
New-Item provider.tf, main.tf, variables.tf, terraform.tfvars -ItemType File
```

Structure finale :
```
🆔/
├── provider.tf        # Configuration du provider Proxmox
├── main.tf            # Définition de la VM
├── variables.tf       # Déclaration des variables
└── terraform.tfvars   # Valeurs secrètes (ne pas committer !)
```

---

## Étape 3 – Configuration du provider (`provider.tf`)

```hcl
terraform {
  required_providers {
    proxmox = {
      source  = "telmate/proxmox"
      version = ">= 2.9.0"
    }
  }
}

provider "proxmox" {
  pm_api_url          = var.pm_url
  pm_api_token_id     = var.pm_token_id
  pm_api_token_secret = var.pm_token_secret
  pm_tls_insecure     = true
}
```

---

## Étape 4 – Ressource VM (`main.tf`)

VM Ubuntu clonée depuis un template Cloud-Init :

```hcl
resource "proxmox_vm_qemu" "vm1" {
  name        = var.pm_vm_name
  target_node = "labinfo"
  clone       = "ubuntu-jammy-template"
  full_clone  = false

  cores   = 2
  sockets = 1
  memory  = 2048

  scsihw = "virtio-scsi-pci"

  disk {
    size    = "10G"
    type    = "scsi"
    storage = "local-lvm"
  }

  network {
    model  = "virtio"
    bridge = "vmbr0"
  }

  os_type    = "cloud-init"
  ipconfig0  = var.pm_ipconfig0
  nameserver = var.pm_nameserver

  ciuser  = "ubuntu"
  sshkeys = <<EOF
  ${file("~/.ssh/ma_cle.pub")}
  ${file("~/.ssh/cle_publique_du_prof.pub")}
  EOF
}
```

---

## Étape 5 – Variables (`variables.tf`)

```hcl
variable "pm_vm_name"      { type = string }
variable "pm_ipconfig0"    { type = string }
variable "pm_nameserver"   { type = string }
variable "pm_url"          { type = string }
variable "pm_token_id"     { type = string }
variable "pm_token_secret" {
  type      = string
  sensitive = true
}
```

---

## Étape 6 – Secrets (`terraform.tfvars`)

```hcl
pm_vm_name      = "vm300xxxxxx"
pm_ipconfig0    = "ip=10.7.237.xxx/23,gw=10.7.237.1"
pm_nameserver   = "10.7.237.3"
pm_url          = "https://10.7.237.xx:8006/api2/json"
pm_token_id     = "tofu@pve!opentofu"
pm_token_secret = "4fa24fc3-bd8c-4916-ba6e-09xxxxxxx3b00"
```

> ⚠️ **Ne jamais committer ce fichier sur GitHub !** Ajouter `terraform.tfvars` dans le `.gitignore`.

---

## Étape 7 – Initialiser et appliquer

```bash
tofu init
tofu plan
tofu apply
```

Taper `yes` pour confirmer. La VM apparaîtra dans Proxmox. 🎉

---

## Étape 8 – Tester la VM

**Linux 🐧**
```bash
ssh -i ~/.ssh/ma_cle.pk \
  -o StrictHostKeyChecking=no \
  -o UserKnownHostsFile=/tmp/ssh_known_hosts_empty \
  ubuntu@10.7.237.xxx (242)
```

**PowerShell 🪟**
```powershell
ssh -i ~/.ssh/ma_cle.pk `
  -o StrictHostKeyChecking=no `
  -o UserKnownHostsFile=/tmp/ssh_known_hosts_empty `
  ubuntu@10.7.237.xxx
```

---

## ✅ Résultats

### 📸 VM créée dans Proxmox

![VM créée dans Proxmox](images/VM100%20CREE%20Proxmox.png)

### 📸 Connexion SSH à la VM via PowerShell

![Connexion SSH à la VM](images/connexion%20a%20la%20vm%20ssh.png)

---

*TP réalisé dans le cadre du cours de Programmation des Systèmes*
