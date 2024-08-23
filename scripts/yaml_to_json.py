import yaml
import json


with open('../openapi/openapi.yaml', 'r', encoding='utf-8') as f:
    yaml_data = yaml.safe_load(f)

with open('../openapi_json/openapi.json', 'w', encoding='utf-8') as f:
    json.dump(yaml_data, f, ensure_ascii=False, indent=4)
