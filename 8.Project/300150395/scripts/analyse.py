import sys
import json
from collections import Counter
import matplotlib.pyplot as plt
import re
from pathlib import Path


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

    stopwords = {"the", "and", "for", "les", "des", "une", "avec", "vous"}
    tokens = [t for t in tokens if t not in stopwords and len(t) > 2]

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


if __name__ == "__main__":
    main()
