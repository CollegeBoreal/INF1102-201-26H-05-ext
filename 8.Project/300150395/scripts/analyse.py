import sys
import json
from collections import Counter
import matplotlib.pyplot as plt
import re
from pathlib import Path
from wordcloud import WordCloud

def charger_items(path: Path):
    items = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            items.append(json.loads(line))
    return items


def nettoyer_texte(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-zàâçéèêëîïôûùüÿñæœ0-9 ]", " ", text)
    return text


def main():
    if len(sys.argv) < 2:
        print("Usage: analyse.py data/articles.jsonl")
        sys.exit(1)

    project_root = Path(__file__).resolve().parent.parent
    input_file = project_root / sys.argv[1]
    output_dir = project_root / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    items = charger_items(input_file)

    textes = [
        (i.get("title") or "") + " " + (i.get("summary") or "")
        for i in items
    ]

    tokens = []
    for t in textes:
        t = nettoyer_texte(t)
        tokens.extend(t.split())

    # stopwords anglais + quelques mots français, pour enlever les mots trop fréquents
    stopwords = {
        "the", "and", "for", "you", "your", "yours", "not", "that", "this", "with",
        "but", "are", "was", "were", "have", "has", "had", "can", "could", "will",
        "would", "should", "about", "into", "from", "they", "them", "their", "there",
        "what", "when", "where", "which", "who", "whom", "why", "how", "all", "any",
        "more", "most", "some", "such", "only", "other", "than", "then",
        "its", "it's", "its", "our", "ours", "we", "us",
        "les", "des", "une", "avec", "vous"
    }

    tokens = [t for t in tokens if t not in stopwords and len(t) > 3]
    compteur = Counter(tokens)
    top10 = compteur.most_common(10)

    with (output_dir / "rapport.txt").open("w", encoding="utf-8") as f:
        f.write("===== RAPPORT SCRAPY NEWS =====\n")
        f.write(f"Nombre d’éléments scrapés : {len(items)}\n\n")
        f.write("Top 10 des mots les plus fréquents :\n")
        for mot, freq in top10:
            f.write(f"- {mot} : {freq}\n")

    mots = [m for m, _ in top10]
    freqs = [f for _, f in top10]
    plt.figure(figsize=(10, 5))
    plt.bar(mots, freqs)
    plt.title("Top 10 mots fréquents")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_dir / "top_words.png")

    # 2) Histogramme horizontal (top_words_horizontal.png)
    plt.figure(figsize=(10, 5))
    plt.barh(mots, freqs)
    plt.title("Top 10 mots fréquents (horizontal)")
    plt.tight_layout()
    plt.savefig(output_dir / "top_words_horizontal.png")

    # 3) Top auteurs (authors_top.png)

    auteurs = [i.get("summary") for i in items if i.get("summary")]
    compteur_auteurs = Counter(auteurs)
    top_auteurs = compteur_auteurs.most_common(5)

    noms = [a for a, _ in top_auteurs]
    freqs_auteurs = [f for _, f in top_auteurs]

    plt.figure(figsize=(8, 4))
    plt.bar(noms, freqs_auteurs)
    plt.title("Top 5 auteurs les plus fréquents")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(output_dir / "authors_top.png")

    # 2) Wordcloud (wordcloud.png)
    # Recréer un grand texte à partir des tokens filtrés
    texte_wc = " ".join(tokens)

    wc = WordCloud(
        width=800,
        height=400,
        background_color="white"
    ).generate(texte_wc)

    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(output_dir / "wordcloud.png")


if __name__ == "__main__":
    main()
