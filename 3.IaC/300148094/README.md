# 📘 Infrastructure as Code (IaC)

> **Nom :** Ouail Gacem  
> **Matricule :** 300148094  
> **Cours :** Programmation système — Administration moderne

---

## 📋 Table des matières

1. [Introduction](#introduction)
2. [Définition](#définition)
3. [Position dans la pile système](#position-dans-la-pile-système)
4. [Pourquoi utiliser l'IaC ?](#pourquoi-utiliser-liac)
5. [IaC vs Scripts classiques](#iac-vs-scripts-classiques)
6. [Approches de l'IaC](#approches-de-liac)
7. [Ce qu'on peut gérer](#ce-quon-peut-gérer)
8. [Outils courants](#outils-courants)
9. [Exercices pratiques — OpenTofu + Proxmox](#exercices-pratiques--opentofu--proxmox)
10. [Bonnes pratiques](#bonnes-pratiques)
11. [IaC et DevOps](#iac-et-devops)
12. [Objectifs pédagogiques](#objectifs-pédagogiques)

---

## Introduction

Traditionnellement, l'administration des systèmes se faisait **manuellement** :

- Installation à la main
- Configurations faites "à la souris"
- Documentation incomplète
- Environnements difficiles à reproduire

> ⚠️ **Problème majeur :** *"Ça marche sur ce serveur, mais pas sur l'autre."*

**Solution moderne → Infrastructure as Code (IaC)**

---

## Définition

**Infrastructure as Code (IaC)** est une approche de programmation système qui permet de gérer les ressources informatiques (serveurs, réseaux, services, utilisateurs, stockage) à l'aide de **fichiers de configuration versionnés** et exécutables automatiquement.

---

## Position dans la pile système

```
Applications
──────────────────────────
Services (Web, DB, DNS, AD, Containers)
──────────────────────────
Infrastructure as Code (IaC)   ◀️ Notre niveau
──────────────────────────
Shell / API OS / Hyperviseur / Cloud
──────────────────────────
Noyau (Linux / Windows)
──────────────────────────
Matériel
```

> L'IaC agit via des **API**, des **services système** et des **hyperviseurs** — sans toucher au noyau.

---

## Pourquoi utiliser l'IaC ?

### ❌ Sans IaC

| Problème | Impact |
|----------|--------|
| Erreurs humaines | Configurations incorrectes |
| Incohérences entre serveurs | Environnements instables |
| Déploiements lents | Perte de temps |
| Documentation non fiable | Difficile à reproduire |

### ✅ Avec IaC

| Avantage | Description |
|----------|-------------|
| **Reproductibilité** | Même infrastructure, partout |
| **Automatisation** | Déploiement sans intervention manuelle |
| **Versionnement** | Git = historique + rollback |
| **Fiabilité** | Moins d'erreurs humaines |
| **Rapidité** | Déploiement en minutes |
| **Auditabilité** | Tout est traçable |

---

## IaC vs Scripts classiques

### Scripts système (impératif)

```bash
apt update
apt install nginx
systemctl start nginx
```

- Dépend de l'ordre d'exécution
- Difficile à maintenir
- Non idempotent

### IaC (déclaratif)

```hcl
resource "nginx_server" {
  version = "1.24"
  port    = 80
}
```

- Décrit l'**état final** souhaité
- L'outil décide comment y arriver
- Idempotent ✔️

---

## Approches de l'IaC

### 🟢 Déclaratif (recommandé)

> *"Voici l'état voulu"*

- **Terraform / OpenTofu**
- **CloudFormation**
- **Kubernetes YAML**

✔ Reproductible &nbsp; ✔ Idempotent &nbsp; ✔ Facile à maintenir

### 🟡 Impératif

> *"Fais ceci, puis cela"*

- **Scripts shell**
- **Ansible** (mixte)

✔ Flexible &nbsp; ✖ Plus complexe à maintenir

---

## Ce qu'on peut gérer

- 🖥️ Machines virtuelles
- 🌐 Réseaux (VLAN, bridges, firewall)
- 💾 Stockage
- 👤 Utilisateurs et permissions
- ⚙️ Services (web, DB, DNS)
- 📦 Containers
- 🧩 Clusters
- ☁️ Infrastructure cloud (AWS, Azure, GCP)
- 🏠 Infrastructure locale (Proxmox, VMware)

> 💡 **L'infrastructure devient un programme.**

---

## Outils courants

### Orchestration

| Outil | Usage |
|-------|-------|
| **Terraform / OpenTofu** | Multi-cloud, local |
| **CloudFormation** | AWS natif |
| **Pulumi** | Code natif (Python, JS...) |

### Configuration

| Outil | Usage |
|-------|-------|
| **Ansible** | Agentless, SSH |
| **Puppet** | Agent-based |
| **Chef** | Ruby DSL |

---

## Exercices pratiques — OpenTofu + Proxmox

### 1️⃣ Installation d'OpenTofu

```bash
# Windows
choco install opentofu

# Mac
brew install opentofu

# Vérification
tofu version
```

### 2️⃣ Structure du projet

```bash
touch provider.tf main.tf variables.tf terraform.tfvars
```

```
mon-projet/
├── provider.tf       # Configuration du provider Proxmox
├── main.tf           # Ressource VM
├── variables.tf      # Déclaration des variables
└── terraform.tfvars  # Valeurs (⚠️ Ne pas commiter !)
```

### 3️⃣ provider.tf

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

### 4️⃣ main.tf — VM Cloud-Init

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

  os_type   = "cloud-init"
  ipconfig0 = var.pm_ipconfig0
  nameserver = var.pm_nameserver

  ciuser  = "ubuntu"
  sshkeys = <<EOF
  ${file("~/.ssh/ma_cle.pub")}
  ${file("~/.ssh/cle_publique_du_prof.pub")}
  EOF
}
```

### 5️⃣ variables.tf

```hcl
variable "pm_vm_name"    { type = string }
variable "pm_ipconfig0"  { type = string }
variable "pm_nameserver" { type = string }
variable "pm_url"        { type = string }
variable "pm_token_id"   { type = string }
variable "pm_token_secret" {
  type      = string
  sensitive = true
}
```

### 6️⃣ terraform.tfvars

```hcl
pm_vm_name      = "vm300148094"
pm_ipconfig0    = "ip=10.7.237.xxx/23,gw=10.7.237.1"
pm_nameserver   = "10.7.237.3"
pm_url          = "https://10.7.237.xx:8006/api2/json"
pm_token_id     = "tofu@pve!opentofu"
pm_token_secret = "VOTRE-SECRET-ICI"
```

> ⚠️ **Ne jamais commiter ce fichier dans Git !** Ajouter `terraform.tfvars` au `.gitignore`.

### 7️⃣ Initialisation et déploiement

```bash
tofu init     # Télécharge les providers
tofu plan     # Prévisualise les changements
tofu apply    # Applique (répondre "yes")
```

### 8️⃣ Connexion SSH à la VM

```bash
# Linux / Mac
ssh -i ~/.ssh/ma_cle.pk \
  -o StrictHostKeyChecking=no \
  ubuntu@10.7.237.xxx

# PowerShell (Windows)
ssh -i ~/.ssh/ma_cle.pk `
  -o StrictHostKeyChecking=no `
  ubuntu@10.7.237.xxx
```

---

## Bonnes pratiques

- ✅ **Versionner** toute l'infrastructure avec Git
- ✅ **Ne jamais modifier** manuellement en production
- ✅ **Séparer** les environnements dev / test / prod
- ✅ **Sécuriser** les variables et secrets (`.tfvars` dans `.gitignore`)
- ✅ **La documentation = le code** lui-même

---

## IaC et DevOps

L'IaC est un **pilier fondamental du DevOps** :

```
CI/CD  →  Déploiement continu  →  Scalabilité  →  Résilience  →  SRE
```

> 🔑 *Sans IaC, le DevOps n'est pas viable à grande échelle.*

---

## Objectifs pédagogiques

À la fin de ce module, l'étudiant(e) sera capable de :

- [ ] Expliquer le concept d'IaC
- [ ] Distinguer script système et IaC
- [ ] Décrire une infrastructure de manière déclarative
- [ ] Utiliser OpenTofu pour créer une VM sur Proxmox
- [ ] Automatiser un déploiement système complet

---
# 📘 Infrastructure as Code (IaC)

> **Nom :** Ouail Gacem  
> **Matricule :** 300148094  
> **Cours :** Programmation système — Administration moderne

---

## 📋 Table des matières

1. [Introduction](#introduction)
2. [Définition](#définition)
3. [Position dans la pile système](#position-dans-la-pile-système)
4. [Pourquoi utiliser l'IaC ?](#pourquoi-utiliser-liac)
5. [IaC vs Scripts classiques](#iac-vs-scripts-classiques)
6. [Approches de l'IaC](#approches-de-liac)
7. [Ce qu'on peut gérer](#ce-quon-peut-gérer)
8. [Outils courants](#outils-courants)
9. [Exercices pratiques — OpenTofu + Proxmox](#exercices-pratiques--opentofu--proxmox)
10. [Bonnes pratiques](#bonnes-pratiques)
11. [IaC et DevOps](#iac-et-devops)
12. [Objectifs pédagogiques](#objectifs-pédagogiques)

---

## Introduction

Traditionnellement, l'administration des systèmes se faisait **manuellement** :

- Installation à la main
- Configurations faites "à la souris"
- Documentation incomplète
- Environnements difficiles à reproduire

> ⚠️ **Problème majeur :** *"Ça marche sur ce serveur, mais pas sur l'autre."*

**Solution moderne → Infrastructure as Code (IaC)**

---

## Définition

**Infrastructure as Code (IaC)** est une approche de programmation système qui permet de gérer les ressources informatiques (serveurs, réseaux, services, utilisateurs, stockage) à l'aide de **fichiers de configuration versionnés** et exécutables automatiquement.

---

## Position dans la pile système

```
Applications
──────────────────────────
Services (Web, DB, DNS, AD, Containers)
──────────────────────────
Infrastructure as Code (IaC)   ◀️ Notre niveau
──────────────────────────
Shell / API OS / Hyperviseur / Cloud
──────────────────────────
Noyau (Linux / Windows)
──────────────────────────
Matériel
```

> L'IaC agit via des **API**, des **services système** et des **hyperviseurs** — sans toucher au noyau.

---

## Pourquoi utiliser l'IaC ?

### ❌ Sans IaC

| Problème | Impact |
|----------|--------|
| Erreurs humaines | Configurations incorrectes |
| Incohérences entre serveurs | Environnements instables |
| Déploiements lents | Perte de temps |
| Documentation non fiable | Difficile à reproduire |

### ✅ Avec IaC

| Avantage | Description |
|----------|-------------|
| **Reproductibilité** | Même infrastructure, partout |
| **Automatisation** | Déploiement sans intervention manuelle |
| **Versionnement** | Git = historique + rollback |
| **Fiabilité** | Moins d'erreurs humaines |
| **Rapidité** | Déploiement en minutes |
| **Auditabilité** | Tout est traçable |

---

## IaC vs Scripts classiques

### Scripts système (impératif)

```bash
apt update
apt install nginx
systemctl start nginx
```

- Dépend de l'ordre d'exécution
- Difficile à maintenir
- Non idempotent

### IaC (déclaratif)

```hcl
resource "nginx_server" {
  version = "1.24"
  port    = 80
}
```

- Décrit l'**état final** souhaité
- L'outil décide comment y arriver
- Idempotent ✔️

---

## Approches de l'IaC

### 🟢 Déclaratif (recommandé)

> *"Voici l'état voulu"*

- **Terraform / OpenTofu**
- **CloudFormation**
- **Kubernetes YAML**

✔ Reproductible &nbsp; ✔ Idempotent &nbsp; ✔ Facile à maintenir

### 🟡 Impératif

> *"Fais ceci, puis cela"*

- **Scripts shell**
- **Ansible** (mixte)

✔ Flexible &nbsp; ✖ Plus complexe à maintenir

---

## Ce qu'on peut gérer

- 🖥️ Machines virtuelles
- 🌐 Réseaux (VLAN, bridges, firewall)
- 💾 Stockage
- 👤 Utilisateurs et permissions
- ⚙️ Services (web, DB, DNS)
- 📦 Containers
- 🧩 Clusters
- ☁️ Infrastructure cloud (AWS, Azure, GCP)
- 🏠 Infrastructure locale (Proxmox, VMware)

> 💡 **L'infrastructure devient un programme.**

---

## Outils courants

### Orchestration

| Outil | Usage |
|-------|-------|
| **Terraform / OpenTofu** | Multi-cloud, local |
| **CloudFormation** | AWS natif |
| **Pulumi** | Code natif (Python, JS...) |

### Configuration

| Outil | Usage |
|-------|-------|
| **Ansible** | Agentless, SSH |
| **Puppet** | Agent-based |
| **Chef** | Ruby DSL |

---

## Exercices pratiques — OpenTofu + Proxmox

### 1️⃣ Installation d'OpenTofu

```bash
# Windows
choco install opentofu

# Mac
brew install opentofu

# Vérification
tofu version
```

### 2️⃣ Structure du projet

```bash
touch provider.tf main.tf variables.tf terraform.tfvars
```

```
mon-projet/
├── provider.tf       # Configuration du provider Proxmox
├── main.tf           # Ressource VM
├── variables.tf      # Déclaration des variables
└── terraform.tfvars  # Valeurs (⚠️ Ne pas commiter !)
```

### 3️⃣ provider.tf

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

### 4️⃣ main.tf — VM Cloud-Init

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

  os_type   = "cloud-init"
  ipconfig0 = var.pm_ipconfig0
  nameserver = var.pm_nameserver

  ciuser  = "ubuntu"
  sshkeys = <<EOF
  ${file("~/.ssh/ma_cle.pub")}
  ${file("~/.ssh/cle_publique_du_prof.pub")}
  EOF
}
```

### 5️⃣ variables.tf

```hcl
variable "pm_vm_name"    { type = string }
variable "pm_ipconfig0"  { type = string }
variable "pm_nameserver" { type = string }
variable "pm_url"        { type = string }
variable "pm_token_id"   { type = string }
variable "pm_token_secret" {
  type      = string
  sensitive = true
}
```

### 6️⃣ terraform.tfvars

```hcl
pm_vm_name      = "vm300148094"
pm_ipconfig0    = "ip=10.7.237.xxx/23,gw=10.7.237.1"
pm_nameserver   = "10.7.237.3"
pm_url          = "https://10.7.237.xx:8006/api2/json"
pm_token_id     = "tofu@pve!opentofu"
pm_token_secret = "VOTRE-SECRET-ICI"
```

> ⚠️ **Ne jamais commiter ce fichier dans Git !** Ajouter `terraform.tfvars` au `.gitignore`.

### 7️⃣ Initialisation et déploiement

```bash
tofu init     # Télécharge les providers
tofu plan     # Prévisualise les changements
tofu apply    # Applique (répondre "yes")
```

### 8️⃣ Connexion SSH à la VM

```bash
# Linux / Mac
ssh -i ~/.ssh/ma_cle.pk \
  -o StrictHostKeyChecking=no \
  ubuntu@10.7.237.xxx

# PowerShell (Windows)
ssh -i ~/.ssh/ma_cle.pk `
  -o StrictHostKeyChecking=no `
  ubuntu@10.7.237.xxx
```

---

## Bonnes pratiques

- ✅ **Versionner** toute l'infrastructure avec Git
- ✅ **Ne jamais modifier** manuellement en production
- ✅ **Séparer** les environnements dev / test / prod
- ✅ **Sécuriser** les variables et secrets (`.tfvars` dans `.gitignore`)
- ✅ **La documentation = le code** lui-même

---

## IaC et DevOps

L'IaC est un **pilier fondamental du DevOps** :

```
CI/CD  →  Déploiement continu  →  Scalabilité  →  Résilience  →  SRE
```

> 🔑 *Sans IaC, le DevOps n'est pas viable à grande échelle.*

---

## Objectifs pédagogiques

À la fin de ce module, l'étudiant(e) sera capable de :

- [ ] Expliquer le concept d'IaC
- [ ] Distinguer script système et IaC
- [ ] Décrire une infrastructure de manière déclarative
- [ ] Utiliser OpenTofu pour créer une VM sur Proxmox
- [ ] Automatiser un déploiement système complet

---

## 💬 Conclusion

> *"L'Infrastructure as Code transforme l'administration système en une discipline de programmation structurée, reproductible et industrielle."*

---

*Ouail Gacem — 300148094*# 📘 Infrastructure as Code (IaC)

> **Nom :** Ouail Gacem  
> **Matricule :** 300148094  
> **Cours :** Programmation système — Administration moderne

---

## 📋 Table des matières

1. [Introduction](#introduction)
2. [Définition](#définition)
3. [Position dans la pile système](#position-dans-la-pile-système)
4. [Pourquoi utiliser l'IaC ?](#pourquoi-utiliser-liac)
5. [IaC vs Scripts classiques](#iac-vs-scripts-classiques)
6. [Approches de l'IaC](#approches-de-liac)
7. [Ce qu'on peut gérer](#ce-quon-peut-gérer)
8. [Outils courants](#outils-courants)
9. [Exercices pratiques — OpenTofu + Proxmox](#exercices-pratiques--opentofu--proxmox)
10. [Bonnes pratiques](#bonnes-pratiques)
11. [IaC et DevOps](#iac-et-devops)
12. [Objectifs pédagogiques](#objectifs-pédagogiques)

---

## Introduction

Traditionnellement, l'administration des systèmes se faisait **manuellement** :

- Installation à la main
- Configurations faites "à la souris"
- Documentation incomplète
- Environnements difficiles à reproduire

> ⚠️ **Problème majeur :** *"Ça marche sur ce serveur, mais pas sur l'autre."*

**Solution moderne → Infrastructure as Code (IaC)**

---

## Définition

**Infrastructure as Code (IaC)** est une approche de programmation système qui permet de gérer les ressources informatiques (serveurs, réseaux, services, utilisateurs, stockage) à l'aide de **fichiers de configuration versionnés** et exécutables automatiquement.

---

## Position dans la pile système

```
Applications
──────────────────────────
Services (Web, DB, DNS, AD, Containers)
──────────────────────────
Infrastructure as Code (IaC)   ◀️ Notre niveau
──────────────────────────
Shell / API OS / Hyperviseur / Cloud
──────────────────────────
Noyau (Linux / Windows)
──────────────────────────
Matériel
```

> L'IaC agit via des **API**, des **services système** et des **hyperviseurs** — sans toucher au noyau.

---

## Pourquoi utiliser l'IaC ?

### ❌ Sans IaC

| Problème | Impact |
|----------|--------|
| Erreurs humaines | Configurations incorrectes |
| Incohérences entre serveurs | Environnements instables |
| Déploiements lents | Perte de temps |
| Documentation non fiable | Difficile à reproduire |

### ✅ Avec IaC

| Avantage | Description |
|----------|-------------|
| **Reproductibilité** | Même infrastructure, partout |
| **Automatisation** | Déploiement sans intervention manuelle |
| **Versionnement** | Git = historique + rollback |
| **Fiabilité** | Moins d'erreurs humaines |
| **Rapidité** | Déploiement en minutes |
| **Auditabilité** | Tout est traçable |

---

## IaC vs Scripts classiques

### Scripts système (impératif)

```bash
apt update
apt install nginx
systemctl start nginx
```

- Dépend de l'ordre d'exécution
- Difficile à maintenir
- Non idempotent

### IaC (déclaratif)

```hcl
resource "nginx_server" {
  version = "1.24"
  port    = 80
}
```

- Décrit l'**état final** souhaité
- L'outil décide comment y arriver
- Idempotent ✔️

---

## Approches de l'IaC

### 🟢 Déclaratif (recommandé)

> *"Voici l'état voulu"*

- **Terraform / OpenTofu**
- **CloudFormation**
- **Kubernetes YAML**

✔ Reproductible &nbsp; ✔ Idempotent &nbsp; ✔ Facile à maintenir

### 🟡 Impératif

> *"Fais ceci, puis cela"*

- **Scripts shell**
- **Ansible** (mixte)

✔ Flexible &nbsp; ✖ Plus complexe à maintenir

---

## Ce qu'on peut gérer

- 🖥️ Machines virtuelles
- 🌐 Réseaux (VLAN, bridges, firewall)
- 💾 Stockage
- 👤 Utilisateurs et permissions
- ⚙️ Services (web, DB, DNS)
- 📦 Containers
- 🧩 Clusters
- ☁️ Infrastructure cloud (AWS, Azure, GCP)
- 🏠 Infrastructure locale (Proxmox, VMware)

> 💡 **L'infrastructure devient un programme.**

---

## Outils courants

### Orchestration

| Outil | Usage |
|-------|-------|
| **Terraform / OpenTofu** | Multi-cloud, local |
| **CloudFormation** | AWS natif |
| **Pulumi** | Code natif (Python, JS...) |

### Configuration

| Outil | Usage |
|-------|-------|
| **Ansible** | Agentless, SSH |
| **Puppet** | Agent-based |
| **Chef** | Ruby DSL |

---

## Exercices pratiques — OpenTofu + Proxmox

### 1️⃣ Installation d'OpenTofu

```bash
# Windows
choco install opentofu

# Mac
brew install opentofu

# Vérification
tofu version
```

### 2️⃣ Structure du projet

```bash
touch provider.tf main.tf variables.tf terraform.tfvars
```

```
mon-projet/
├── provider.tf       # Configuration du provider Proxmox
├── main.tf           # Ressource VM
├── variables.tf      # Déclaration des variables
└── terraform.tfvars  # Valeurs (⚠️ Ne pas commiter !)
```

### 3️⃣ provider.tf

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

### 4️⃣ main.tf — VM Cloud-Init

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

  os_type   = "cloud-init"
  ipconfig0 = var.pm_ipconfig0
  nameserver = var.pm_nameserver

  ciuser  = "ubuntu"
  sshkeys = <<EOF
  ${file("~/.ssh/ma_cle.pub")}
  ${file("~/.ssh/cle_publique_du_prof.pub")}
  EOF
}
```

### 5️⃣ variables.tf

```hcl
variable "pm_vm_name"    { type = string }
variable "pm_ipconfig0"  { type = string }
variable "pm_nameserver" { type = string }
variable "pm_url"        { type = string }
variable "pm_token_id"   { type = string }
variable "pm_token_secret" {
  type      = string
  sensitive = true
}
```

### 6️⃣ terraform.tfvars

```hcl
pm_vm_name      = "vm300148094"
pm_ipconfig0    = "ip=10.7.237.xxx/23,gw=10.7.237.1"
pm_nameserver   = "10.7.237.3"
pm_url          = "https://10.7.237.xx:8006/api2/json"
pm_token_id     = "tofu@pve!opentofu"
pm_token_secret = "VOTRE-SECRET-ICI"
```

> ⚠️ **Ne jamais commiter ce fichier dans Git !** Ajouter `terraform.tfvars` au `.gitignore`.

### 7️⃣ Initialisation et déploiement

```bash
tofu init     # Télécharge les providers
tofu plan     # Prévisualise les changements
tofu apply    # Applique (répondre "yes")
```

### 8️⃣ Connexion SSH à la VM

```bash
# Linux / Mac
ssh -i ~/.ssh/ma_cle.pk \
  -o StrictHostKeyChecking=no \
  ubuntu@10.7.237.xxx

# PowerShell (Windows)
ssh -i ~/.ssh/ma_cle.pk `
  -o StrictHostKeyChecking=no `
  ubuntu@10.7.237.xxx
```

---

## Bonnes pratiques

- ✅ **Versionner** toute l'infrastructure avec Git
- ✅ **Ne jamais modifier** manuellement en production
- ✅ **Séparer** les environnements dev / test / prod
- ✅ **Sécuriser** les variables et secrets (`.tfvars` dans `.gitignore`)
- ✅ **La documentation = le code** lui-même

---

## IaC et DevOps

L'IaC est un **pilier fondamental du DevOps** :

```
CI/CD  →  Déploiement continu  →  Scalabilité  →  Résilience  →  SRE
```

> 🔑 *Sans IaC, le DevOps n'est pas viable à grande échelle.*

---

## Objectifs pédagogiques

À la fin de ce module, l'étudiant(e) sera capable de :

- [ ] Expliquer le concept d'IaC
- [ ] Distinguer script système et IaC
- [ ] Décrire une infrastructure de manière déclarative
- [ ] Utiliser OpenTofu pour créer une VM sur Proxmox
- [ ] Automatiser un déploiement système complet

---

## 💬 Conclusion

> *"L'Infrastructure as Code transforme l'administration système en une discipline de programmation structurée, reproductible et industrielle."*

---

*Ouail Gacem — 300148094*# 📘 Infrastructure as Code (IaC)

> **Nom :** Ouail Gacem  
> **Matricule :** 300148094  
> **Cours :** Programmation système — Administration moderne

---

## 📋 Table des matières

1. [Introduction](#introduction)
2. [Définition](#définition)
3. [Position dans la pile système](#position-dans-la-pile-système)
4. [Pourquoi utiliser l'IaC ?](#pourquoi-utiliser-liac)
5. [IaC vs Scripts classiques](#iac-vs-scripts-classiques)
6. [Approches de l'IaC](#approches-de-liac)
7. [Ce qu'on peut gérer](#ce-quon-peut-gérer)
8. [Outils courants](#outils-courants)
9. [Exercices pratiques — OpenTofu + Proxmox](#exercices-pratiques--opentofu--proxmox)
10. [Bonnes pratiques](#bonnes-pratiques)
11. [IaC et DevOps](#iac-et-devops)
12. [Objectifs pédagogiques](#objectifs-pédagogiques)

---

## Introduction

Traditionnellement, l'administration des systèmes se faisait **manuellement** :

- Installation à la main
- Configurations faites "à la souris"
- Documentation incomplète
- Environnements difficiles à reproduire

> ⚠️ **Problème majeur :** *"Ça marche sur ce serveur, mais pas sur l'autre."*

**Solution moderne → Infrastructure as Code (IaC)**

---

## Définition

**Infrastructure as Code (IaC)** est une approche de programmation système qui permet de gérer les ressources informatiques (serveurs, réseaux, services, utilisateurs, stockage) à l'aide de **fichiers de configuration versionnés** et exécutables automatiquement.

---

## Position dans la pile système

```
Applications
──────────────────────────
Services (Web, DB, DNS, AD, Containers)
──────────────────────────
Infrastructure as Code (IaC)   ◀️ Notre niveau
──────────────────────────
Shell / API OS / Hyperviseur / Cloud
──────────────────────────
Noyau (Linux / Windows)
──────────────────────────
Matériel
```

> L'IaC agit via des **API**, des **services système** et des **hyperviseurs** — sans toucher au noyau.

---

## Pourquoi utiliser l'IaC ?

### ❌ Sans IaC

| Problème | Impact |
|----------|--------|
| Erreurs humaines | Configurations incorrectes |
| Incohérences entre serveurs | Environnements instables |
| Déploiements lents | Perte de temps |
| Documentation non fiable | Difficile à reproduire |

### ✅ Avec IaC

| Avantage | Description |
|----------|-------------|
| **Reproductibilité** | Même infrastructure, partout |
| **Automatisation** | Déploiement sans intervention manuelle |
| **Versionnement** | Git = historique + rollback |
| **Fiabilité** | Moins d'erreurs humaines |
| **Rapidité** | Déploiement en minutes |
| **Auditabilité** | Tout est traçable |

---

## IaC vs Scripts classiques

### Scripts système (impératif)

```bash
apt update
apt install nginx
systemctl start nginx
```

- Dépend de l'ordre d'exécution
- Difficile à maintenir
- Non idempotent

### IaC (déclaratif)

```hcl
resource "nginx_server" {
  version = "1.24"
  port    = 80
}
```

- Décrit l'**état final** souhaité
- L'outil décide comment y arriver
- Idempotent ✔️

---

## Approches de l'IaC

### 🟢 Déclaratif (recommandé)

> *"Voici l'état voulu"*

- **Terraform / OpenTofu**
- **CloudFormation**
- **Kubernetes YAML**

✔ Reproductible &nbsp; ✔ Idempotent &nbsp; ✔ Facile à maintenir

### 🟡 Impératif

> *"Fais ceci, puis cela"*

- **Scripts shell**
- **Ansible** (mixte)

✔ Flexible &nbsp; ✖ Plus complexe à maintenir

---

## Ce qu'on peut gérer

- 🖥️ Machines virtuelles
- 🌐 Réseaux (VLAN, bridges, firewall)
- 💾 Stockage
- 👤 Utilisateurs et permissions
- ⚙️ Services (web, DB, DNS)
- 📦 Containers
- 🧩 Clusters
- ☁️ Infrastructure cloud (AWS, Azure, GCP)
- 🏠 Infrastructure locale (Proxmox, VMware)

> 💡 **L'infrastructure devient un programme.**

---

## Outils courants

### Orchestration

| Outil | Usage |
|-------|-------|
| **Terraform / OpenTofu** | Multi-cloud, local |
| **CloudFormation** | AWS natif |
| **Pulumi** | Code natif (Python, JS...) |

### Configuration

| Outil | Usage |
|-------|-------|
| **Ansible** | Agentless, SSH |
| **Puppet** | Agent-based |
| **Chef** | Ruby DSL |

---

## Exercices pratiques — OpenTofu + Proxmox

### 1️⃣ Installation d'OpenTofu

```bash
# Windows
choco install opentofu

# Mac
brew install opentofu

# Vérification
tofu version
```

### 2️⃣ Structure du projet

```bash
touch provider.tf main.tf variables.tf terraform.tfvars
```

```
mon-projet/
├── provider.tf       # Configuration du provider Proxmox
├── main.tf           # Ressource VM
├── variables.tf      # Déclaration des variables
└── terraform.tfvars  # Valeurs (⚠️ Ne pas commiter !)
```

### 3️⃣ provider.tf

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

### 4️⃣ main.tf — VM Cloud-Init

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

  os_type   = "cloud-init"
  ipconfig0 = var.pm_ipconfig0
  nameserver = var.pm_nameserver

  ciuser  = "ubuntu"
  sshkeys = <<EOF
  ${file("~/.ssh/ma_cle.pub")}
  ${file("~/.ssh/cle_publique_du_prof.pub")}
  EOF
}
```

### 5️⃣ variables.tf

```hcl
variable "pm_vm_name"    { type = string }
variable "pm_ipconfig0"  { type = string }
variable "pm_nameserver" { type = string }
variable "pm_url"        { type = string }
variable "pm_token_id"   { type = string }
variable "pm_token_secret" {
  type      = string
  sensitive = true
}
```

### 6️⃣ terraform.tfvars

```hcl
pm_vm_name      = "vm300148094"
pm_ipconfig0    = "ip=10.7.237.xxx/23,gw=10.7.237.1"
pm_nameserver   = "10.7.237.3"
pm_url          = "https://10.7.237.xx:8006/api2/json"
pm_token_id     = "tofu@pve!opentofu"
pm_token_secret = "VOTRE-SECRET-ICI"
```

> ⚠️ **Ne jamais commiter ce fichier dans Git !** Ajouter `terraform.tfvars` au `.gitignore`.

### 7️⃣ Initialisation et déploiement

```bash
tofu init     # Télécharge les providers
tofu plan     # Prévisualise les changements
tofu apply    # Applique (répondre "yes")
```

### 8️⃣ Connexion SSH à la VM

```bash
# Linux / Mac
ssh -i ~/.ssh/ma_cle.pk \
  -o StrictHostKeyChecking=no \
  ubuntu@10.7.237.xxx

# PowerShell (Windows)
ssh -i ~/.ssh/ma_cle.pk `
  -o StrictHostKeyChecking=no `
  ubuntu@10.7.237.xxx
```

---

## Bonnes pratiques

- ✅ **Versionner** toute l'infrastructure avec Git
- ✅ **Ne jamais modifier** manuellement en production
- ✅ **Séparer** les environnements dev / test / prod
- ✅ **Sécuriser** les variables et secrets (`.tfvars` dans `.gitignore`)
- ✅ **La documentation = le code** lui-même

---

## IaC et DevOps

L'IaC est un **pilier fondamental du DevOps** :

```
CI/CD  →  Déploiement continu  →  Scalabilité  →  Résilience  →  SRE
```

> 🔑 *Sans IaC, le DevOps n'est pas viable à grande échelle.*

---

## Objectifs pédagogiques

À la fin de ce module, l'étudiant(e) sera capable de :

- [ ] Expliquer le concept d'IaC
- [ ] Distinguer script système et IaC
- [ ] Décrire une infrastructure de manière déclarative
- [ ] Utiliser OpenTofu pour créer une VM sur Proxmox
- [ ] Automatiser un déploiement système complet

---

## 💬 Conclusion

> *"L'Infrastructure as Code transforme l'administration système en une discipline de programmation structurée, reproductible et industrielle."*

---

*Ouail Gacem — 300148094*# 📘 Infrastructure as Code (IaC)

> **Nom :** Ouail Gacem  
> **Matricule :** 300148094  
> **Cours :** Programmation système — Administration moderne

---

## 📋 Table des matières

1. [Introduction](#introduction)
2. [Définition](#définition)
3. [Position dans la pile système](#position-dans-la-pile-système)
4. [Pourquoi utiliser l'IaC ?](#pourquoi-utiliser-liac)
5. [IaC vs Scripts classiques](#iac-vs-scripts-classiques)
6. [Approches de l'IaC](#approches-de-liac)
7. [Ce qu'on peut gérer](#ce-quon-peut-gérer)
8. [Outils courants](#outils-courants)
9. [Exercices pratiques — OpenTofu + Proxmox](#exercices-pratiques--opentofu--proxmox)
10. [Bonnes pratiques](#bonnes-pratiques)
11. [IaC et DevOps](#iac-et-devops)
12. [Objectifs pédagogiques](#objectifs-pédagogiques)

---

## Introduction

Traditionnellement, l'administration des systèmes se faisait **manuellement** :

- Installation à la main
- Configurations faites "à la souris"
- Documentation incomplète
- Environnements difficiles à reproduire

> ⚠️ **Problème majeur :** *"Ça marche sur ce serveur, mais pas sur l'autre."*

**Solution moderne → Infrastructure as Code (IaC)**

---

## Définition

**Infrastructure as Code (IaC)** est une approche de programmation système qui permet de gérer les ressources informatiques (serveurs, réseaux, services, utilisateurs, stockage) à l'aide de **fichiers de configuration versionnés** et exécutables automatiquement.

---

## Position dans la pile système

```
Applications
──────────────────────────
Services (Web, DB, DNS, AD, Containers)
──────────────────────────
Infrastructure as Code (IaC)   ◀️ Notre niveau
──────────────────────────
Shell / API OS / Hyperviseur / Cloud
──────────────────────────
Noyau (Linux / Windows)
──────────────────────────
Matériel
```

> L'IaC agit via des **API**, des **services système** et des **hyperviseurs** — sans toucher au noyau.

---

## Pourquoi utiliser l'IaC ?

### ❌ Sans IaC

| Problème | Impact |
|----------|--------|
| Erreurs humaines | Configurations incorrectes |
| Incohérences entre serveurs | Environnements instables |
| Déploiements lents | Perte de temps |
| Documentation non fiable | Difficile à reproduire |

### ✅ Avec IaC

| Avantage | Description |
|----------|-------------|
| **Reproductibilité** | Même infrastructure, partout |
| **Automatisation** | Déploiement sans intervention manuelle |
| **Versionnement** | Git = historique + rollback |
| **Fiabilité** | Moins d'erreurs humaines |
| **Rapidité** | Déploiement en minutes |
| **Auditabilité** | Tout est traçable |

---

## IaC vs Scripts classiques

### Scripts système (impératif)

```bash
apt update
apt install nginx
systemctl start nginx
```

- Dépend de l'ordre d'exécution
- Difficile à maintenir
- Non idempotent

### IaC (déclaratif)

```hcl
resource "nginx_server" {
  version = "1.24"
  port    = 80
}
```

- Décrit l'**état final** souhaité
- L'outil décide comment y arriver
- Idempotent ✔️

---

## Approches de l'IaC

### 🟢 Déclaratif (recommandé)

> *"Voici l'état voulu"*

- **Terraform / OpenTofu**
- **CloudFormation**
- **Kubernetes YAML**

✔ Reproductible &nbsp; ✔ Idempotent &nbsp; ✔ Facile à maintenir

### 🟡 Impératif

> *"Fais ceci, puis cela"*

- **Scripts shell**
- **Ansible** (mixte)

✔ Flexible &nbsp; ✖ Plus complexe à maintenir

---

## Ce qu'on peut gérer

- 🖥️ Machines virtuelles
- 🌐 Réseaux (VLAN, bridges, firewall)
- 💾 Stockage
- 👤 Utilisateurs et permissions
- ⚙️ Services (web, DB, DNS)
- 📦 Containers
- 🧩 Clusters
- ☁️ Infrastructure cloud (AWS, Azure, GCP)
- 🏠 Infrastructure locale (Proxmox, VMware)

> 💡 **L'infrastructure devient un programme.**

---

## Outils courants

### Orchestration

| Outil | Usage |
|-------|-------|
| **Terraform / OpenTofu** | Multi-cloud, local |
| **CloudFormation** | AWS natif |
| **Pulumi** | Code natif (Python, JS...) |

### Configuration

| Outil | Usage |
|-------|-------|
| **Ansible** | Agentless, SSH |
| **Puppet** | Agent-based |
| **Chef** | Ruby DSL |

---

## Exercices pratiques — OpenTofu + Proxmox

### 1️⃣ Installation d'OpenTofu

```bash
# Windows
choco install opentofu

# Mac
brew install opentofu

# Vérification
tofu version
```

### 2️⃣ Structure du projet

```bash
touch provider.tf main.tf variables.tf terraform.tfvars
```

```
mon-projet/
├── provider.tf       # Configuration du provider Proxmox
├── main.tf           # Ressource VM
├── variables.tf      # Déclaration des variables
└── terraform.tfvars  # Valeurs (⚠️ Ne pas commiter !)
```

### 3️⃣ provider.tf

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

### 4️⃣ main.tf — VM Cloud-Init

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

  os_type   = "cloud-init"
  ipconfig0 = var.pm_ipconfig0
  nameserver = var.pm_nameserver

  ciuser  = "ubuntu"
  sshkeys = <<EOF
  ${file("~/.ssh/ma_cle.pub")}
  ${file("~/.ssh/cle_publique_du_prof.pub")}
  EOF
}
```

### 5️⃣ variables.tf

```hcl
variable "pm_vm_name"    { type = string }
variable "pm_ipconfig0"  { type = string }
variable "pm_nameserver" { type = string }
variable "pm_url"        { type = string }
variable "pm_token_id"   { type = string }
variable "pm_token_secret" {
  type      = string
  sensitive = true
}
```

### 6️⃣ terraform.tfvars

```hcl
pm_vm_name      = "vm300148094"
pm_ipconfig0    = "ip=10.7.237.xxx/23,gw=10.7.237.1"
pm_nameserver   = "10.7.237.3"
pm_url          = "https://10.7.237.xx:8006/api2/json"
pm_token_id     = "tofu@pve!opentofu"
pm_token_secret = "VOTRE-SECRET-ICI"
```

> ⚠️ **Ne jamais commiter ce fichier dans Git !** Ajouter `terraform.tfvars` au `.gitignore`.

### 7️⃣ Initialisation et déploiement

```bash
tofu init     # Télécharge les providers
tofu plan     # Prévisualise les changements
tofu apply    # Applique (répondre "yes")
```

### 8️⃣ Connexion SSH à la VM

```bash
# Linux / Mac
ssh -i ~/.ssh/ma_cle.pk \
  -o StrictHostKeyChecking=no \
  ubuntu@10.7.237.xxx

# PowerShell (Windows)
ssh -i ~/.ssh/ma_cle.pk `
  -o StrictHostKeyChecking=no `
  ubuntu@10.7.237.xxx
```

---

## Bonnes pratiques

- ✅ **Versionner** toute l'infrastructure avec Git
- ✅ **Ne jamais modifier** manuellement en production
- ✅ **Séparer** les environnements dev / test / prod
- ✅ **Sécuriser** les variables et secrets (`.tfvars` dans `.gitignore`)
- ✅ **La documentation = le code** lui-même

---

## IaC et DevOps

L'IaC est un **pilier fondamental du DevOps** :

```
CI/CD  →  Déploiement continu  →  Scalabilité  →  Résilience  →  SRE
```

> 🔑 *Sans IaC, le DevOps n'est pas viable à grande échelle.*

---

## Objectifs pédagogiques

À la fin de ce module, l'étudiant(e) sera capable de :

- [ ] Expliquer le concept d'IaC
- [ ] Distinguer script système et IaC
- [ ] Décrire une infrastructure de manière déclarative
- [ ] Utiliser OpenTofu pour créer une VM sur Proxmox
- [ ] Automatiser un déploiement système complet

---

## 💬 Conclusion

> *"L'Infrastructure as Code transforme l'administration système en une discipline de programmation structurée, reproductible et industrielle."*

---

*Ouail Gacem — 300148094*# 📘 Infrastructure as Code (IaC)

> **Nom :** Ouail Gacem  
> **Matricule :** 300148094  
> **Cours :** Programmation système — Administration moderne

---

## 📋 Table des matières

1. [Introduction](#introduction)
2. [Définition](#définition)
3. [Position dans la pile système](#position-dans-la-pile-système)
4. [Pourquoi utiliser l'IaC ?](#pourquoi-utiliser-liac)
5. [IaC vs Scripts classiques](#iac-vs-scripts-classiques)
6. [Approches de l'IaC](#approches-de-liac)
7. [Ce qu'on peut gérer](#ce-quon-peut-gérer)
8. [Outils courants](#outils-courants)
9. [Exercices pratiques — OpenTofu + Proxmox](#exercices-pratiques--opentofu--proxmox)
10. [Bonnes pratiques](#bonnes-pratiques)
11. [IaC et DevOps](#iac-et-devops)
12. [Objectifs pédagogiques](#objectifs-pédagogiques)

---

## Introduction

Traditionnellement, l'administration des systèmes se faisait **manuellement** :

- Installation à la main
- Configurations faites "à la souris"
- Documentation incomplète
- Environnements difficiles à reproduire

> ⚠️ **Problème majeur :** *"Ça marche sur ce serveur, mais pas sur l'autre."*

**Solution moderne → Infrastructure as Code (IaC)**

---

## Définition

**Infrastructure as Code (IaC)** est une approche de programmation système qui permet de gérer les ressources informatiques (serveurs, réseaux, services, utilisateurs, stockage) à l'aide de **fichiers de configuration versionnés** et exécutables automatiquement.

---

## Position dans la pile système

```
Applications
──────────────────────────
Services (Web, DB, DNS, AD, Containers)
──────────────────────────
Infrastructure as Code (IaC)   ◀️ Notre niveau
──────────────────────────
Shell / API OS / Hyperviseur / Cloud
──────────────────────────
Noyau (Linux / Windows)
──────────────────────────
Matériel
```

> L'IaC agit via des **API**, des **services système** et des **hyperviseurs** — sans toucher au noyau.

---

## Pourquoi utiliser l'IaC ?

### ❌ Sans IaC

| Problème | Impact |
|----------|--------|
| Erreurs humaines | Configurations incorrectes |
| Incohérences entre serveurs | Environnements instables |
| Déploiements lents | Perte de temps |
| Documentation non fiable | Difficile à reproduire |

### ✅ Avec IaC

| Avantage | Description |
|----------|-------------|
| **Reproductibilité** | Même infrastructure, partout |
| **Automatisation** | Déploiement sans intervention manuelle |
| **Versionnement** | Git = historique + rollback |
| **Fiabilité** | Moins d'erreurs humaines |
| **Rapidité** | Déploiement en minutes |
| **Auditabilité** | Tout est traçable |

---

## IaC vs Scripts classiques

### Scripts système (impératif)

```bash
apt update
apt install nginx
systemctl start nginx
```

- Dépend de l'ordre d'exécution
- Difficile à maintenir
- Non idempotent

### IaC (déclaratif)

```hcl
resource "nginx_server" {
  version = "1.24"
  port    = 80
}
```

- Décrit l'**état final** souhaité
- L'outil décide comment y arriver
- Idempotent ✔️

---

## Approches de l'IaC

### 🟢 Déclaratif (recommandé)

> *"Voici l'état voulu"*

- **Terraform / OpenTofu**
- **CloudFormation**
- **Kubernetes YAML**

✔ Reproductible &nbsp; ✔ Idempotent &nbsp; ✔ Facile à maintenir

### 🟡 Impératif

> *"Fais ceci, puis cela"*

- **Scripts shell**
- **Ansible** (mixte)

✔ Flexible &nbsp; ✖ Plus complexe à maintenir

---

## Ce qu'on peut gérer

- 🖥️ Machines virtuelles
- 🌐 Réseaux (VLAN, bridges, firewall)
- 💾 Stockage
- 👤 Utilisateurs et permissions
- ⚙️ Services (web, DB, DNS)
- 📦 Containers
- 🧩 Clusters
- ☁️ Infrastructure cloud (AWS, Azure, GCP)
- 🏠 Infrastructure locale (Proxmox, VMware)

> 💡 **L'infrastructure devient un programme.**

---

## Outils courants

### Orchestration

| Outil | Usage |
|-------|-------|
| **Terraform / OpenTofu** | Multi-cloud, local |
| **CloudFormation** | AWS natif |
| **Pulumi** | Code natif (Python, JS...) |

### Configuration

| Outil | Usage |
|-------|-------|
| **Ansible** | Agentless, SSH |
| **Puppet** | Agent-based |
| **Chef** | Ruby DSL |

---

## Exercices pratiques — OpenTofu + Proxmox

### 1️⃣ Installation d'OpenTofu

```bash
# Windows
choco install opentofu

# Mac
brew install opentofu

# Vérification
tofu version
```

### 2️⃣ Structure du projet

```bash
touch provider.tf main.tf variables.tf terraform.tfvars
```

```
mon-projet/
├── provider.tf       # Configuration du provider Proxmox
├── main.tf           # Ressource VM
├── variables.tf      # Déclaration des variables
└── terraform.tfvars  # Valeurs (⚠️ Ne pas commiter !)
```

### 3️⃣ provider.tf

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

### 4️⃣ main.tf — VM Cloud-Init

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

  os_type   = "cloud-init"
  ipconfig0 = var.pm_ipconfig0
  nameserver = var.pm_nameserver

  ciuser  = "ubuntu"
  sshkeys = <<EOF
  ${file("~/.ssh/ma_cle.pub")}
  ${file("~/.ssh/cle_publique_du_prof.pub")}
  EOF
}
```

### 5️⃣ variables.tf

```hcl
variable "pm_vm_name"    { type = string }
variable "pm_ipconfig0"  { type = string }
variable "pm_nameserver" { type = string }
variable "pm_url"        { type = string }
variable "pm_token_id"   { type = string }
variable "pm_token_secret" {
  type      = string
  sensitive = true
}
```

### 6️⃣ terraform.tfvars

```hcl
pm_vm_name      = "vm300148094"
pm_ipconfig0    = "ip=10.7.237.xxx/23,gw=10.7.237.1"
pm_nameserver   = "10.7.237.3"
pm_url          = "https://10.7.237.xx:8006/api2/json"
pm_token_id     = "tofu@pve!opentofu"
pm_token_secret = "VOTRE-SECRET-ICI"
```

> ⚠️ **Ne jamais commiter ce fichier dans Git !** Ajouter `terraform.tfvars` au `.gitignore`.

### 7️⃣ Initialisation et déploiement

```bash
tofu init     # Télécharge les providers
tofu plan     # Prévisualise les changements
tofu apply    # Applique (répondre "yes")
```

### 8️⃣ Connexion SSH à la VM

```bash
# Linux / Mac
ssh -i ~/.ssh/ma_cle.pk \
  -o StrictHostKeyChecking=no \
  ubuntu@10.7.237.xxx

# PowerShell (Windows)
ssh -i ~/.ssh/ma_cle.pk `
  -o StrictHostKeyChecking=no `
  ubuntu@10.7.237.xxx
```

---

## Bonnes pratiques

- ✅ **Versionner** toute l'infrastructure avec Git
- ✅ **Ne jamais modifier** manuellement en production
- ✅ **Séparer** les environnements dev / test / prod
- ✅ **Sécuriser** les variables et secrets (`.tfvars` dans `.gitignore`)
- ✅ **La documentation = le code** lui-même

---

## IaC et DevOps

L'IaC est un **pilier fondamental du DevOps** :

```
CI/CD  →  Déploiement continu  →  Scalabilité  →  Résilience  →  SRE
```

> 🔑 *Sans IaC, le DevOps n'est pas viable à grande échelle.*

---

## Objectifs pédagogiques

À la fin de ce module, l'étudiant(e) sera capable de :

- [ ] Expliquer le concept d'IaC
- [ ] Distinguer script système et IaC
- [ ] Décrire une infrastructure de manière déclarative
- [ ] Utiliser OpenTofu pour créer une VM sur Proxmox
- [ ] Automatiser un déploiement système complet

---

## 💬 Conclusion

> *"L'Infrastructure as Code transforme l'administration système en une discipline de programmation structurée, reproductible et industrielle."*

---

*Ouail Gacem — 300148094*# 📘 Infrastructure as Code (IaC)

> **Nom :** Ouail Gacem  
> **Matricule :** 300148094  
> **Cours :** Programmation système — Administration moderne

---

## 📋 Table des matières

1. [Introduction](#introduction)
2. [Définition](#définition)
3. [Position dans la pile système](#position-dans-la-pile-système)
4. [Pourquoi utiliser l'IaC ?](#pourquoi-utiliser-liac)
5. [IaC vs Scripts classiques](#iac-vs-scripts-classiques)
6. [Approches de l'IaC](#approches-de-liac)
7. [Ce qu'on peut gérer](#ce-quon-peut-gérer)
8. [Outils courants](#outils-courants)
9. [Exercices pratiques — OpenTofu + Proxmox](#exercices-pratiques--opentofu--proxmox)
10. [Bonnes pratiques](#bonnes-pratiques)
11. [IaC et DevOps](#iac-et-devops)
12. [Objectifs pédagogiques](#objectifs-pédagogiques)

---

## Introduction

Traditionnellement, l'administration des systèmes se faisait **manuellement** :

- Installation à la main
- Configurations faites "à la souris"
- Documentation incomplète
- Environnements difficiles à reproduire

> ⚠️ **Problème majeur :** *"Ça marche sur ce serveur, mais pas sur l'autre."*

**Solution moderne → Infrastructure as Code (IaC)**

---

## Définition

**Infrastructure as Code (IaC)** est une approche de programmation système qui permet de gérer les ressources informatiques (serveurs, réseaux, services, utilisateurs, stockage) à l'aide de **fichiers de configuration versionnés** et exécutables automatiquement.

---

## Position dans la pile système

```
Applications
──────────────────────────
Services (Web, DB, DNS, AD, Containers)
──────────────────────────
Infrastructure as Code (IaC)   ◀️ Notre niveau
──────────────────────────
Shell / API OS / Hyperviseur / Cloud
──────────────────────────
Noyau (Linux / Windows)
──────────────────────────
Matériel
```

> L'IaC agit via des **API**, des **services système** et des **hyperviseurs** — sans toucher au noyau.

---

## Pourquoi utiliser l'IaC ?

### ❌ Sans IaC

| Problème | Impact |
|----------|--------|
| Erreurs humaines | Configurations incorrectes |
| Incohérences entre serveurs | Environnements instables |
| Déploiements lents | Perte de temps |
| Documentation non fiable | Difficile à reproduire |

### ✅ Avec IaC

| Avantage | Description |
|----------|-------------|
| **Reproductibilité** | Même infrastructure, partout |
| **Automatisation** | Déploiement sans intervention manuelle |
| **Versionnement** | Git = historique + rollback |
| **Fiabilité** | Moins d'erreurs humaines |
| **Rapidité** | Déploiement en minutes |
| **Auditabilité** | Tout est traçable |

---

## IaC vs Scripts classiques

### Scripts système (impératif)

```bash
apt update
apt install nginx
systemctl start nginx
```

- Dépend de l'ordre d'exécution
- Difficile à maintenir
- Non idempotent

### IaC (déclaratif)

```hcl
resource "nginx_server" {
  version = "1.24"
  port    = 80
}
```

- Décrit l'**état final** souhaité
- L'outil décide comment y arriver
- Idempotent ✔️

---

## Approches de l'IaC

### 🟢 Déclaratif (recommandé)

> *"Voici l'état voulu"*

- **Terraform / OpenTofu**
- **CloudFormation**
- **Kubernetes YAML**

✔ Reproductible &nbsp; ✔ Idempotent &nbsp; ✔ Facile à maintenir

### 🟡 Impératif

> *"Fais ceci, puis cela"*

- **Scripts shell**
- **Ansible** (mixte)

✔ Flexible &nbsp; ✖ Plus complexe à maintenir

---

## Ce qu'on peut gérer

- 🖥️ Machines virtuelles
- 🌐 Réseaux (VLAN, bridges, firewall)
- 💾 Stockage
- 👤 Utilisateurs et permissions
- ⚙️ Services (web, DB, DNS)
- 📦 Containers
- 🧩 Clusters
- ☁️ Infrastructure cloud (AWS, Azure, GCP)
- 🏠 Infrastructure locale (Proxmox, VMware)

> 💡 **L'infrastructure devient un programme.**

---

## Outils courants

### Orchestration

| Outil | Usage |
|-------|-------|
| **Terraform / OpenTofu** | Multi-cloud, local |
| **CloudFormation** | AWS natif |
| **Pulumi** | Code natif (Python, JS...) |

### Configuration

| Outil | Usage |
|-------|-------|
| **Ansible** | Agentless, SSH |
| **Puppet** | Agent-based |
| **Chef** | Ruby DSL |

---

## Exercices pratiques — OpenTofu + Proxmox

### 1️⃣ Installation d'OpenTofu

```bash
# Windows
choco install opentofu

# Mac
brew install opentofu

# Vérification
tofu version
```

### 2️⃣ Structure du projet

```bash
touch provider.tf main.tf variables.tf terraform.tfvars
```

```
mon-projet/
├── provider.tf       # Configuration du provider Proxmox
├── main.tf           # Ressource VM
├── variables.tf      # Déclaration des variables
└── terraform.tfvars  # Valeurs (⚠️ Ne pas commiter !)
```

### 3️⃣ provider.tf

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

### 4️⃣ main.tf — VM Cloud-Init

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

  os_type   = "cloud-init"
  ipconfig0 = var.pm_ipconfig0
  nameserver = var.pm_nameserver

  ciuser  = "ubuntu"
  sshkeys = <<EOF
  ${file("~/.ssh/ma_cle.pub")}
  ${file("~/.ssh/cle_publique_du_prof.pub")}
  EOF
}
```

### 5️⃣ variables.tf

```hcl
variable "pm_vm_name"    { type = string }
variable "pm_ipconfig0"  { type = string }
variable "pm_nameserver" { type = string }
variable "pm_url"        { type = string }
variable "pm_token_id"   { type = string }
variable "pm_token_secret" {
  type      = string
  sensitive = true
}
```

### 6️⃣ terraform.tfvars

```hcl
pm_vm_name      = "vm300148094"
pm_ipconfig0    = "ip=10.7.237.xxx/23,gw=10.7.237.1"
pm_nameserver   = "10.7.237.3"
pm_url          = "https://10.7.237.xx:8006/api2/json"
pm_token_id     = "tofu@pve!opentofu"
pm_token_secret = "VOTRE-SECRET-ICI"
```

> ⚠️ **Ne jamais commiter ce fichier dans Git !** Ajouter `terraform.tfvars` au `.gitignore`.

### 7️⃣ Initialisation et déploiement

```bash
tofu init     # Télécharge les providers
tofu plan     # Prévisualise les changements
tofu apply    # Applique (répondre "yes")
```

### 8️⃣ Connexion SSH à la VM

```bash
# Linux / Mac
ssh -i ~/.ssh/ma_cle.pk \
  -o StrictHostKeyChecking=no \
  ubuntu@10.7.237.xxx

# PowerShell (Windows)
ssh -i ~/.ssh/ma_cle.pk `
  -o StrictHostKeyChecking=no `
  ubuntu@10.7.237.xxx
```

---

## Bonnes pratiques

- ✅ **Versionner** toute l'infrastructure avec Git
- ✅ **Ne jamais modifier** manuellement en production
- ✅ **Séparer** les environnements dev / test / prod
- ✅ **Sécuriser** les variables et secrets (`.tfvars` dans `.gitignore`)
- ✅ **La documentation = le code** lui-même

---

## IaC et DevOps

L'IaC est un **pilier fondamental du DevOps** :

```
CI/CD  →  Déploiement continu  →  Scalabilité  →  Résilience  →  SRE
```

> 🔑 *Sans IaC, le DevOps n'est pas viable à grande échelle.*

---

## Objectifs pédagogiques

À la fin de ce module, l'étudiant(e) sera capable de :

- [ ] Expliquer le concept d'IaC
- [ ] Distinguer script système et IaC
- [ ] Décrire une infrastructure de manière déclarative
- [ ] Utiliser OpenTofu pour créer une VM sur Proxmox
- [ ] Automatiser un déploiement système complet

---

## 💬 Conclusion

> *"L'Infrastructure as Code transforme l'administration système en une discipline de programmation structurée, reproductible et industrielle."*

---

*Ouail Gacem — 300148094*# 📘 Infrastructure as Code (IaC)

> **Nom :** Ouail Gacem  
> **Matricule :** 300148094  
> **Cours :** Programmation système — Administration moderne

---

## 📋 Table des matières

1. [Introduction](#introduction)
2. [Définition](#définition)
3. [Position dans la pile système](#position-dans-la-pile-système)
4. [Pourquoi utiliser l'IaC ?](#pourquoi-utiliser-liac)
5. [IaC vs Scripts classiques](#iac-vs-scripts-classiques)
6. [Approches de l'IaC](#approches-de-liac)
7. [Ce qu'on peut gérer](#ce-quon-peut-gérer)
8. [Outils courants](#outils-courants)
9. [Exercices pratiques — OpenTofu + Proxmox](#exercices-pratiques--opentofu--proxmox)
10. [Bonnes pratiques](#bonnes-pratiques)
11. [IaC et DevOps](#iac-et-devops)
12. [Objectifs pédagogiques](#objectifs-pédagogiques)

---

## Introduction

Traditionnellement, l'administration des systèmes se faisait **manuellement** :

- Installation à la main
- Configurations faites "à la souris"
- Documentation incomplète
- Environnements difficiles à reproduire

> ⚠️ **Problème majeur :** *"Ça marche sur ce serveur, mais pas sur l'autre."*

**Solution moderne → Infrastructure as Code (IaC)**

---

## Définition

**Infrastructure as Code (IaC)** est une approche de programmation système qui permet de gérer les ressources informatiques (serveurs, réseaux, services, utilisateurs, stockage) à l'aide de **fichiers de configuration versionnés** et exécutables automatiquement.

---

## Position dans la pile système

```
Applications
──────────────────────────
Services (Web, DB, DNS, AD, Containers)
──────────────────────────
Infrastructure as Code (IaC)   ◀️ Notre niveau
──────────────────────────
Shell / API OS / Hyperviseur / Cloud
──────────────────────────
Noyau (Linux / Windows)
──────────────────────────
Matériel
```

> L'IaC agit via des **API**, des **services système** et des **hyperviseurs** — sans toucher au noyau.

---

## Pourquoi utiliser l'IaC ?

### ❌ Sans IaC

| Problème | Impact |
|----------|--------|
| Erreurs humaines | Configurations incorrectes |
| Incohérences entre serveurs | Environnements instables |
| Déploiements lents | Perte de temps |
| Documentation non fiable | Difficile à reproduire |

### ✅ Avec IaC

| Avantage | Description |
|----------|-------------|
| **Reproductibilité** | Même infrastructure, partout |
| **Automatisation** | Déploiement sans intervention manuelle |
| **Versionnement** | Git = historique + rollback |
| **Fiabilité** | Moins d'erreurs humaines |
| **Rapidité** | Déploiement en minutes |
| **Auditabilité** | Tout est traçable |

---

## IaC vs Scripts classiques

### Scripts système (impératif)

```bash
apt update
apt install nginx
systemctl start nginx
```

- Dépend de l'ordre d'exécution
- Difficile à maintenir
- Non idempotent

### IaC (déclaratif)

```hcl
resource "nginx_server" {
  version = "1.24"
  port    = 80
}
```

- Décrit l'**état final** souhaité
- L'outil décide comment y arriver
- Idempotent ✔️

---

## Approches de l'IaC

### 🟢 Déclaratif (recommandé)

> *"Voici l'état voulu"*

- **Terraform / OpenTofu**
- **CloudFormation**
- **Kubernetes YAML**

✔ Reproductible &nbsp; ✔ Idempotent &nbsp; ✔ Facile à maintenir

### 🟡 Impératif

> *"Fais ceci, puis cela"*

- **Scripts shell**
- **Ansible** (mixte)

✔ Flexible &nbsp; ✖ Plus complexe à maintenir

---

## Ce qu'on peut gérer

- 🖥️ Machines virtuelles
- 🌐 Réseaux (VLAN, bridges, firewall)
- 💾 Stockage
- 👤 Utilisateurs et permissions
- ⚙️ Services (web, DB, DNS)
- 📦 Containers
- 🧩 Clusters
- ☁️ Infrastructure cloud (AWS, Azure, GCP)
- 🏠 Infrastructure locale (Proxmox, VMware)

> 💡 **L'infrastructure devient un programme.**

---

## Outils courants

### Orchestration

| Outil | Usage |
|-------|-------|
| **Terraform / OpenTofu** | Multi-cloud, local |
| **CloudFormation** | AWS natif |
| **Pulumi** | Code natif (Python, JS...) |

### Configuration

| Outil | Usage |
|-------|-------|
| **Ansible** | Agentless, SSH |
| **Puppet** | Agent-based |
| **Chef** | Ruby DSL |

---

## Exercices pratiques — OpenTofu + Proxmox

### 1️⃣ Installation d'OpenTofu

```bash
# Windows
choco install opentofu

# Mac
brew install opentofu

# Vérification
tofu version
```

### 2️⃣ Structure du projet

```bash
touch provider.tf main.tf variables.tf terraform.tfvars
```

```
mon-projet/
├── provider.tf       # Configuration du provider Proxmox
├── main.tf           # Ressource VM
├── variables.tf      # Déclaration des variables
└── terraform.tfvars  # Valeurs (⚠️ Ne pas commiter !)
```

### 3️⃣ provider.tf

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

### 4️⃣ main.tf — VM Cloud-Init

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

  os_type   = "cloud-init"
  ipconfig0 = var.pm_ipconfig0
  nameserver = var.pm_nameserver

  ciuser  = "ubuntu"
  sshkeys = <<EOF
  ${file("~/.ssh/ma_cle.pub")}
  ${file("~/.ssh/cle_publique_du_prof.pub")}
  EOF
}
```

### 5️⃣ variables.tf

```hcl
variable "pm_vm_name"    { type = string }
variable "pm_ipconfig0"  { type = string }
variable "pm_nameserver" { type = string }
variable "pm_url"        { type = string }
variable "pm_token_id"   { type = string }
variable "pm_token_secret" {
  type      = string
  sensitive = true
}
```

### 6️⃣ terraform.tfvars

```hcl
pm_vm_name      = "vm300148094"
pm_ipconfig0    = "ip=10.7.237.xxx/23,gw=10.7.237.1"
pm_nameserver   = "10.7.237.3"
pm_url          = "https://10.7.237.xx:8006/api2/json"
pm_token_id     = "tofu@pve!opentofu"
pm_token_secret = "VOTRE-SECRET-ICI"
```

> ⚠️ **Ne jamais commiter ce fichier dans Git !** Ajouter `terraform.tfvars` au `.gitignore`.

### 7️⃣ Initialisation et déploiement

```bash
tofu init     # Télécharge les providers
tofu plan     # Prévisualise les changements
tofu apply    # Applique (répondre "yes")
```

### 8️⃣ Connexion SSH à la VM

```bash
# Linux / Mac
ssh -i ~/.ssh/ma_cle.pk \
  -o StrictHostKeyChecking=no \
  ubuntu@10.7.237.xxx

# PowerShell (Windows)
ssh -i ~/.ssh/ma_cle.pk `
  -o StrictHostKeyChecking=no `
  ubuntu@10.7.237.xxx
```

---

## Bonnes pratiques

- ✅ **Versionner** toute l'infrastructure avec Git
- ✅ **Ne jamais modifier** manuellement en production
- ✅ **Séparer** les environnements dev / test / prod
- ✅ **Sécuriser** les variables et secrets (`.tfvars` dans `.gitignore`)
- ✅ **La documentation = le code** lui-même

---

## IaC et DevOps

L'IaC est un **pilier fondamental du DevOps** :

```
CI/CD  →  Déploiement continu  →  Scalabilité  →  Résilience  →  SRE
```

> 🔑 *Sans IaC, le DevOps n'est pas viable à grande échelle.*

---

## Objectifs pédagogiques

À la fin de ce module, l'étudiant(e) sera capable de :

- [ ] Expliquer le concept d'IaC
- [ ] Distinguer script système et IaC
- [ ] Décrire une infrastructure de manière déclarative
- [ ] Utiliser OpenTofu pour créer une VM sur Proxmox
- [ ] Automatiser un déploiement système complet

---

## 💬 Conclusion

> *"L'Infrastructure as Code transforme l'administration système en une discipline de programmation structurée, reproductible et industrielle."*

---
