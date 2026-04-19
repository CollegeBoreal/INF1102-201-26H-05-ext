# 🧪 TP — Batch DevOps PowerShell sous Linux (Ubuntu 22.04)

> **Nom :** Ouail Gacem  
> **Matricule :** 300148094  
> **Cours :** Programmation système — Administration Linux & DevOps

---

## 📋 Table des matières

1. [Objectif du laboratoire](#objectif-du-laboratoire)
2. [Environnement utilisé](#environnement-utilisé)
3. [Installation de PowerShell sur Ubuntu 22.04](#installation-de-powershell-sur-ubuntu-2204)
4. [Travail réalisé](#travail-réalisé)
   - [Partie 1 — Préparation de l'environnement](#partie-1--préparation-de-lenvironnement)
   - [Partie 2 — Création du script principal](#partie-2--création-du-script-principal)
   - [Partie 3 — Code complet du script](#partie-3--code-complet-du-script)
   - [Partie 4 — Exécution du batch](#partie-4--exécution-du-batch)
   - [Partie 5 — Structure finale du projet](#partie-5--structure-finale-du-projet)
5. [Pourquoi PowerShell sous Linux ?](#pourquoi-powershell-sous-linux-)
6. [Comparatif Bash vs PowerShell](#comparatif-bash-vs-powershell)
7. [Conclusion](#conclusion)

---

## 🎯 Objectif du laboratoire

Dans ce TP, j'ai créé un **script batch DevOps en PowerShell** fonctionnant sous Linux (Ubuntu 22.04). Ce script automatise plusieurs tâches d'administration système :

- Vérifier l'état du système (CPU, mémoire, disque)
- Vérifier la connectivité réseau via SSH
- Générer un **rapport texte** et un **rapport JSON**
- Automatiser des tâches administratives et DevOps
- Comprendre le **pipeline PowerShell orienté objets**

---

## 🖥️ Environnement utilisé

- Distribution : **Ubuntu 22.04 (Jammy)**
- Shell : **PowerShell (pwsh)**
- Accès : **sudo**

> ⚠️ Sous Ubuntu 22.04, PowerShell n'est **pas** dans les dépôts officiels. Il faut ajouter le dépôt Microsoft manuellement.

---

## 💾 Installation de PowerShell sur Ubuntu 22.04

Voici les étapes que j'ai suivies pour installer PowerShell :

**1. Mettre à jour le système :**

```bash
sudo apt update
```

**2. Installer les dépendances :**

```bash
sudo apt install -y wget apt-transport-https software-properties-common
```

**3. Télécharger et installer le dépôt Microsoft :**

```bash
wget https://packages.microsoft.com/config/ubuntu/22.04/packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
```

**4. Mettre à jour les dépôts :**

```bash
sudo apt update
```

**5. Installer PowerShell :**

```bash
sudo apt install -y powershell
```

**6. Lancer PowerShell :**

```bash
pwsh
```

Le prompt change alors pour :

```
PS /home/user>
```

**7. Vérifier la version installée :**

```powershell
$PSVersionTable
```

---

## 🛠️ Travail réalisé

### Partie 1 — Préparation de l'environnement

J'ai créé le dossier de travail pour le TP :

```bash
sudo mkdir /devops-batch
```

Ce dossier contiendra le script, le rapport texte et le rapport JSON.

---

### Partie 2 — Création du script principal

J'ai créé le fichier du script avec `nano` :

```bash
sudo nano /devops-batch/devops_batch.ps1
```

La première ligne du fichier est le **shebang** pour indiquer à Linux d'utiliser PowerShell :

```powershell
#!/usr/bin/env pwsh
```

---

### Partie 3 — Code complet du script

Voici le script complet que j'ai intégré dans `devops_batch.ps1` :

```powershell
#!/usr/bin/env pwsh

# =========================
# Batch DevOps PowerShell
# =========================

# Variables
$rapportTxt  = "/devops-batch/rapport.txt"
$rapportJson = "/devops-batch/rapport.json"
$hostname    = hostname
$user        = whoami
$date        = Get-Date

# Création du rapport texte
Write-Output "===== RAPPORT DEVOPS =====" | Tee-Object $rapportTxt
Write-Output "Date : $date"              | Tee-Object -FilePath $rapportTxt -Append
Write-Output "Utilisateur : $user"       | Tee-Object -FilePath $rapportTxt -Append
Write-Output "Machine : $hostname"       | Tee-Object -FilePath $rapportTxt -Append
Write-Output ""                          | Tee-Object -FilePath $rapportTxt -Append

# =========================
# Vérification CPU & mémoire
# =========================
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

# =========================
# Vérification disque
# =========================
Write-Output "" | Tee-Object -FilePath $rapportTxt -Append
Write-Output "Espace disque :" | Tee-Object -FilePath $rapportTxt -Append
$disk = df -h
Write-Output $disk | Tee-Object -FilePath $rapportTxt -Append

# =========================
# Vérification SSH
# =========================
Write-Output "" | Tee-Object -FilePath $rapportTxt -Append
$sshHost = "127.0.0.1"
Write-Output "Test SSH vers $sshHost :" | Tee-Object -FilePath $rapportTxt -Append
try {
    $result = ssh -o BatchMode=yes -o ConnectTimeout=5 $sshHost "echo 'OK'" 2>&1
    Write-Output "Résultat : $result" | Tee-Object -FilePath $rapportTxt -Append
} catch {
    Write-Output "SSH échoué vers $sshHost" | Tee-Object -FilePath $rapportTxt -Append
}

# =========================
# Génération JSON
# =========================
$reportObj = [PSCustomObject]@{
    Date        = $date
    Utilisateur = $user
    Machine     = $hostname
    TopCPU      = $topCPU | ForEach-Object { @{ Process = $_.ProcessName; CPU    = $_.CPU } }
    TopMemory   = $topMem | ForEach-Object { @{ Process = $_.ProcessName; Memory = $_.WorkingSet } }
    Disk        = $disk
}

$reportObj | ConvertTo-Json -Depth 5 | Set-Content $rapportJson

Write-Output ""
Write-Output "Rapports générés : $rapportTxt et $rapportJson"
```

**Explication des sections du script :**

| Section | Rôle |
|---------|------|
| Variables | Définit les chemins des rapports, l'utilisateur, la machine et la date |
| `Tee-Object` | Affiche dans la console **et** écrit dans le fichier en même temps |
| `Get-Process` | Récupère la liste des processus actifs sous forme d'**objets** |
| `Sort-Object CPU` | Trie les processus par consommation CPU décroissante |
| `Sort-Object WS` | Trie par consommation mémoire (Working Set) décroissante |
| `df -h` | Appelle la commande Linux pour lister l'espace disque |
| `ssh ... "echo 'OK'"` | Teste la connectivité SSH vers localhost avec timeout |
| `try / catch` | Gestion d'erreur si le SSH échoue |
| `[PSCustomObject]` | Crée un objet structuré pour le rapport JSON |
| `ConvertTo-Json -Depth 5` | Convertit l'objet en JSON lisible par des API ou scripts |

---

### Partie 4 — Exécution du batch

J'ai exécuté le script avec les droits sudo :

```bash
sudo pwsh /devops-batch/devops_batch.ps1
```

**Résultat attendu dans la console :**

```
===== RAPPORT DEVOPS =====
Date : 02/05/2026 15:30:00
Utilisateur : ubuntu
Machine : mon-serveur

Top 5 processus par CPU :
pwsh - CPU: 12.5
sshd - CPU: 0.8
...

Espace disque :
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        20G  5.2G   14G  28% /
...

Test SSH vers 127.0.0.1 :
Résultat : OK

Rapports générés : /devops-batch/rapport.txt et /devops-batch/rapport.json
```

J'ai vérifié le contenu des fichiers générés :

```bash
cat /devops-batch/rapport.txt
cat /devops-batch/rapport.json
```

---

### Partie 5 — Structure finale du projet

Après l'exécution complète du script, voici la structure du dossier :

```
/devops-batch/
│
├── devops_batch.ps1      # Script principal PowerShell
├── rapport.txt           # Rapport texte généré automatiquement
└── rapport.json          # Rapport JSON généré automatiquement
```

---

## 💡 Pourquoi PowerShell sous Linux ?

### 1. Automatisation multi-plateforme

PowerShell fonctionne sur **Windows, Linux et macOS**. Les mêmes scripts peuvent s'exécuter sur plusieurs OS avec peu ou pas de modification — très utile dans un environnement mixte (Windows + Ubuntu + RedHat).

### 2. Pipeline orienté objets

Contrairement à Bash qui travaille avec du **texte brut**, PowerShell travaille avec des **objets .NET** :

```powershell
Get-Process | Where-Object {$_.CPU -gt 10} | Select-Object ProcessName, CPU
```

Chaque commande renvoie un objet structuré, ce qui facilite le filtrage, la sélection et l'exportation sans parsing complexe.

### 3. Intégration avec les API et services

PowerShell peut appeler des **API REST**, manipuler du **JSON** et du **XML** directement. Cela permet d'automatiser des tâches DevOps avec Azure, AWS, ou d'autres plateformes depuis Linux.

### 4. Scripts plus robustes et maintenables

Avec des **variables typées**, des **fonctions** et des **modules**, PowerShell permet de structurer les scripts comme de vrais programmes — bien plus facile à maintenir que des scripts Bash complexes.

---

## 📊 Comparatif Bash vs PowerShell

| Fonctionnalité | Bash | PowerShell | Avantage |
|----------------|------|------------|---------|
| Type de données | Texte (strings) | Objets (.NET) | Filtrage et export sans parsing |
| Filtrage | `grep` / `awk` | `Where-Object {$_.CPU -gt 10}` | Plus lisible et robuste |
| Export JSON | `jq` (externe) | `ConvertTo-Json` (natif) | Prêt pour les API DevOps |
| Boucles | `for i in *; do...; done` | `foreach ($f in Get-ChildItem)` | Accès direct aux propriétés |
| Variables typées | Non (string par défaut) | Oui (`[int]$count = 5`) | Moins d'erreurs, meilleure maintenance |
| Gestion fichiers | `cp`, `mv`, `rm`, `tar` | `Copy-Item`, `Move-Item`, `Compress-Archive` | Commandes cohérentes et cross-platform |
| Multi-plateforme | Linux / macOS seulement | Linux + Windows + macOS | Portabilité totale |

**Exemple concret — Générer un rapport des processus :**

```bash
# Bash
ps aux --sort=-%mem | head -n 5 > top_mem.txt
df -h >> top_mem.txt
```

```powershell
# PowerShell — résultat directement en JSON
$report = [PSCustomObject]@{
    TopMemory = Get-Process | Sort-Object WS -Descending | Select-Object -First 5 Name, WS
    Disk      = df -h
}
$report | ConvertTo-Json | Set-Content report.json
```

> PowerShell produit un **JSON prêt à l'emploi**, sans étape de parsing supplémentaire.

---
<img width="1920" height="1080" alt="Screenshot (381)" src="https://github.com/user-attachments/assets/bc598e2d-8fa3-4cfe-b699-cf137089438c" />
<img width="1920" height="1080" alt="Screenshot (380)" src="https://github.com/user-attachments/assets/0dc16c2a-f0b8-418d-8d3b-69fc63993097" />
<img width="1920" height="1080" alt="Screenshot (379)" src="https://github.com/user-attachments/assets/d5726dfe-5a5c-43c3-947a-0f7423acfe98" />
<img width="1920" height="1080" alt="Screenshot (382)" src="https://github.com/user-attachments/assets/eb5475e7-31f7-4989-854c-f05a7cc99245" />
<img width="998" height="474" alt="Screenshot 2026-04-17 013915" src="https://github.com/user-attachments/assets/5d063dae-b09c-4c09-9579-b250c696102f" />

## 💬 Conclusion

Grâce à ce laboratoire, j'ai appris à :

- Installer **PowerShell sur Ubuntu 22.04** en ajoutant le dépôt Microsoft
- Écrire un **script batch DevOps complet** en PowerShell sous Linux
- Utiliser le **pipeline orienté objets** (`Get-Process`, `Sort-Object`, `Select-Object`)
- Générer des **rapports texte et JSON** automatiquement
- Tester la **connectivité SSH** avec gestion d'erreurs (`try/catch`)
- Comprendre les **avantages de PowerShell** face à Bash pour le DevOps

> 💡 *PowerShell sous Linux combine la puissance de Windows avec la flexibilité de Linux — idéal pour l'automatisation DevOps multi-plateforme.*

---

*Ouail Gacem — 300148094*




