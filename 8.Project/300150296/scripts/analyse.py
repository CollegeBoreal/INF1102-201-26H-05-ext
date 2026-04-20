import sys
import re
from collections import Counter

if len(sys.argv) < 2:
    print("Usage: python3 analyse.py <logfile>")
    sys.exit(1)

logfile = sys.argv[1]

with open(logfile) as f:
    lines = f.readlines()

data = "".join(lines)

# IP
ips = re.findall(r'(\d{1,3}(?:\.\d{1,3}){3})', data)

# URLs
urls = re.findall(r'"GET ([^ ]+)', data)

# Codes HTTP
codes = re.findall(r'" (\d{3}) ', data)

print(f"\n📊 Statistiques:\n")
print(f"Total requêtes: {len(lines)}")
print(f"Total IP uniques: {len(set(ips))}")

print(f"\n🔝 Top 5 IP:")
for ip, count in Counter(ips).most_common(5):
    print(f"  {count} - {ip}")

print(f"\n🔝 Top 5 URLs:")
for url, count in Counter(urls).most_common(5):
    print(f"  {count} - {url}")

print(f"\n📈 Codes HTTP:")
for code, count in Counter(codes).most_common():
    print(f"  {code}: {count}")