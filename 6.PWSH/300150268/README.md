\# TP PWSH – Batch DevOps PowerShell

\## 300150268 | IP: 10.7.237.230



\## 💾 Installation PowerShell

\- Ubuntu 22.04 LTS

\- PowerShell 7.6.0
capt=============1============================
<img width="960" height="1020" alt="ssh5" src="https://github.com/user-attachments/assets/eff8dd5f-ff5a-4393-80d0-64a6847079a4" />
capt=======================2================
<img width="960" height="1020" alt="ssh4" src="https://github.com/user-attachments/assets/a351b427-8ef5-4c93-a5f3-96dd8f84873f" />
capt=====================3=================
<img width="956" height="644" alt="ssh3" src="https://github.com/user-attachments/assets/17c5d9f5-8d5a-49d9-a697-6f169c40603d" />
capt========================4=================
<img width="960" height="1020" alt="sssh" src="https://github.com/user-attachments/assets/8a487b30-f7cd-4d80-ace6-047fb645a5bb" />
capt================5=====================
<img width="953" height="457" alt="ssh" src="https://github.com/user-attachments/assets/c440bcdf-ca54-48a6-bc64-4fdd59136bf8" />


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

