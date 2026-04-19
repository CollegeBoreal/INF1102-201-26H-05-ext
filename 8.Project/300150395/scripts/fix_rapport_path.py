import nbformat as nbf

path = "RAPPORT.ipynb"
nb = nbf.read(path, as_version=4)

replacements = {
    # JSONL
    'with open("articles.jsonl", "r", encoding="utf-8") as f:':
    'with open("data/articles.jsonl", "r", encoding="utf-8") as f:',
    # rapport.txt
    'with open("rapport.txt", "r", encoding="utf-8") as f:':
    'with open("output/rapport.txt", "r", encoding="utf-8") as f:',
    # IPython.display.Image chemins relatifs
    'Image(filename="top_words.png")':
    'Image(filename="output/top_words.png")',
    'Image(filename="wordcloud.png")':
    'Image(filename="output/wordcloud.png")',
    'Image(filename="top_words_horizontal.png")':
    'Image(filename="output/top_words_horizontal.png")',
    'Image(filename="authors_top.png")':
    'Image(filename="output/authors_top.png")',
}

changed = False
for cell in nb.cells:
    src = cell.get("source", "")
    for old, new in replacements.items():
        if old in src:
            src = src.replace(old, new)
            changed = True
    cell["source"] = src

if changed:
    nbf.write(nb, path)
    print("Chemins corrigés dans RAPPORT.ipynb.")
else:
    print("Aucune cellule à corriger.")
