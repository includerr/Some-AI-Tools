import yaml
import csv
import sys

if len(sys.argv) < 3:
    sys.exit(1)

with open(sys.argv[1], 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

if not isinstance(data, list):
    if isinstance(data, dict):
        data = [data]
    else:
        sys.exit(1)

headers = list(data[0].keys()) if data else []

with open(sys.argv[2], 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    writer.writerows(data)
