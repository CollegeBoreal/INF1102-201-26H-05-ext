import sys
from collections import Counter
import matplotlib.pyplot as plt
import os

file = sys.argv[1]

ips = []
urls = []

with open(file, 'r') as f:
    for line in f:
        parts = line.split()
        ips.append(parts[0])
        urls.append(parts[5])

top_ips = Counter(ips).most_common(3)
top_urls = Counter(urls).most_common(3)

# 📄 Générer rapport texte
os.makedirs("output", exist_ok=True)
with open("output/rapport.txt", "w") as out:
    out.write("Top IPs:\n")
    for ip, count in top_ips:
        out.write(f"{ip} : {count}\n")

    out.write("\nTop URLs:\n")
    for url, count in top_urls:
        out.write(f"{url} : {count}\n")

# 📊 Générer graphique
os.makedirs("Figures", exist_ok=True)

labels = [ip for ip, _ in top_ips]
values = [count for _, count in top_ips]

plt.bar(labels, values)
plt.title("Top IPs")
plt.xlabel("IP")
plt.ylabel("Nombre de requêtes")
plt.savefig("Figures/top_ips.png")

print("✅ Rapport et graphique générés")
