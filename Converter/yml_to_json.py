import yaml
import json
import sys

if len(sys.argv) < 3:
    sys.exit(1)

with open(sys.argv[1], 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

with open(sys.argv[2], 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
