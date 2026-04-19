import nbformat as nbf

path = "RAPPORT.ipynb"

nb = nbf.read(path, as_version=4)

# 1) Cellule Markdown : titre de section
nb.cells.append(
    nbf.v4.new_markdown_cell("## Visualisations des résultats")
)

# 2) Cellule code : import commun
nb.cells.append(
    nbf.v4.new_code_cell(
        "from PIL import Image\n"
        "import matplotlib.pyplot as plt\n"
    )
)

# 3) Histogramme top_words.png
nb.cells.append(
    nbf.v4.new_code_cell(
        "img = Image.open('output/top_words.png')\n"
        "plt.imshow(img)\n"
        "plt.axis('off')"
    )
)

# 4) Wordcloud wordcloud.png
nb.cells.append(
    nbf.v4.new_code_cell(
        "img = Image.open('output/wordcloud.png')\n"
        "plt.imshow(img)\n"
        "plt.axis('off')"
    )
)

# 5) Histogramme horizontal
nb.cells.append(
    nbf.v4.new_code_cell(
        "img = Image.open('output/top_words_horizontal.png')\n"
        "plt.imshow(img)\n"
        "plt.axis('off')"
    )
)

# 6) Top auteurs
nb.cells.append(
    nbf.v4.new_code_cell(
        "img = Image.open('output/authors_top.png')\n"
        "plt.imshow(img)\n"
        "plt.axis('off')"
    )
)

nbf.write(nb, path)
print("RAPPORT.ipynb mis à jour avec les figures.")
