
# INF1102 – Jupyter

## Installation de Jupyter avec Miniforge

1. Installation de Miniforge :

choco install miniforge3 -y

Installation dans :
C:\tools\miniforge3

---

2. Configuration PowerShell :

Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

C:\tools\miniforge3\Scripts\conda.exe init powershell

Redémarrer PowerShell.

---

3. Création de l’environnement :

conda create -n INF1102 python=3.12 -y
conda activate INF1102

---

4. Installation et lancement de Jupyter :

conda install -c conda-forge jupyterlab -y
jupyter lab

---

Validation :

- L’environnement INF1102 fonctionne.
- JupyterLab démarre correctement.