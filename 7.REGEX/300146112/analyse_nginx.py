import re

with open("/var/log/nginx/access.log") as f:
    lines = f.readlines()

data = "".join(lines)

codes = re.findall(r'" (\d{3}) ', data)

print("Total:", len(lines))
print("Erreurs:", len([c for c in codes if c.startswith(('4','5'))]))
