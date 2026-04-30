from collections import Counter

ips = []
urls = []

with open("../data/sample.log", "r") as fichier:
    for ligne in fichier:
        elements = ligne.split()
        if len(elements) >= 3:
            ips.append(elements[0])
            urls.append(elements[2])

top_ips = Counter(ips).most_common(3)
top_urls = Counter(urls).most_common(3)

with open("../output/rapport.txt", "w") as rapport:
    rapport.write("===== RAPPORT ANALYSE LOG =====\n\n")

    rapport.write("Top IP:\n")
    for ip, n in top_ips:
        rapport.write(f"{ip}: {n}\n")

    rapport.write("\nTop URLs:\n")
    for url, n in top_urls:
        rapport.write(f"{url}: {n}\n")

print("Analyse terminee")