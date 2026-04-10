import json
import nbformat as nbf

nb = nbf.v4.new_notebook()
cells = []

# Cellule 1 : Titre + nom
cells.append(nbf.v4.new_markdown_cell(
"""# INF1102 — Projet Scrapy News

Ismail Trache — 300150395"""
))

# Cellule 2 : Objectif
cells.append(nbf.v4.new_markdown_cell(
"""## Objectif du projet

Ce projet utilise le framework Scrapy pour récupérer automatiquement des citations sur le site de démonstration `https://quotes.toscrape.com`.
Les données sont ensuite analysées avec un script Python pour calculer le nombre d’éléments récupérés et le top 10 des mots les plus fréquents.
Le notebook présente les fichiers générés (`articles.jsonl`, `rapport.txt`, `top_words.png`) et commente les résultats."""
))

# Cellule 3 : code pour charger les données
cells.append(nbf.v4.new_code_cell(
"""import json

with open("articles.jsonl", "r", encoding="utf-8") as f:
    items = [json.loads(line) for line in f if line.strip()]

len(items)"""
))

# Cellule 4 : code pour afficher rapport.txt
cells.append(nbf.v4.new_code_cell(
"""with open("rapport.txt", "r", encoding="utf-8") as f:
    print(f.read())"""
))

# Cellule 5 : code pour afficher la figure
cells.append(nbf.v4.new_code_cell(
"""from IPython.display import Image

Image(filename="top_words.png")"""
))

# Cellule 6 : Analyse des résultats
cells.append(nbf.v4.new_markdown_cell(
"""## Analyse des résultats

Le spider Scrapy a récupéré 100 éléments au total (citations + auteur) dans le fichier `articles.jsonl`.
Le top 10 des mots les plus fréquents montre que des mots comme **you**, **not**, **that**, **love** apparaissent très souvent.
Cela s’explique par le style des citations en anglais, avec beaucoup de phrases adressées à une personne (`you`) et des thèmes fréquents comme l’amour (`love`) ou la négation (`not`)."""
))

# Cellule 7 : Conclusion
cells.append(nbf.v4.new_markdown_cell(
"""## Conclusion

Ce projet a permis de mettre en place une chaîne complète Bash / PowerShell + Python + Scrapy :
le spider récupère les données, le script Python génère un rapport texte (`rapport.txt`) et une figure (`top_words.png`), et ce notebook présente et commente les résultats.
Ce travail montre comment automatiser un scraping simple avec Scrapy, puis analyser les données textuelles avec Python et les visualiser dans un rapport Jupyter."""
))

nb["cells"] = cells

with open("RAPPORT.ipynb", "w", encoding="utf-8") as f:
    nbf.write(nb, f)
