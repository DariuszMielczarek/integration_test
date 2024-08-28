import yaml
import json


with open('../openapi_json/openapi.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)

with open('../openapi/openapi.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(json_data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
