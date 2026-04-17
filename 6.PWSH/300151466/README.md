
# :six: PWSH (PowerShell) — TP DevOps


**Nom :** adel bennacer

**Boréal ID :** 300151466

**Cours :** INF1105

**Environnement :** Ubuntu 22.04 LTS

**Shell :** PowerShell (pwsh)

---

## :floppy_disk: Installation de PowerShell sur Ubuntu 22.04

### 1. Mettre à jour le système
<img width="568" height="182" alt="c7" src="https://github.com/user-attachments/assets/a06af502-e056-4acc-834a-8907d753fa3b" />
```bash
sudo apt update
```<img width="598" height="444" alt="c6" src="https://github.com/user-attachments/assets/d4c9cdb9-3ed5-42d8-8f23-0c231f27578c" />

### 2. Installer les dépendances

```bash
sudo apt install -y wget apt-transport-https software-properties-common
```
<img width="568" height="182" alt="c7" src="https://github.com/user-attachments/assets/c0802a6b-0de9-4952-b90f-df2454f6427b" />



### 3. Ajouter le dépôt Microsoft

```bash
wget https://packages.microsoft.com/config/ubuntu/22.04/packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
```

### 4. Mettre à jour les dépôts

```bash
sudo apt update
```
<img width="449" height="79" alt="c8" src="https://github.com/user-attachments/assets/bc0fd460-f431-4306-bb04-9f48f53357c8" />

### 5. Installer PowerShell

```bash
sudo apt install -y powershell
```

### 6. Lancer PowerShell

```bash
pwsh
```

Prompt :

```
PS /home/ubuntu>
```

![Installation de PowerShell](images/1.png)

### 7. Vérifier la version

```powershell
$PSVersionTable
```

### 8. Passage de Bash à PowerShell

Depuis un terminal Bash classique :


1. Créer un **script batch PowerShell** pour Linux.
2. Vérifier l'état du système (CPU, mémoire, disque).
3. Vérifier la connectivité réseau (SSH).
4. Générer un **rapport texte et JSON**.
5. Automatiser des tâches **administratives et DevOps**.
6. Comprendre le pipeline **PowerShell orienté objets**.

---

## 🔹 PARTIE 1 – Préparation de l'environnement

Création du dossier de travail :

```bash
mkdir ~/devops-batch
```

---

## 🔹 PARTIE 2 – Créer le script principal


Shebang Linux :

```powershell
#!/usr/bin/env pwsh
```

---

## 🔹 PARTIE 3 – Script complet

```powershell
#!/usr/bin/env pwsh

# =====================================
# DevOps Batch Script - INF1102
# Auteur : adel bennacer
# Boreal ID : 300151466
# =====================================

$rapportTxt  = "$HOME/devops-batch/rapport.txt"
$rapportJson = "$HOME/devops-batch/rapport.json"

if (-not (Test-Path "$HOME/devops-batch")) {
    New-Item -ItemType Directory -Path "$HOME/devops-batch" | Out-Null
}

$date     = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$hostname = hostname
$user     = whoami

Write-Output "===== RAPPORT DEVOPS =====" | Tee-Object -FilePath $rapportTxt
Write-Output "Date : $date" | Tee-Object -FilePath $rapportTxt -Append
Write-Output "Utilisateur : $user" | Tee-Object -FilePath $rapportTxt -Append
Write-Output "Machine : $hostname" | Tee-Object -FilePath $rapportTxt -Append
Write-Output "" | Tee-Object -FilePath $rapportTxt -Append

Write-Output "Top 5 processus par CPU :" | Tee-Object -FilePath $rapportTxt -Append
$topCPU = Get-Process | Sort-Object CPU -Descending | Select-Object -First 5
foreach ($p in $topCPU) {
    Write-Output ("{0} - CPU: {1}" -f $p.ProcessName, $p.CPU) | Tee-Object -FilePath $rapportTxt -Append
}

Write-Output "" | Tee-Object -FilePath $rapportTxt -Append
Write-Output "Top 5 processus par mémoire :" | Tee-Object -FilePath $rapportTxt -Append
$topMem = Get-Process | Sort-Object WS -Descending | Select-Object -First 5
foreach ($p in $topMem) {
    Write-Output ("{0} - Mémoire: {1}" -f $p.ProcessName, $p.WorkingSet) | Tee-Object -FilePath $rapportTxt -Append
}

Write-Output "" | Tee-Object -FilePath $rapportTxt -Append
Write-Output "Espace disque :" | Tee-Object -FilePath $rapportTxt -Append
$disk = df -h
Write-Output $disk | Tee-Object -FilePath $rapportTxt -Append

Write-Output "" | Tee-Object -FilePath $rapportTxt -Append
$sshHost = "127.0.0.1"
Write-Output "Test SSH vers $sshHost :" | Tee-Object -FilePath $rapportTxt -Append
try {
    $result = ssh -o BatchMode=yes -o ConnectTimeout=5 $sshHost "echo OK" 2>&1
    Write-Output "Résultat : $result" | Tee-Object -FilePath $rapportTxt -Append
}
catch {
    Write-Output "SSH échoué vers $sshHost" | Tee-Object -FilePath $rapportTxt -Append
}

Write-Output "" | Tee-Object -FilePath $rapportTxt -Append

$reportObj = [PSCustomObject]@{
    Date        = $date
    Utilisateur = $user
    Machine     = $hostname
    TopCPU      = $topCPU | ForEach-Object {
        [PSCustomObject]@{ Process = $_.ProcessName; CPU = $_.CPU }
    }
    TopMemory   = $topMem | ForEach-Object {
        [PSCustomObject]@{ Process = $_.ProcessName; Memory = $_.WorkingSet }
    }
    Disk        = $disk
}

$reportObj | ConvertTo-Json -Depth 5 | Set-Content $rapportJson

Write-Output ""
Write-Output "Rapports générés : $rapportTxt et $rapportJson"
```

---

## 🔹 PARTIE 4 – Exécuter le batch

```bash
pwsh ./devops_batch.ps1
```

Résultat obtenu :



Top 5 processus par mémoire :
pwsh - Mémoire: 188960768
pwsh - Mémoire: 104501248
snapd - Mémoire: 39628800
multipathd - Mémoire: 27881472
systemd-journald - Mémoire: 24113152

Espace disque :
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       9.6G  5.6G  4.0G  59% /

Test SSH vers 127.0.0.1 :
Résultat : OK

Rapports générés : /home/ubuntu/devops-batch/rapport.txt
                   /home/ubuntu/devops-batch/rapport.json
```

![Exécution du script](images/3.png)

---

## 🔹 PARTIE 5 – Résolution des erreurs SSH

Avant que le test SSH retourne `OK`, deux étapes ont été nécessaires :

**1. Accepter la clé du serveur local :**

```bash
ssh-keyscan -H 127.0.0.1 >> ~/.ssh/known_hosts
```

**2. Autoriser la clé publique locale :**

```bash
ssh-keygen -t rsa -b 4096 -N "" -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
```

---

| **Variables typées** | Non typées | `[int]$count = 5` | Moins d'erreurs, meilleure maintenance |
| **Multi-plateforme** | Linux/macOS | Linux + Windows + macOS | Même script sur tous les OS |
