

```terraforms
pm_vm_name      = "vm300151403"   
pm_ipconfig0    = "ip=10.7.237.238/23,gw=10.7.237.1"
pm_nameserver   = "10.7.237.3"    

pm_url          = "https://10.7.237.38:8006/api2/json"
pm_token_id     = "tofu@pve!opentofu"
pm_token_secret = "f2097a3c-f9f0-xxxx-9a43-5cxxxe"
```
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
# Download cloud image
wget https://cloud-images.ubuntu.com/jammy/current/jammy-server-cloudimg-amd64.img

# Create VM
qm create 9000 --name ubuntu-jammy-template --memory 2048 --cores 2 --net0 virtio,bridge=vmbr0

# Import disk
qm importdisk 9000 jammy-server-cloudimg-amd64.img local-lvm

# Attach disk
qm set 9000 --scsihw virtio-scsi-pci --scsi0 local-lvm:vm-9000-disk-0

# Cloud-init disk
qm set 9000 --ide2 local-lvm:cloudinit

# Boot settings
qm set 9000 --boot c --bootdisk scsi0
qm set 9000 --serial0 socket --vga serial0

# Convert to template
qm template 9000
```

## 🏗️ Installation

- [ ] [💻 Proxmox VE Installation – HP ProLiant DL360 G6](https://github.com/CollegeBoreal/Laboratoires/tree/main/D.DC/S.Servers/Proliant/Proxmox)



