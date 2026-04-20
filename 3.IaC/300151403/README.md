<!-- HEADER ANIMÉ -->
<p align="center">
  <img src="https://raw.githubusercontent.com/gauravghongde/social-icons/master/SVG/DevOps.svg" width="120"/>
</p>

<h1 align="center">🚀 Infrastructure as Code – OpenTofu / Proxmox Lab</h1>

<p align="center">
  <img src="https://img.shields.io/badge/OpenTofu-IaC-blue?style=for-the-badge&logo=terraform" />
  <img src="https://img.shields.io/badge/Proxmox-VE7-orange?style=for-the-badge&logo=proxmox" />
  <img src="https://img.shields.io/badge/Cloud--Init-Automation-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/DevOps-Lab-purple?style=for-the-badge&logo=githubactions" />
</p>

---

## 🌦️ PROJET_METEO / IaC LAB

Pipeline d’infrastructure automatisée basé sur **OpenTofu (Terraform-like)** pour déployer des VMs sur **Proxmox VE 7** avec Cloud-Init.

---

## 🎯 Objectif

✔ Automatiser la création de machines virtuelles  
✔ Utiliser Infrastructure as Code (IaC)  
✔ Gérer Proxmox via API  
✔ Déployer des environnements reproductibles  

---

## ⚙️ Stack technique

- 🧠 OpenTofu (Terraform compatible)
- 🖥️ Proxmox VE 7
- ☁️ Cloud-Init
- 🔐 API Token Proxmox
- 🐧 Ubuntu Cloud Image
- 🔑 SSH automation

---

## 📦 Configuration (terraform.tfvars)

```hcl
pm_vm_name      = "vm300151403"
pm_ipconfig0    = "ip=10.7.237.238/23,gw=10.7.237.1"
pm_nameserver   = "10.7.237.3"

pm_url          = "https://10.7.237.38:8006/api2/json"
pm_token_id     = "tofu@pve!opentofu"
pm_token_secret = "**************"
