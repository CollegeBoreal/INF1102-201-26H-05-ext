<<<<<<< HEAD
## Validation de la configuration Git
=======
\# Installation de Jupyter avec Miniforge (Windows)



\## 1. Installation de Miniforge



Installation via Chocolatey :



choco install miniforge3 -y



Installation dans :

C:\\tools\\miniforge3



---



\## 2. Configuration PowerShell



Autoriser les scripts :



Set-ExecutionPolicy RemoteSigned -Scope CurrentUser



Initialiser conda :



C:\\tools\\miniforge3\\Scripts\\conda.exe init powershell



Redémarrer PowerShell



---



\## 3. Création de l'environnement



conda create -n INF1102 python=3.12 -y

conda activate INF1102



---



\## 4. Installation de JupyterLab



conda install -c conda-forge jupyterlab -y



Lancement :



jupyter lab



---



\## Capture d'écran



Voir dossier images/777
>>>>>>> b716d91 (Ajout README installation Jupyter)

![Validation Git](images/validation_git.png)
