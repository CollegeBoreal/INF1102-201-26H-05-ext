##300151403
:fortune_cookie: Utiliser **PowerShell sous Linux** apporte plusieurs avantages, surtout dans un contexte **administration système, DevOps ou automatisation multi-plateforme**. Voici les principaux points :

---

## 1️⃣ Automatisation multi-plateforme

* PowerShell fonctionne **sur Windows, Linux et macOS**.
* Les mêmes scripts peuvent fonctionner **sur plusieurs OS**, avec peu ou pas de modification.
* Très utile si tu gères **des serveurs mixtes** dans une entreprise (Windows + Ubuntu + RedHat, etc.).

---

## 2️⃣ Pipeline orienté objets

* Contrairement au Bash, qui travaille principalement avec du texte, PowerShell **travaille avec des objets**.
* Exemple :

```powershell
Get-Process | Where-Object {$_.CPU -gt 10} | Select-Object ProcessName, CPU
```

* Chaque commande renvoie un **objet structuré**, pas seulement des lignes de texte, ce qui facilite :

  * le filtrage (`Where-Object`)
  * la sélection (`Select-Object`)
  * l’exportation (`Export-Csv`, `ConvertTo-Json`)

---

## 3️⃣ Intégration avec les API et services

* PowerShell peut appeler **API REST**, manipuler JSON et XML facilement.
* Exemple : tu peux automatiser des tâches DevOps avec **Moodle API, Azure, AWS, Rubrik**, etc., directement depuis Linux.
* Bash demanderait beaucoup plus de parsing et de scripts supplémentaires.

---

## 4️⃣ Gestion de systèmes complexe

* PowerShell peut **accéder à des informations système avancées** : processus, services, utilisateurs, SSH, disque, réseau, etc.
* Les commandes sont souvent **plus lisibles et standardisées** qu’avec Bash, surtout pour des tâches complexes.

---

## 5️⃣ Scripts plus robustes et maintenables

* **Variables typées, fonctions, modules** : permet de structurer les scripts comme de vrais programmes.
* Plus facile de créer des **batchs DevOps complexes**, comme celui que tu as commencé à faire (`devops_batch.ps1`).

---

## 6️⃣ Interopérabilité avec Windows

* Si tu as des **scripts Windows** existants, tu peux souvent les **adapter pour Linux** sans réécrire tout en Bash.
* Très utile dans un **environnement hybride Windows/Linux**.

---

### Exemple concret :

* **Bash** : extraire les 5 processus les plus gourmands en mémoire, puis générer un JSON :

```bash
ps aux --sort=-%mem | head -n 6 | awk '{print $11, $4}' > top.txt
```

* **PowerShell** :

```powershell
Get-Process | Sort-Object WS -Descending | Select-Object -First 5 Name,WS | ConvertTo-Json
```

→ Le résultat est directement un **JSON utilisable**, prêt pour des scripts DevOps.

---

💡 **Résumé en une phrase** :

> PowerShell sous Linux combine **la puissance et la lisibilité de PowerShell Windows** avec **la flexibilité de Linux**, ce qui rend l’automatisation et le DevOps plus rapides, robustes et multi-plateforme.

---

# Comparatif Bash vs PowerShell sous Linux

| Fonctionnalité            | Bash                            | PowerShell                                                                            | Commentaire / Avantage PowerShell                                                      |
| ------------------------- | ------------------------------- | ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| **Type de données**       | Texte (strings)                 | Objets (.NET/PSObjects)                                                               | Les objets permettent de filtrer, trier et exporter facilement sans parsing compliqué. |                                                                                            |                            |                         |                                                                      |
| **Filtrage**              | `grep` ou `awk`                 | `Where-Object {$_.CPU -gt 10}`                                                        | Plus lisible et robuste, sans découpage manuel des colonnes.                           |                                                                                            |                            |                         |                                                                      |
| **Export CSV / JSON**     | `awk ... > fichier.csv` ou `jq` | `ConvertTo-Csv` ou `ConvertTo-Json`                                                   | Prêt pour ingestion dans d’autres scripts ou API DevOps.                               |                                                                                            |                            |                         |                                                                      |
| **Boucles**               | `for i in *; do ...; done`      | `foreach ($f in Get-ChildItem) { ... }`                                               | Syntaxe plus orientée objets, accès direct aux propriétés (`$f.Name`, `$f.Length`).    |                                                                                            |                            |                         |                                                                      |
| **Variables typées**      | Pas typées, string par défaut   | Typées (`[int]$count = 5`)                                                            | Moins d’erreurs et meilleure maintenance pour scripts complexes.                       |                                                                                            |                            |                         |                                                                      |
| **Accès SSH**             | `ssh user@host "command"`       | `ssh user@host "command"` (directement dans PowerShell, intégré dans un script batch) | Peut être intégré avec variables PowerShell et gestion automatique des erreurs.        |                                                                                            |                            |                         |                                                                      |
| **Gestion fichiers**      | `cp, mv, rm, tar`               | `Copy-Item, Move-Item, Remove-Item, Compress-Archive`                                 | Commandes plus cohérentes et cross-platform.                                           |                                                                                            |                            |                         |                                                                      |
| **Automatisation DevOps** | Scripts multiples + parsing     | Scripts uniques orientés objets + modules                                             | PowerShell facilite intégration API, JSON, Azure, AWS, etc.                            |                                                                                            |                            |                         |                                                                      |
| **Multi-plateforme**      | Limité, Bash Linux/macOS        | Linux + Windows + macOS                                                               | Les mêmes scripts fonctionnent sur plusieurs OS sans réécriture majeure.               |                                                                                            |                            |                         |                                                                      |

---

### Exemple concret : générer un rapport DevOps

**Bash** :

```bash
ps aux --sort=-%mem | head -n 5 > top_mem.txt
df -h >> top_mem.txt
```

**PowerShell** :
