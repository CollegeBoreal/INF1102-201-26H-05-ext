# 📊 Projet 8 – Analyse de logs avec Bash & Python

**Étudiante : KAHINA ZERKANI 300151556**

---

## 🎯 Objectif

Ce projet consiste à analyser un fichier de logs (`sample.log`) en utilisant **Python** et **Bash/PowerShell**, afin de générer automatiquement :

* 📄 un **rapport texte**
* 📊 un **graphique (visualisation)**
* 📘 un **notebook explicatif (Jupyter)**

---

## ⚙️ Technologies utilisées

* Python 3
* Bash (Linux)
* PowerShell
* Matplotlib (visualisation)
* Jupyter Notebook
* Git / GitHub

---

## 📁 Structure du projet

```text
300151556/
├── README.md
├── RAPPORT.ipynb
├── data/
│   └── sample.log
├── output/
│   └── rapport.txt
├── scripts/
│   ├── analyse.sh
│   ├── analyse.py
│   └── requirements.txt
├── Figures/
│   └── top_ips.png
├── images/
│   ├── execution.png
│   └── rapport.png
```

---

## 🧾 Description des fichiers

### 🔹 `scripts/analyse.py`

Script Python qui :

* lit le fichier log
* extrait les adresses IP et URLs
* calcule les fréquences
* génère `rapport.txt`
* génère un graphique (`Figures/top_ips.png`)

---

### 🔹 `scripts/analyse.sh`

Script Bash qui lance automatiquement l’analyse :

```bash
bash scripts/analyse.sh
```

---

### 🔹 `data/sample.log`

Fichier de logs utilisé pour les tests.

---

### 🔹 `output/rapport.txt`

Rapport généré automatiquement contenant :

* Top IPs
* Top URLs

---

### 🔹 `Figures/top_ips.png`

Graphique représentant les adresses IP les plus fréquentes.

---

### 🔹 `RAPPORT.ipynb`

Notebook Jupyter contenant :

* explication de la méthode
* analyse des résultats
* visualisation des données

---

## ▶️ Exécution

### 🔹 Méthode 1 (Bash)

```bash
bash scripts/analyse.sh
```


---

### 🔹 Méthode 2 (Python direct)

```bash
python3 scripts/analyse.py data/sample.log
```
<img width="745" height="47" alt="image" src="https://github.com/user-attachments/assets/a0a92deb-d1b6-4473-b89c-9f9ce4b9a975" />

---

## 📄 Exemple de sortie

```text
Top IPs:
192.168.1.1 : 3
192.168.1.2 : 1
192.168.1.3 : 1

Top URLs:
/index.html : 3
/about.html : 1
/contact.html : 1
```

---

## 🖼️ Résultats

### 🔹 Exécution du script

<img width="607" height="58" alt="image" src="https://github.com/user-attachments/assets/6d02d856-29fc-4baf-afcd-e4065570d8b4" />



---

### 🔹 Rapport généré
<img width="542" height="44" alt="image" src="https://github.com/user-attachments/assets/69e51d38-fee6-460c-8658-382153d0b3ab" />


<img width="160" height="161" alt="image" src="https://github.com/user-attachments/assets/a94df6d0-4215-41aa-88f1-973ccf3b4f2b" />



---

## 📊 Graphique

<img width="527" height="29" alt="image" src="https://github.com/user-attachments/assets/4efd1d05-8d37-478f-870f-c58abdee6d68" />

<img width="659" height="322" alt="image" src="https://github.com/user-attachments/assets/46b9c334-c4b4-4ff4-b138-78e7ac560716" />



---

## 🧠 Concepts appris

* Automatisation avec Bash
* Traitement de données avec Python
* Analyse de logs
* Utilisation de structures de données (`Counter`)
* Génération de rapports et graphiques

---

## ✅ Conclusion

Ce projet démontre comment combiner plusieurs outils pour automatiser l’analyse de données.

✔ Automatisation
✔ Analyse rapide
✔ Résultats exploitables

---

## 👩‍💻 Auteur

**Kahina Zerkani**
Techniques des systèmes informatiques
Collège Boréal
