# 7️⃣ REGEX — Analyse des logs Nginx avec Expressions Régulières

**Nom :** Hani  
**Boréal ID :** 300150557  
**Cours :** INF1102  
**Environnement :** Ubuntu 22.04 LTS  
**Shells :** PowerShell (pwsh) + Python 3

## 1. Introduction

Dans ce laboratoire, l'objectif est d'utiliser des expressions régulières (Regex) pour analyser les logs du serveur web Nginx.

Les scripts développés permettent de :
- Lire le fichier `/var/log/nginx/access.log`
- Extraire les codes HTTP (200, 404, 500...)
- Identifier les Top 5 adresses IP
- Identifier les Top 5 pages visitées
- Générer un rapport texte automatique

## 2. Structure du projet7.REGEX/300150557/
│
├── analyse_nginx.ps1                    # Script PowerShell
├── analyse_nginx.py                     # Script Python
├── rapport_nginx_ps1_2026-04-17.txt     # Rapport généré PowerShell
├── rapport_nginx_py_2026-04-17.txt      # Rapport généré Python
├── README.md                            # Ce fichier
└── images/
├── 1.png    # Script analyse_nginx.ps1 dans nano
├── 2.png    # Script analyse_nginx.py dans nano
├── 3.png    # Exécution des deux scripts
└── 4.png    # Contenu du rapport généré
## 4. Regex utilisées

| Élément | Regex |
|---------|-------|
| Adresse IP | `(\d{1,3}(\.\d{1,3}){3})` |
| Code HTTP | `" (\d{3}) "` |
| Pages GET | `"GET ([^ ]+)` |
| Erreurs 4xx/5xx | `^[45]` |

## 5. Script PowerShell — analyse_nginx.ps1

![Script PowerShell](images/1.png)

## 6. Script Python — analyse_nginx.py

![Script Python](images/2.png)

## 7. Exécution des scripts

```bash
# PowerShell
pwsh ./analyse_nginx.ps1

# Python
python3 ./analyse_nginx.py
```

![Exécution des scripts](images/3.png)

## 8. Résultat obtenu

![Rapport généré](images/4.png)

## 9. Automatisation avec Cron

```bash
crontab -e
0 2 * * * /usr/bin/pwsh /home/etudiant/INF1102-201-26H-05/7.REGEX/300150557/analyse_nginx.ps1
5 2 * * * /usr/bin/python3 /home/etudiant/INF1102-201-26H-05/7.REGEX/300150557/analyse_nginx.py
```

## 10. Comparatif Bash / PowerShell / Python

| Action | Bash | PowerShell | Python |
|--------|------|-----------|--------|
| Chercher un mot | `grep "mot" fichier` | `Select-String -Pattern "mot"` | `re.search(r"mot", texte)` |
| Extraire IP | `grep -oE "\d{1,3}(\.\d{1,3}){3}"` | `-match "(\d{1,3}\.){3}\d{1,3}"` | `re.findall(r"\d{1,3}(?:\.\d{1,3}){3}", data)` |
| Codes HTTP | `grep -oP '" \K\d{3}'` | `-match '" (\d{3}) '` | `re.findall(r'" (\d{3}) ', data)` |
| Supprimer lignes vides | `grep -v "^\s*$"` | `Where-Object { $_ -notmatch "^\s*$" }` | `[l for l in f if l.strip()]` |

## 🥠 Conclusion

Les expressions régulières permettent d'extraire rapidement des informations précises depuis des fichiers de logs volumineux, que ce soit en PowerShell ou Python — les deux approches produisent le même résultat avec des syntaxes légèrement différentes.