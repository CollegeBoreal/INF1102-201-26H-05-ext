# Projet 5 : Monitoring de sites web 🌐

**Cours** : INF1102-201-26H-05  
**Étudiant** : Tarik Tidjet  
**Matricule** : 300150275  
**Date** : 2026-03-31  

---

## 📋 Description

Ce projet surveille la disponibilité de plusieurs sites web, mesure leur temps de réponse et génère un rapport automatique via un script Bash et Python.

---

## 📁 Structure du projet
```
300150275/
├── scripts/
│   ├── analyse.sh       # Script Bash principal
│   └── analyse.py       # Script Python d'analyse
├── data/
│   └── sample.log       # Logs générés automatiquement
├── output/
│   └── rapport.txt      # Rapport généré automatiquement
├── RAPPORT.ipynb        # Rapport Jupyter avec visualisations
└── README.md            # Instructions et explications
```

---

## 🖥️ 1. Connexion SSH
```bash
ssh -i ~/.ssh/ma_cle \
  -o StrictHostKeyChecking=no \
  -o UserKnownHostsFile=/tmp/ssh_known_hosts_empty \
  ubuntu@10.7.237.231
```

![Connexion SSH](images/01_connexion_ssh.png)

---

## ▶️ 2. Exécution des scripts
```bash
bash scripts/analyse.sh
```

![Exécution](images/02_execution_scripts.png)

---

## 📊 3. Rapport généré
```bash
cat output/rapport.txt
```

![Rapport](images/03_rapport.png)

---

## 🚀 4. Push sur GitHub
```bash
git add 8.Projet/300150275/
git commit -m "Ajout Projet Monitoring - 300150275"
git push
```

![Git Push](images/04_git_push.png)

---

## 🧠 Sites surveillés

| Site | Code HTTP | Temps | Statut |
|------|-----------|-------|--------|
| google.com | 200 | 419ms | ✅ EN LIGNE |
| github.com | 301 | 370ms | ❌ HORS LIGNE |
| wikipedia.org | 200 | 566ms | ✅ EN LIGNE |
| youtube.com | 200 | 430ms | ✅ EN LIGNE |
| amazon.com | 503 | 294ms | ❌ HORS LIGNE |

---

## ✅ Résultats
## 📈 Graphique d'évolution

![Évolution des temps de réponse](output/graphique_evolution.png)
- **3 sites** en ligne sur 5
- **Temps moyen** : 415ms
- **Site le plus rapide** : amazon.com (294ms)
- **Site le plus lent** : wikipedia.org (566ms)
