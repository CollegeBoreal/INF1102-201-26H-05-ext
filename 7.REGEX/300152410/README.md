# 7️⃣ REGEX – Analyse logs Nginx

**Étudiant :** Imad Boudeuf  
**Numéro :** 300152410  
**Cours :** INF1102-201-26H-05  

## 🎯 Objectif
Analyser les logs Nginx avec des expressions régulières en PowerShell et Python.

## 📁 Fichiers
| Fichier | Description |
|---|---|
| `analyse_nginx.ps1` | Script PowerShell d'analyse |
| `analyse_nginx.py` | Script Python d'analyse |
| `rapport_nginx_ps1_2026-04-10.txt` | Rapport PowerShell |
| `rapport_nginx_py_2026-04-10.txt` | Rapport Python |

## 📊 Résultats
- Total requêtes : 2
- Erreurs 404 : 1
- Top IP : 127.0.0.1
- Top pages : /, /favicon.ico

## 🧠 Regex utilisées
| Élément | Regex |
|---|---|
| IP | `(\d{1,3}\.){3}\d{1,3}` |
| Code HTTP | `" (\d{3}) "` |
| Pages GET | `"GET ([^ ]+)` |
| Erreurs | `^[45]` |