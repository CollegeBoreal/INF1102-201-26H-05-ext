import re

with open("notes.txt", "r", encoding="utf-8") as f:
    text = f.read()

patterns = {
    "Emails": r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
    "Téléphones": r"[0-9]{3}-[0-9]{3}-[0-9]{4}",
    "Dates": r"[0-9]{4}-[0-9]{2}-[0-9]{2}",
    "IP": r"([0-9]{1,3}\.){3}[0-9]{1,3}",
    "Codes HTTP": r"Erreur [0-9]{3}",
}

for titre, pattern in patterns.items():
    print(f"=== {titre} ===")
    print(re.findall(pattern, text))
    print()
