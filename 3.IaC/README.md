# 🏗️ Infrastructure as Code (IaC)

| #️⃣ | Participations | Vérifications |
|-|-|-| 
| 🥇 | [:tada: Participation](.scripts/Participation-group1.md) | [:checkered_flag: Vérification](.scripts/Check-group1.md) |
| 🥈 | [:tada: Participation](.scripts/Participation-group2.md) | [:checkered_flag: Vérification](.scripts/Check-group2.md) |

## 1. Introduction

Traditionnellement, l’administration des systèmes se faisait **manuellement** :

* installation à la main
* configurations faites “à la souris”
* documentation incomplète
* environnements difficiles à reproduire

👉 **Problème majeur** :

> *“Ça marche sur ce serveur, mais pas sur l’autre.”*

### Solution moderne : Infrastructure as Code (IaC)

L’**Infrastructure as Code** consiste à **décrire, déployer et gérer une infrastructure informatique à l’aide de code**, plutôt que par des actions manuelles.

---

## 2. Définition

> **Infrastructure as Code (IaC)** est une approche de programmation système qui permet de gérer les ressources informatiques (serveurs, réseaux, services, utilisateurs, stockage) à l’aide de fichiers de configuration versionnés et exécutables automatiquement.

---

## 3. Où se situe l’IaC en programmation système ?

### Position dans la pile système

```
Applications
──────────────
Services (Web, DB, DNS, AD, Containers)
──────────────
Infrastructure as Code (IaC)
──────────────
Shell / API OS / Hyperviseur / Cloud
──────────────
Noyau (Linux / Windows)
──────────────
Matériel
```

👉 L’IaC :

* **ne programme pas le noyau**
* **programme le système et son infrastructure**
* agit via des **API, des services système et des hyperviseurs**

---

## 4. Pourquoi utiliser l’IaC ?

### Problèmes sans IaC

* erreurs humaines
* incohérences entre serveurs
* déploiements lents
* documentation non fiable

### Avantages de l’IaC

| Avantage         | Description                            |
| ---------------- | -------------------------------------- |
| Reproductibilité | Même infrastructure, partout           |
| Automatisation   | Déploiement sans intervention manuelle |
| Versionnement    | Git = historique, rollback             |
| Fiabilité        | Moins d’erreurs humaines               |
| Rapidité         | Déploiement en minutes                 |
| Auditabilité     | Tout est traçable                      |

---

## 5. IaC vs scripts système classiques

### Scripts système (bash / PowerShell)

```bash
apt update
apt install nginx
systemctl start nginx
```

* impératif
* dépend de l’ordre
* difficile à maintenir

### IaC (déclaratif)

```hcl
resource "nginx_server" {
  version = "1.24"
  port    = 80
}
```

* déclaratif
* décrit **l’état final**
* l’outil décide *comment* y arriver

---

## 6. Approches de l’IaC

### 6.1 IaC déclaratif

> *Voici l’état voulu*

* Terraform / OpenTofu
* CloudFormation
* Kubernetes YAML

✔ recommandé
✔ reproductible
✔ idempotent

---

### 6.2 IaC impératif

> *Fais ceci, puis cela*

* Scripts shell
* Ansible (mixte)

✔ flexible
✖ plus complexe à maintenir

---

## 7. Que peut-on gérer avec l’IaC ?

* Machines virtuelles
* Réseaux (VLAN, bridges, firewall)
* Stockage
* Utilisateurs et permissions
* Services (web, DB, DNS)
* Containers
* Clusters
* Infrastructure cloud
* Infrastructure locale (Proxmox, VMware)

👉 **L’infrastructure devient un programme.**

---

## 8. Outils IaC courants

### Outils d’orchestration

* **Terraform / OpenTofu**
* CloudFormation
* Pulumi

### Outils de configuration

* Ansible
* Puppet
* Chef

### Plateformes ciblées

* Proxmox
* AWS / Azure / GCP
* Kubernetes

---

## 9. Exemple simple (conceptuel)

### Objectif

> Créer automatiquement une VM Linux avec un serveur web.

### Étapes IaC

1. Définir la VM
2. Allouer CPU / RAM
3. Créer le réseau
4. Installer le service web
5. Exposer le port

👉 **Une seule commande** :

```bash
tofu apply
```

---

## 10. IaC et bonnes pratiques

* Infrastructure versionnée (Git)
* Pas de modification manuelle en production
* Séparation dev / test / prod
* Variables et secrets sécurisés
* Documentation = code

---

## 11. IaC et DevOps

L’IaC est un **pilier du DevOps** :

* CI/CD
* déploiement continu
* scalabilité
* résilience
* SRE

👉 Sans IaC, **le DevOps n’est pas viable à grande échelle**.

---

## 12. Place de l’IaC dans le cours

### Prérequis recommandés

* Linux / Windows
* Bash / PowerShell
* Réseaux
* Virtualisation

### Position idéale dans la session

1. Scripts système
2. Services et démons
3. Virtualisation
4. **Infrastructure as Code**
5. Orchestration avancée

---

## 13. Objectifs pédagogiques

À la fin de cette leçon, l’étudiant(e) sera capable de :

* expliquer le concept d’IaC
* distinguer script système et IaC
* décrire une infrastructure de manière déclarative
* utiliser un outil IaC de base
* automatiser un déploiement système

---

## 14. Phrase de conclusion

> **L’Infrastructure as Code transforme l’administration système en une discipline de programmation structurée, reproductible et industrielle.**

# :b: Expérimentation

### 🎛️ Créer un fichier dans ce répertoire `(3.IaC)`:

:checkered_flag: Finalement,

- [ ] Créer un répertoire avec :id: (votre identifiant boreal)
   - [ ] `mkdir ` :id:
- [ ] dans votre répertoire ajouter le fichier `README.md`
  - [ ] `nano `README.md
- [ ] envoyer vers le serveur `github.com`
  - [ ] `cd ..`
  - [ ] `git add `:id: 
  - [ ] `git commit -m "mon fichier ..."`
  - [ ] `git push`

- [ ] Se diriger vers le répertoire avec :id: (votre identifiant boreal)
   - [ ] `cd ` :id:

- [ ] Continuer les 🔄 Exercices 

### 🔄 Exercices

<img src=images/Proxmox-INF1102.png width='50%' height='50%' > </img>


OpenTofu works **almost exactly like Terraform**, and Proxmox VE 7 is well-supported via the **Telmate Proxmox provider**.

Below is a **minimal, working, PVE-7-friendly workflow**.

#### 1️⃣ Install OpenTofu

On your workstation:

- [ ] Windows 🪟

```bash
choco install opentofu
```

- [ ] Mac 🍎

```bash
brew install opentofu
```

Verify:

```bash
tofu version
```
```lua
OpenTofu v1.11.3
on darwin_arm64
+ provider registry.opentofu.org/telmate/proxmox v2.9.14
```

---

#### 2️⃣ Create project structure


Go to your directory :id:

- [ ] Sur bash 🐧

```bash
touch provider.tf main.tf variables.tf terraform.tfvars
```

- [ ] Sur Powershell 🪟

```powershell
New-Item provider.tf, main.tf, variables.tf, terraform.tfvars -ItemType File
```

---

#### 3️⃣ Provider configuration (`provider.tf`)

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
  pm_api_url      = var.pm_url
  pm_api_token_id = var.pm_token_id
  pm_api_token_secret = var.pm_token_secret
  pm_tls_insecure = true
}
```

---

#### 4️⃣ VM resource (Cloud-Init VM) (`main.tf`)

Example **Ubuntu VM** cloned from a template:

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

  os_type = "cloud-init"

  ipconfig0 = var.pm_ipconfig0
  nameserver = var.pm_nameserver

  ciuser  = "ubuntu"
  sshkeys = <<EOF
   ${file("~/.ssh/ma_cle.pub")}
   ${file("~/.ssh/cle_publique_du_prof.pub")}
  EOF
}
```

---

#### 5️⃣ Variables (`variables.tf`)

```hcl
variable "pm_vm_name" {
  type = string
}

variable "pm_ipconfig0" {
  type = string
}

variable "pm_nameserver" {
  type = string
}

variable "pm_url" {
  type = string
}

variable "pm_token_id" {
  type = string
}

variable "pm_token_secret" {
  type      = string
  sensitive = true
}
```

---

#### 6️⃣ Secrets (`terraform.tfvars`)

```hcl
pm_vm_name      = "vm300xxxxxx"
pm_ipconfig0    = "ip=10.7.237.xxx/23,gw=10.7.237.1"
pm_nameserver   = "10.7.237.3"
pm_url          = "https://10.7.237.xx:8006/api2/json"
pm_token_id     = "tofu@pve!opentofu"
pm_token_secret = "4fa24fc3-bd8c-4916-ba6e-09xxxxxxx3b00"
```

⚠️ **Do not commit this file**

---

#### 7️⃣ Initialize & apply

```bash
tofu init
tofu plan
tofu apply
```

Type `yes`.

🎉 VM will appear in Proxmox.

---

#### 8️⃣ Test VM

- [ ] 🐧 Linux

```lua
ssh -i ~/.ssh/ma_cle.pk \
  -o StrictHostKeyChecking=no \
  -o UserKnownHostsFile=/tmp/ssh_known_hosts_empty \
  ubuntu@10.7.237.xxx
```

- [ ] 🪟 Powershell

```powershell
ssh -i ~/.ssh/ma_cle.pk `
  -o StrictHostKeyChecking=no `
  -o UserKnownHostsFile=/tmp/ssh_known_hosts_empty `
  ubuntu@10.7.237.xxx
```


# :books: References

| Cle du prof                     |
|---------------------------------|
| nano ~/.ssh/cle_publique_du_prof.pub |

- [ ] Copier dans le fichier ci-dessus

```lua
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD2pLhMqFGKffSdYvNCMAyM7598oBY+m/3q5AMXmb7IE6vq42+yGzqEUzZu9WrFckFD4Hq52rIU5DeOvi83DCF3uroXjNTEtCKdi+tY7cV18bHmsDsBHMqTnpuvroofgFWA0Pi++b2kGW2I5eyy1Qjv5rOp7y11Xe6XeZFEz7qQO1/xNiBMJEruG9Xldgooe4hkaOF39qnbqD4ui3LxYaTUTEulstw4wN70dSB8Zu9YQP7A7KU2zIEwJ1aw8whfO1CAM/AVvoDyqMtV8VXoaZSHOBgluMtinQfyyt473S2ZZeJlnmhK0F1gdOhO4SVZNRMj96m30ryYkYBFWvvLRP5N b300098957@ramena
```

---

##  Prereqs on Proxmox (PVE 7) (Déjâ fait sur le serveur)

### ✔ Enable API access

You need either:

* a **user + password**, or
* **API token** (recommended)

**Recommended (API token):**

```bash
pveum user add tofu@pve
pveum aclmod / -user tofu@pve -role Administrator
pveum user token add tofu@pve opentofu --privsep 0
```

Save:

* **Token ID**: `tofu@pve!opentofu`
* **Token Secret**: (shown once)

---

### ✔ Create VM Template (cloud-init_template.sh)

```lua
#!/bin/bash

VMID=9000
IMG="jammy-server-cloudimg-amd64.img"

# 🔧 PARAMÈTRE STORAGE
STORAGE=${1:-local-zfs}

echo "➡️ Storage utilisé : $STORAGE"

# Delete VM if exists
if qm status $VMID &>/dev/null; then
    echo "VM $VMID existe → suppression..."
    qm destroy $VMID --purge
fi

# Download image
wget -O $IMG https://cloud-images.ubuntu.com/jammy/current/$IMG

# Create VM
qm create $VMID \
  --name ubuntu-jammy-template \
  --memory 2048 \
  --cores 2 \
  --net0 virtio,bridge=vmbr0

# Import disk
qm importdisk $VMID $IMG $STORAGE

# Attach disk
qm set $VMID --scsihw virtio-scsi-pci --scsi0 $STORAGE:vm-$VMID-disk-0

# Cloud-init disk
qm set $VMID --ide2 $STORAGE:cloudinit

# Boot settings
qm set $VMID --boot c --bootdisk scsi0
qm set $VMID --serial0 socket --vga serial0

# Network (DHCP)
qm set $VMID --ipconfig0 ip=dhcp

# Convert to template
qm template $VMID
```

---

# 🔍 2. Voir ton storage actuel

```bash id="8xqk1a"
pvesm status
```

Tu verras un truc comme :

* local-lvm ❌ (pas chez toi)
* local-zfs ✔️ (ton cas actuel)

---

```bash
bash cloud-init_template.sh local-zfs
bash cloud-init_template.sh local-lvm
```

## ✅ Script universel (ZFS ou LVM)

---

# ⚡ 5. Résumé simple

| Type Proxmox | STORAGE à utiliser |
| ------------ | ------------------ |
| ZFS          | `local-zfs` ✔️     |
| LVM          | `local-lvm` ✔️     |

---

# 💡 6. TON CAS (important)

D’après ton setup :

```text id="7k9xpd"
raidz1 → ZFS
```

👉 donc tu dois utiliser :

```bash id="z9d2mf"
STORAGE="local-zfs"
```

---

# 🏁 Conclusion

✔️ script paramétrable = meilleure pratique
✔️ ZFS chez toi → `local-zfs`
✔️ LVM ailleurs → `local-lvm`
✔️ une seule variable = zéro erreur


## 🏗️ Installation

- [ ] [💻 Proxmox VE Installation – HP ProLiant DL360 G6](https://github.com/CollegeBoreal/Laboratoires/tree/main/D.DC/S.Servers/Proliant/Proxmox)
