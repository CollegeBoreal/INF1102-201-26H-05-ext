# 6️⃣ PWSH (PowerShell) — TP DevOps

**Nom :** Syphax  
**Boréal ID :** 300151233  
**Cours :** INF1102  
**Environnement :** Ubuntu 22.04 LTS  
**Shell :** PowerShell (pwsh)

## Installation de PowerShell

```bash
sudo apt update
sudo apt install -y wget apt-transport-https software-properties-common
wget https://packages.microsoft.com/config/ubuntu/22.04/packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
sudo apt update
sudo apt install -y powershell
