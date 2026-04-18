# 📝 Expressions Régulières (Regex) — Analyse des logs Nginx

> **Nom :** Ouail Gacem  
> **Matricule :** 300148094  
> **Cours :** Programmation système — Traitement de texte & Automatisation

---

## 📋 Table des matières

1. [Objectif du laboratoire](#objectif-du-laboratoire)
2. [Notions théoriques — Les Regex](#notions-théoriques--les-regex)
   - [Composants de base](#composants-de-base)
   - [Patterns utiles prêts à l'emploi](#patterns-utiles-prêts-à-lemploi)
3. [Travail réalisé — TP Analyse Nginx](#travail-réalisé--tp-analyse-nginx)
   - [Structure du projet](#structure-du-projet)
   - [Partie 1 — Script PowerShell](#partie-1--script-powershell)
   - [Partie 2 — Script Python](#partie-2--script-python)
   - [Partie 3 — Automatisation avec Cron](#partie-3--automatisation-avec-cron)
   - [Partie 4 — Vérification](#partie-4--vérification)
   - [Partie 5 — Dépannage](#partie-5--dépannage)
4. [Comparatif Bash / PowerShell / Python](#comparatif-bash--powershell--python)
5. [Cheat Sheet Regex](#cheat-sheet-regex)
6. [Conclusion](#conclusion)

---

## 🎯 Objectif du laboratoire

Dans ce TP, j'ai créé deux scripts (PowerShell et Python) qui :

- Analysent le fichier `/var/log/nginx/access.log` avec des **expressions régulières**
- Extraient les IP, les codes HTTP, les erreurs 404/500 et les pages les plus visitées
- Génèrent automatiquement un **rapport texte daté**
- Peuvent être **automatisés avec cron** pour s'exécuter chaque nuit

---

## 📚 Notions théoriques — Les Regex

Une **expression régulière (Regex)** est une chaîne spéciale utilisée pour rechercher, valider ou manipuler du texte. Les principaux concepts sont identiques en Bash, PowerShell et Python, seule la syntaxe d'appel varie.

**Usages courants :** filtrer des logs, valider des emails, extraire des numéros de téléphone, nettoyer des fichiers.

---

### Composants de base

| Symbole | Signification | Exemple | Résultat |
|---------|--------------|---------|----------|
| `.` | N'importe quel caractère | `a.c` | `abc`, `a2c` |
| `*` | 0 ou plusieurs répétitions | `ab*c` | `ac`, `abc`, `abbc` |
| `+` | 1 ou plusieurs répétitions | `ab+c` | `abc`, `abbc` |
| `?` | 0 ou 1 répétition | `colou?r` | `color`, `colour` |
| `^` | Début de ligne | `^Hello` | lignes commençant par Hello |
| `$` | Fin de ligne | `end$` | lignes finissant par end |
| `[]` | Classe de caractères | `[aeiou]` | une voyelle |
| `[^]` | Négation | `[^0-9]` | tout sauf un chiffre |
| `()` | Groupement / capture | `(ab)+` | `ab`, `abab` |
| `\|` | OU logique | `chat\|chien` | "chat" ou "chien" |
| `\d` | Chiffre (0–9) | `\d\d` | `12`, `45` |
| `\w` | Lettre ou chiffre | `\w+` | `abc123` |
| `\s` | Espace | `\s+` | `" "` |
| `{n}` | Exactement n fois | `\d{3}` | `123` |
| `{n,m}` | Entre n et m fois | `\d{2,4}` | `12`, `1234` |

---

### Patterns utiles prêts à l'emploi

| Cas | Regex |
|-----|-------|
| Email | `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}` |
| Téléphone | `\d{3}-\d{3}-\d{4}` |
| Date (YYYY-MM-DD) | `\d{4}-\d{2}-\d{2}` |
| Ligne vide | `^\s*$` |
| Adresse IP | `(\d{1,3}\.){3}\d{1,3}` |
| Code HTTP | `" (\d{3}) "` |
| Page GET | `"GET ([^ ]+)` |

---

## 🛠️ Travail réalisé — TP Analyse Nginx

### Format d'une ligne du log Nginx

Avant d'écrire les scripts, j'ai analysé la structure d'une ligne typique du fichier `/var/log/nginx/access.log` :

```
192.168.1.10 - - [17/Mar/2026:14:32:10 +0000] "GET /index.html HTTP/1.1" 200 1024
```

| Champ | Regex utilisée | Extrait |
|-------|---------------|---------|
| Adresse IP | `(\d{1,3}\.){3}\d{1,3}` | `192.168.1.10` |
| Code HTTP | `" (\d{3}) "` | `200` |
| Page visitée | `"GET ([^ ]+)` | `/index.html` |
| Erreurs | `" [45]\d{2} "` | `404`, `500` |

---

### Structure du projet

```
REGEX/
├── analyse_nginx.ps1                        # Script PowerShell
├── analyse_nginx.py                         # Script Python
├── rapport_nginx_ps1_YYYY-MM-DD.txt        # Rapport généré par PowerShell
└── rapport_nginx_py_YYYY-MM-DD.txt         # Rapport généré par Python
```

---

### Partie 1 — Script PowerShell

J'ai créé le fichier `analyse_nginx.ps1` dans le dossier `REGEX/` :

```powershell
$logfile = "/var/log/nginx/access.log"
$rapport = "REGEX/rapport_nginx_ps1_$(Get-Date -Format yyyy-MM-dd).txt"

$lines = Get-Content $logfile

"📊 Rapport Nginx - $(Get-Date)" | Out-File $rapport
"----------------------------------" | Out-File $rapport -Append

# Total des requêtes
$total = $lines.Count
"Total requêtes : $total" | Out-File $rapport -Append

# Extraction des codes HTTP
$codes = $lines | ForEach-Object {
    if ($_ -match '" (\d{3}) ') { $matches[1] }
}

# Erreurs HTTP (4xx et 5xx)
$errors    = $codes | Where-Object { $_ -match '^[45]' }
$notfound  = $codes | Where-Object { $_ -eq "404" }
$servererr = $codes | Where-Object { $_ -eq "500" }

"Erreurs HTTP : $($errors.Count)"   | Out-File $rapport -Append
"Erreurs 404 : $($notfound.Count)"  | Out-File $rapport -Append
"Erreurs 500 : $($servererr.Count)" | Out-File $rapport -Append

# Top 5 des adresses IP
$ips = $lines | ForEach-Object {
    if ($_ -match '^(\d{1,3}(\.\d{1,3}){3})') { $matches[1] }
}

"`nTop 5 IP :" | Out-File $rapport -Append
$ips | Group-Object | Sort-Object Count -Descending | Select-Object -First 5 |
ForEach-Object {
    "$($_.Count) $($_.Name)" | Out-File $rapport -Append
}

# Top 5 des pages visitées
$pages = $lines | ForEach-Object {
    if ($_ -match '"GET ([^ ]+)') { $matches[1] }
}

"`nTop 5 pages :" | Out-File $rapport -Append
$pages | Group-Object | Sort-Object Count -Descending | Select-Object -First 5 |
ForEach-Object {
    "$($_.Count) $($_.Name)" | Out-File $rapport -Append
}

Write-Host "✅ Rapport généré : $rapport"
```

**Explication des étapes du script PowerShell :**

| Étape | Commande clé | Rôle |
|-------|-------------|------|
| Lecture du log | `Get-Content $logfile` | Charge toutes les lignes dans une variable |
| Extraction codes HTTP | `-match '" (\d{3}) '` | Regex qui capture le code entre guillemets |
| Filtrage erreurs | `Where-Object { $_ -match '^[45]' }` | Garde uniquement les codes 4xx et 5xx |
| Top IPs | `Group-Object \| Sort-Object Count -Descending` | Compte et trie les IP par fréquence |
| Top pages | `-match '"GET ([^ ]+)'` | Capture l'URL après GET |
| Écriture rapport | `Out-File $rapport -Append` | Ajoute chaque ligne dans le fichier |

**Exécution du script :**

```bash
pwsh ./REGEX/analyse_nginx.ps1
```

**Exemple de rapport généré (`rapport_nginx_ps1_2026-02-05.txt`) :**

```
📊 Rapport Nginx - 02/05/2026 02:00:01
----------------------------------
Total requêtes : 4872
Erreurs HTTP : 312
Erreurs 404 : 287
Erreurs 500 : 25

Top 5 IP :
152 10.7.237.226
 87 192.168.1.15
 34 172.16.0.5
 12 10.0.0.1
  8 192.168.1.20

Top 5 pages :
412 /index.html
198 /about
 87 /contact
 45 /api/v1/users
 23 /assets/style.css
```

---

### Partie 2 — Script Python

J'ai créé le fichier `analyse_nginx.py` en Python, qui fait exactement la même analyse mais avec le module `re` :

```python
import re
from collections import Counter
from datetime import datetime

logfile = "/var/log/nginx/access.log"

with open(logfile) as f:
    lines = f.readlines()

data = "".join(lines)

rapport = f"REGEX/rapport_nginx_py_{datetime.now().date()}.txt"

# Total des requêtes
total = len(lines)

# Extraction des codes HTTP
codes = re.findall(r'" (\d{3}) ', data)

# Erreurs HTTP (4xx et 5xx)
errors = [c for c in codes if c.startswith(('4', '5'))]

# Adresses IP
ips = re.findall(r'(\d{1,3}(?:\.\d{1,3}){3})', data)

# Pages visitées
pages = re.findall(r'"GET ([^ ]+)', data)

with open(rapport, "w") as f:
    f.write(f"📊 Rapport Nginx - {datetime.now()}\n")
    f.write("----------------------------------\n")
    f.write(f"Total requêtes : {total}\n")
    f.write(f"Erreurs HTTP : {len(errors)}\n")
    f.write(f"Erreurs 404 : {codes.count('404')}\n")
    f.write(f"Erreurs 500 : {codes.count('500')}\n")

    f.write("\nTop 5 IP :\n")
    for ip, count in Counter(ips).most_common(5):
        f.write(f"{count} {ip}\n")

    f.write("\nTop 5 pages :\n")
    for page, count in Counter(pages).most_common(5):
        f.write(f"{count} {page}\n")

print("✅ Rapport généré :", rapport)
```

**Explication des étapes du script Python :**

| Étape | Commande clé | Rôle |
|-------|-------------|------|
| Lecture du log | `f.readlines()` | Charge toutes les lignes |
| Extraction codes | `re.findall(r'" (\d{3}) ', data)` | Capture tous les codes HTTP |
| Filtrage erreurs | `c.startswith(('4', '5'))` | Filtre les erreurs 4xx/5xx |
| Top IPs | `Counter(ips).most_common(5)` | Compte et classe les 5 premières IP |
| Top pages | `Counter(pages).most_common(5)` | Idem pour les pages |
| Écriture rapport | `f.write(...)` | Génère le fichier texte daté |

**Exécution du script :**

```bash
python3 REGEX/analyse_nginx.py
```

---

### Partie 3 — Automatisation avec Cron

Pour que les analyses s'exécutent **automatiquement chaque nuit à 2h**, j'ai ajouté la tâche dans le crontab :

```bash
crontab -e
```

Ligne ajoutée :

```
0 2 * * * /usr/bin/pwsh /home/user/REGEX/analyse_nginx.ps1
```

> ⚠️ J'utilise le **chemin absolu** vers `pwsh` pour éviter les problèmes de PATH dans cron.

---

### Partie 4 — Vérification

Pour confirmer que cron a bien exécuté le script, j'ai consulté les logs système :

```bash
grep CRON /var/log/syslog
```

Je vérifie aussi que les rapports ont bien été créés et datés correctement :

```bash
ls -lh REGEX/
cat REGEX/rapport_nginx_ps1_$(date +%F).txt
```

---

### Partie 5 — Dépannage

| Problème rencontré | Cause possible | Solution appliquée |
|--------------------|---------------|-------------------|
| `Permission denied` sur le log | Fichier lisible uniquement par root | Exécuter avec `sudo` |
| Script PowerShell ne lit pas le fichier | Chemin incorrect | Vérifier le chemin absolu du log |
| Regex incorrecte | Mauvais format testé | Tester sur un petit extrait du log |
| Cron ne déclenche pas le script | Chemin relatif dans la commande cron | Utiliser uniquement des chemins absolus |

---

## 📊 Comparatif Bash / PowerShell / Python

| Action | Bash | PowerShell | Python |
|--------|------|------------|--------|
| Chercher un mot | `grep "mot" fichier` | `Select-String -Pattern "mot"` | `re.search(r"mot", texte)` |
| Vérifier un chiffre | `grep "[0-9]" fichier` | `"abc" -match "\d"` | `re.findall(r"\d", texte)` |
| Extraire du texte | `sed -E 's/.*: (.*)/\1/'` | `$matches[1]` | `match.group(1)` |
| Supprimer lignes vides | `grep -v "^\s*$"` | `Where-Object{$_ -notmatch "^\s*$"}` | `[l for l in f if l.strip()]` |
| Export JSON | `jq` (externe) | `ConvertTo-Json` | `json.dumps()` |
| Type de données | Texte brut | Objets .NET | Strings + objets Python |

---

## 📖 Cheat Sheet Regex

### Symboles essentiels

| Regex | Signification | Exemple | Résultat |
|-------|--------------|---------|----------|
| `.` | N'importe quel caractère | `a.c` | `abc`, `a1c` |
| `\d` | Chiffre (0–9) | `\d\d` | `12`, `45` |
| `\w` | Lettre ou chiffre | `\w+` | `abc123` |
| `\s` | Espace | `\s+` | `" "` |
| `^` | Début de ligne | `^Hello` | `Hello world` |
| `$` | Fin de ligne | `end$` | `the end` |
| `{n,m}` | Entre n et m fois | `\d{2,4}` | `12`, `1234` |
| `[^]` | Négation | `[^0-9]` | toute lettre |
| `()` | Groupe de capture | `(ab)+` | `abab` |

### Astuces rapides

- **Tester les regex** → [regex101.com](https://regex101.com) (très recommandé)
- **Python** → toujours utiliser `r"..."` (raw string)
- **Bash** → penser à `-E` pour les regex étendues (`grep -E`)
- **PowerShell** → `$matches` contient les groupes capturés

---
<img width="1920" height="1080" alt="Screenshot (385)" src="https://github.com/user-attachments/assets/98b31e25-517f-47f1-8b2b-151bd2860c6c" />
<img width="1920" height="1080" alt="Screenshot (384)" src="https://github.com/user-attachments/assets/2ba31277-250f-4e34-af00-8005deef15bb" />

## 💬 Conclusion

Grâce à ce laboratoire, j'ai appris à :

- Comprendre et utiliser les **expressions régulières** dans trois environnements différents
- Analyser un fichier de logs **réel** (Nginx) avec des regex adaptées
- Écrire un **script PowerShell** et un **script Python** produisant le même rapport
- **Automatiser** l'analyse avec cron pour une exécution nocturne
- **Diagnostiquer** les problèmes courants (permissions, chemins, regex incorrectes)

> 🔑 *Les regex sont un outil fondamental de l'administration système — maîtrisées une fois, elles servent partout : logs, validation, extraction, nettoyage.*

---

*Ouail Gacem — 300148094*



