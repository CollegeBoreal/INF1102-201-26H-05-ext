<!-- AWS-STYLE DEVOPS DASHBOARD README -->

<p align="center">
  <img src="https://media.giphy.com/media/kH1DBkPNyZPOk0BxrM/giphy.gif" width="120" />
</p>

<h1 align="center">☁️ DevOps Infrastructure Dashboard – OpenTofu / Proxmox</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Cloud-IaC-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/OpenTofu-Terraform%20Compatible-4CAF50?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Proxmox-VE7-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/DevOps-Automation-purple?style=for-the-badge" />
</p>

---

# 📊 AWS-LIKE INFRASTRUCTURE DASHBOARD

<p align="center">
  <img src="https://media.giphy.com/media/3o7TKsQ8U9O5f1Z5cE/giphy.gif" width="80%" />
</p>

---

## 🟢 SYSTEM STATUS (REAL-TIME SIMULATION)

| Component           | Status    | Load |
| ------------------- | --------- | ---- |
| 🖥️ Proxmox Cluster | 🟢 Online | 32%  |
| ☁️ OpenTofu Engine  | 🟢 Active | 18%  |
| 🔐 API Gateway      | 🟢 Secure | 12%  |
| 🌐 Network Layer    | 🟢 Stable | 25%  |

---

## 🏗️ ARCHITECTURE OVERVIEW

```mermaid
flowchart LR
A[Developer Code] --> B[OpenTofu Plan]
B --> C[Proxmox API]
C --> D[VM Provisioning]
D --> E[Cloud-Init Setup]
E --> F[Running Infrastructure]
F --> G[Monitoring Dashboard]
```

---

## ⚙️ INFRASTRUCTURE PIPELINE (CI/CD STYLE)

<p align="center">
  <img src="https://media.giphy.com/media/13HgwGsXF0aiGY/giphy.gif" width="70%" />
</p>

```
Git Push → OpenTofu Init → Plan → Apply → Proxmox VM → Cloud Init → SSH Ready 🚀
```

---

## 🖥️ VIRTUAL MACHINE FACTORY

```hcl
pm_vm_name      = "vm300151403"
pm_ipconfig0    = "ip=10.7.237.238/23,gw=10.7.237.1"
pm_nameserver   = "10.7.237.3"
```

✔ Auto provisioning
✔ Static IP assignment
✔ SSH key injection
✔ Cloud-init automation

---

## 🔐 SECURITY LAYER

* 🔑 API Token authentication
* 🔒 SSH Key-based access
* 🚫 No plaintext secrets in repo
* 🧱 Firewall rules via Proxmox

---

## 📡 LIVE MONITORING (SIMULATED)

<p align="center">
  <img src="https://media.giphy.com/media/l0HlNQ03J5JxX6lva/giphy.gif" width="60%" />
</p>

* CPU Usage 📊
* Memory Usage 🧠
* Network Traffic 🌐
* VM Health 🟢

---

## ☁️ CLOUD LAYER (PROXMOX VE 7)

* VM Templates (Ubuntu Cloud Image)
* API-driven provisioning
* LVM storage backend
* Virtual bridge networking (vmbr0)

---

## 🚀 DEPLOYMENT COMMANDS

```bash
# Initialize
opentofu init

# Plan infrastructure
opentofu plan

# Deploy
opentofu apply
```

---

## 📦 PROJECT STRUCTURE

```
📁 3.IaC
 ├── provider.tf
 ├── main.tf
 ├── variables.tf
 ├── terraform.tfvars
 └── README.md
```

---

## 🧠 DEVOPS THINKING MODEL

> "Infrastructure is code. Everything is reproducible. Nothing is manual."

---

## 🎯 KPI DASHBOARD

| Metric          | Value  |
| --------------- | ------ |
| Deployment Time | 2m 34s |
| Success Rate    | 99.8%  |
| VM Provisioned  | 12     |
| Failures        | 0      |

---

## 🔥 AWS-STYLE VISUAL FLOW

<p align="center">
  <img src="https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif" width="70%" />
</p>

---

## 👨‍💻 AUTHOR

DevOps / Cloud Engineering Lab – INF1102

---

<p align="center">
  <img src="https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif" width="250" />
</p>
