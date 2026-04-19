import sys
import json
from collections import Counter
import matplotlib.pyplot as plt
import re
from pathlib import Path
from wordcloud import WordCloud


BASE_DIR = Path(__file__).resolve().parent.parent


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
    # 1) Choisir le fichier d'entrée
    if len(sys.argv) >= 2:
        # On prend l'argument tel quel et on le résout par rapport au cwd
        input_file = Path(sys.argv[1]).resolve()
    else:
        # Par défaut, on utilise ton fichier Scrapy
        input_file = BASE_DIR / "data" / "articles.jsonl"

    # 2) Si le fichier n'existe pas, fallback sur articles.jsonl sans crasher
    if not input_file.exists():
        fallback = BASE_DIR / "data" / "articles.jsonl"
        if fallback.exists():
            print(f"Fichier {input_file} introuvable, utilisation de {fallback}")
            input_file = fallback
        else:
            print(f"Aucun fichier d'entrée valide trouvé (ni {input_file} ni {fallback})")
            return 0  # surtout pas d'exception

    output_dir = BASE_DIR / "output"
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

    plt.figure(figsize=(10, 5))
    plt.barh(mots, freqs)
    plt.title("Top 10 mots fréquents (horizontal)")
    plt.tight_layout()
    plt.savefig(output_dir / "top_words_horizontal.png")

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

    texte_wc = " ".join(tokens)
    wc = WordCloud(width=800, height=400, background_color="white").generate(texte_wc)

    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(output_dir / "wordcloud.png")

if __name__ == "__main__":
    main()
