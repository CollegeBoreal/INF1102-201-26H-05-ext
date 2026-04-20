import re

with open("notes.txt", "r") as f:
    data = f.read()

ips = re.findall(r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}", data)

print("IPs trouvées :", ips)

