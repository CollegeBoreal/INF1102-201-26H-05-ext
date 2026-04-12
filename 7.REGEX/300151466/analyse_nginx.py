import re
from collections import Counter

log_file = "/var/log/nginx/access.log"

ips = []

with open(log_file, "r") as f:
    for line in f:
        match = re.match(r"(\d+\.\d+\.\d+\.\d+)", line)
        if match:
            ips.append(match.group(1))

counter = Counter(ips)

output_file = "REGEX/rapport_nginx_py_2026-03-31.txt"

with open(output_file, "w") as f:
    for ip, count in counter.most_common(10):
        f.write(f"{ip} - {count}\n")

print(f"Rapport généré : {output_file}")
