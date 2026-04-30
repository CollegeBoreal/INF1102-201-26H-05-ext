from collections import Counter

ips = []
urls = []

with open("data/sample.log", "r") as f:
    for line in f:
        parts = line.split()
        if len(parts) >= 3:
            ips.append(parts[0])
            urls.append(parts[2])

top_ips = Counter(ips).most_common(3)
top_urls = Counter(urls).most_common(3)

with open("rapport.txt", "w") as out:
    out.write("===== RAPPORT ANALYSE LOG =====\n\n")

    out.write("Top IP:\n")
    for ip, count in top_ips:
        out.write(f"{ip}: {count}\n")

    out.write("\nTop URLs:\n")
    for url, count in top_urls:
        out.write(f"{url}: {count}\n")

print("Analyse terminée")