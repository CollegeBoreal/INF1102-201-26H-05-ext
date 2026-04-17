# 🧪 TP : Analyse des logs Nginx avec Regex (PowerShell & Python)

---

## 👤 Identification

| Champ        | Information                     |
|--------------|---------------------------------|
| **Nom**      | Calvin Kiegaing Kouam           |
| **Matricule**| 300152131                       |
| **Cours**    | Programmation des Systèmes      |

---

## 🎯 Objectif

Créer un script qui :
- Analyse `/var/log/nginx/access.log`
- Utilise des expressions régulières
- Génère un rapport automatique
- Peut être automatisé (cron / tâche planifiée)

---

## 📂 Structure du projet

```
REGEX/
├── analyse_nginx.ps1                      # Script PowerShell complet
├── analyse_nginx.py                       # Script Python complet
├── rapport_nginx_ps1_YYYY-MM-DD.txt
└── rapport_nginx_py_YYYY-MM-DD.txt
```

---

## 🧾 Format du log Nginx

```
192.168.1.10 - - [17/Mar/2026:14:32:10 +0000] "GET /index.html HTTP/1.1" 200 1024
```

---

## 🧠 Expressions régulières utilisées

| Élément      | Regex                          |
|--------------|--------------------------------|
| IP           | `(\d{1,3}\.){3}\d{1,3}`        |
| Code HTTP    | `" (\d{3}) `                   |
| Pages GET    | `"GET ([^ ]+)`                 |
| Erreurs      | `" (4\|5)\d{2} `               |

---

## ⚡ PARTIE 1 — Script PowerShell

### 📄 analyse_nginx.ps1

```powershell
$logfile = "/var/log/nginx/access.log"
$rapport = "REGEX/rapport_nginx_ps1_$(Get-Date -Format yyyy-MM-dd).txt"

$lines = Get-Content $logfile

"📊 Rapport Nginx - $(Get-Date)" | Out-File $rapport
"----------------------------------" | Out-File $rapport -Append

# Total
$total = $lines.Count
"Total requêtes : $total" | Out-File $rapport -Append

# Codes HTTP
$codes = $lines | ForEach-Object {
    if ($_ -match '" (\d{3}) ') { $matches[1] }
}

# Erreurs
$errors = $codes | Where-Object { $_ -match '^[45]' }
"Erreurs HTTP : $($errors.Count)" | Out-File $rapport -Append

# 404
$notfound = $codes | Where-Object { $_ -eq "404" }
"Erreurs 404 : $($notfound.Count)" | Out-File $rapport -Append

# 500
$servererr = $codes | Where-Object { $_ -eq "500" }
"Erreurs 500 : $($servererr.Count)" | Out-File $rapport -Append

# IPs
$ips = $lines | ForEach-Object {
    if ($_ -match '^(\d{1,3}(\.\d{1,3}){3})') { $matches[1] }
}

"`nTop 5 IP :" | Out-File $rapport -Append
$ips | Group-Object | Sort-Object Count -Descending | Select-Object -First 5 |
ForEach-Object {
    "$($_.Count) $($_.Name)" | Out-File $rapport -Append
}

# Pages
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

### ▶️ Exécution du script PowerShell

```bash
pwsh ./REGEX/analyse_nginx.ps1
```

![Exécution script PowerShell](images/1%20execution%20script%20pwsh.png)

---

## 🐍 PARTIE 2 — Script Python

### 📄 analyse_nginx.py

```python
import re
from collections import Counter
from datetime import datetime

logfile = "/var/log/nginx/access.log"

with open(logfile) as f:
    lines = f.readlines()

data = "".join(lines)

rapport = f"REGEX/rapport_nginx_py_{datetime.now().date()}.txt"

# Total
total = len(lines)

# Codes HTTP
codes = re.findall(r'" (\d{3}) ', data)

# Erreurs
errors = [c for c in codes if c.startswith(('4', '5'))]

# IP
ips = re.findall(r'(\d{1,3}(?:\.\d{1,3}){3})', data)

# Pages
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
    for p, count in Counter(pages).most_common(5):
        f.write(f"{count} {p}\n")

print("✅ Rapport généré :", rapport)
```

### ▶️ Exécution du script Python

```bash
python3 REGEX/analyse_nginx.py
```

![Exécution script Python](images/2%20execution%20script%20python.png)

---

## 📊 Rapports générés

### Rapports créés après exécution

![Rapports générés](images/3%20rapport%20generes%20.png)

### Contenu du rapport PowerShell

![Contenu rapport PS1](images/4%20contennu%20rapport%20ps1.png)

### Contenu du rapport Python

![Contenu rapport Python](images/5%20contenu%20rapport%20python.png)

---

## ⏰ PARTIE 3 — Automatisation (Cron)

### Configuration Linux (cron)

```bash
crontab -e
0 2 * * * /usr/bin/pwsh /home/user/REGEX/analyse_nginx.ps1
```

![Automatisation cron](images/6%20automatisation%20cron.png)

---

## 🔍 PARTIE 4 — Vérification

```bash
grep CRON /var/log/syslog
```

---

## 🧯 PARTIE 5 — Dépannage

| Problème                        | Solution                        |
|---------------------------------|---------------------------------|
| Accès refusé au log             | `sudo`                          |
| Script PowerShell ne lit pas    | Vérifier le chemin              |
| Regex incorrect                 | Tester avec un petit extrait    |
| Cron ne fonctionne pas          | Utiliser le chemin absolu       |

---

## 🎓 Compétences couvertes

- ✔ Regex (PowerShell + Python)
- ✔ Analyse de logs web
- ✔ Traitement de texte
- ✔ Automatisation
- ✔ Débogage
