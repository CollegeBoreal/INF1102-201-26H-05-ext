\# :six: PWSH (PowerShell) — TP DevOps



\*\*Nom :\*\* Hani Aghilas Damouche

\*\*Boréal ID :\*\* 300150557

\*\*Cours :\*\* INF1102

\*\*Environnement :\*\* Ubuntu 22.04 LTS

\*\*Shell :\*\* PowerShell (pwsh)



\---



\## :floppy\_disk: Installation de PowerShell sur Ubuntu 22.04



\### 1. Mettre à jour le système



```bash

sudo apt update

```



\### 2. Installer les dépendances



```bash

sudo apt install -y wget apt-transport-https software-properties-common

```



\### 3. Ajouter le dépôt Microsoft



```bash

wget https://packages.microsoft.com/config/ubuntu/22.04/packages-microsoft-prod.deb

sudo dpkg -i packages-microsoft-prod.deb

```



\### 4. Mettre à jour les dépôts



```bash

sudo apt update

```



\### 5. Installer PowerShell



```bash

sudo apt install -y powershell

```



\### 6. Lancer PowerShell



```bash

pwsh

```



Prompt :



```

PS /home/ubuntu>

```



!\[Installation PowerShell](images/1.png)



\---



\### 7. Vérifier la version



```powershell

$PSVersionTable

```



\---



\### 8. Passage Bash → PowerShell



```bash

pwsh

```



Sortir :



```powershell

exit

```



!\[Bash vers PowerShell](images/2.png)



\---



\# :test\_tube: Laboratoire — Batch DevOps PowerShell



\## 🎯 Objectifs



\* Créer un script PowerShell sous Linux

\* Vérifier CPU, mémoire, disque

\* Tester la connectivité SSH

\* Générer des rapports TXT et JSON

\* Automatiser des tâches système



\---



\## 🔹 PARTIE 1 – Préparation



```bash

mkdir -p /home/ubuntu/devops-batch

sudo mkdir -p /devops-batch

sudo chown -R ubuntu:ubuntu /devops-batch

```



\---



\## 🔹 PARTIE 2 – Création du script



```bash

nano /home/ubuntu/devops-batch/devops\_batch.ps1

```



Shebang :



```powershell

\#!/usr/bin/env pwsh

```



\---



\## 🔹 PARTIE 3 – Script complet



```powershell

\#!/usr/bin/env pwsh



$rapportTxt  = "/devops-batch/rapport.txt"

$rapportJson = "/devops-batch/rapport.json"



$date     = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

$hostname = hostname

$user     = whoami



Write-Output "===== RAPPORT DEVOPS =====" | Tee-Object $rapportTxt

Write-Output "Date : $date" | Tee-Object -Append $rapportTxt

Write-Output "Utilisateur : $user" | Tee-Object -Append $rapportTxt

Write-Output "Machine : $hostname" | Tee-Object -Append $rapportTxt



$topCPU = Get-Process | Sort-Object CPU -Descending | Select-Object -First 5

$topMem = Get-Process | Sort-Object WS -Descending | Select-Object -First 5

$disk = df -h



$sshHost = "127.0.0.1"

try {

&#x20;   $sshResult = ssh -o BatchMode=yes -o ConnectTimeout=5 $sshHost "echo OK"

} catch {

&#x20;   $sshResult = "FAILED"

}



$reportObj = \[PSCustomObject]@{

&#x20;   Date = $date

&#x20;   User = $user

&#x20;   Host = $hostname

&#x20;   CPU  = $topCPU

&#x20;   Memory = $topMem

&#x20;   Disk = $disk

&#x20;   SSH = $sshResult

}



$reportObj | ConvertTo-Json -Depth 5 | Set-Content $rapportJson

```



\---



\## 🔹 PARTIE 4 – Exécution



```bash

pwsh /home/ubuntu/devops-batch/devops\_batch.ps1

```



Résultat :



\* création de `rapport.txt`

\* création de `rapport.json`



!\[Execution](images/3.png)



\---



\## 🔹 PARTIE 5 – Correction SSH



```bash

ssh-keyscan -H 127.0.0.1 >> \~/.ssh/known\_hosts

ssh-keygen -t rsa -b 4096 -N "" -f \~/.ssh/id\_rsa

cat \~/.ssh/id\_rsa.pub >> \~/.ssh/authorized\_keys

chmod 600 \~/.ssh/authorized\_keys

```



\---



\## 🔹 PARTIE 6 – Résultat final



```bash

ls -l /devops-batch

cat /devops-batch/rapport.txt

```



!\[Rapports](images/4.png)



\---



\## 📁 Structure finale



```

6.PWSH/

└── 300150557/

&#x20;   ├── README.md

&#x20;   ├── devops\_batch.ps1

&#x20;   └── images/

&#x20;       ├── 1.png

&#x20;       ├── 2.png

&#x20;       ├── 3.png

&#x20;       ├── 4.png

&#x20;       └── 5.png

```



\---



\## 💡 Conclusion



PowerShell sous Linux permet :



\* une automatisation multi-plateforme

\* une gestion orientée objets

\* une meilleure intégration DevOps

\* une génération facile de JSON



👉 C’est plus puissant que Bash pour les scripts complexes.



