import re
from collections import Counter

with open("data/sample.log") as f:
    lines = f.readlines()

data = "".join(lines)

codes = re.findall(r'" (\d{3}) ', data)
ips = re.findall(r'(\d{1,3}(?:\.\d{1,3}){3})', data)
pages = re.findall(r'"GET ([^ ]+)', data)

with open("output/rapport.txt", "w") as f:
    f.write(f"Total: {len(lines)}\n")
    f.write(f"Erreurs: {len([c for c in codes if c.startswith(('4','5'))])}\n")

    f.write("\nTop IP:\n")
    for ip, count in Counter(ips).most_common(3):
        f.write(f"{count} - {ip}\n")

    f.write("\nTop pages:\n")
    for p, count in Counter(pages).most_common(3):
        f.write(f"{count} - {p}\n")

print("OK")
