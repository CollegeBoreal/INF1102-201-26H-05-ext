\# TP PWSH – Batch DevOps PowerShell

\## 300150268 | IP: 10.7.237.230



\## 💾 Installation PowerShell

\- Ubuntu 22.04 LTS

\- PowerShell 7.6.0



\## 🎯 Objectifs

\- Créer un script batch PowerShell pour Linux

\- Vérifier CPU, mémoire, disque

\- Tester SSH

\- Générer rapport texte et JSON



\## 📄 Script : devops\_batch.ps1

\- Top 5 processus par CPU

\- Top 5 processus par mémoire

\- Espace disque : df -h

\- Test SSH vers 127.0.0.1



\## 📊 Résultats

\- Machine : vm300150268

\- Utilisateur : ubuntu

\- SSH : OK

\- Rapports générés : rapport.txt et rapport.json



\## 🔍 Vérification

pwsh \~/devops-batch/devops\_batch.ps1

cat \~/devops-batch/rapport.txt

