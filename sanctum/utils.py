try:
    import orjson as json
except ImportError:
    import json

def _to_json(data: dict):
    return json.dumps(data)