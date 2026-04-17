##300148094

⚙️ DevOps Batch System Monitor (PowerShell on Linux)
GitHub repo size GitHub stars GitHub last commit License PowerShell Platform

🎯 Overview
This project is a DevOps automation batch script built with PowerShell (pwsh) on Linux.

It performs system monitoring and generates structured reports in both text and JSON formats.

🚀 Features
✔ System monitoring (CPU, Memory, Disk) ✔ Network connectivity check (SSH) ✔ Automated report generation (TXT + JSON) ✔ Object-oriented pipeline (PowerShell) ✔ Cross-platform DevOps scripting

📸 Sample Output
===== RAPPORT DEVOPS =====
Date : 2026-04-13
Utilisateur : user
Machine : ubuntu

Top 5 processus CPU :
nginx - CPU: 25
python - CPU: 18

Espace disque :
/dev/sda1  40G  20G  50%

Test SSH :
Résultat : OK
📂 Project Structure
/devops-batch/
├── devops_batch.ps1
├── rapport.txt
└── rapport.json
Capture d'écran 2026-04-13 110148
⚙️ Requirements
Ubuntu 22.04 (Jammy)
PowerShell Core (pwsh)
SSH client installed
🔧 Installation
1. Install PowerShell
sudo apt update
sudo apt install -y powershell
2. Create project directory
sudo mkdir /devops-batch
3. Create script
sudo nano /devops-batch/devops_batch.ps1
▶️ Usage
Run the script:

sudo pwsh /devops-batch/devops_batch.ps1
📊 Generated Reports
📄 Text Report
/devops-batch/rapport.txt
📦 JSON Report
/devops-batch/rapport.json
🧠 PowerShell Pipeline Example
Get-Process |
Where-Object {$_.CPU -gt 10} |
Select-Object ProcessName, CPU
➡️ Unlike Bash, PowerShell manipulates objects instead of raw text, making automation more reliable.

🔍 What the Script Checks
🖥️ System
Top 5 processes (CPU)
Top 5 processes (Memory)
💾 Disk
Disk usage via df -h
🌐 Network
SSH connectivity test (localhost)
⏰ Automation
Linux Cron Job
crontab -e
0 2 * * * /usr/bin/pwsh /devops-batch/devops_batch.ps1
📈 Roadmap
 Add email alerting
 Add monitoring dashboard
 Integrate with Prometheus / Grafana
 Add API export
 Multi-host monitoring
⚖️ Bash vs PowerShell
Feature	Bash	PowerShell
Data type	Text	Objects
JSON support	External tools	Native
Pipeline	Text-based	Object-based
DevOps automation	Medium	High
💡 Why PowerShell on Linux?
Cross-platform scripting (Linux + Windows)
Native JSON support
Cleaner automation pipelines
Better maintainability for DevOps scripts
🤝 Contributing
Contributions are welcome!

git fork
git checkout -b feature/new-feature
git commit -m "Add new feature"
git push origin feature/new-feature
📄 License
MIT License

👨‍💻 Author
DevOps Lab — PowerShell Automation on Linux

⭐ Support
If you find this project useful, give it a ⭐ on GitHub!
