import re

logs = [
    "192.168.1.10 GET /index.html 200",
    "10.0.0.5 GET /login 404",
    "172.16.0.8 GET /admin 500"
]

print("=== Analyse Python Regex ===")

for ligne in logs:

    ip = re.findall(r'(\d{1,3}(?:\.\d{1,3}){3})', ligne)
    page = re.findall(r'GET ([^ ]+)', ligne)
    code = re.findall(r'(200|404|500)', ligne)

    print("IP :", ip)
    print("Page :", page)
    print("Code :", code)
    print()