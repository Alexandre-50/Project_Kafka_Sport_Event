import json
from typing import Any, Dict

def dumps_json(obj: Dict[str, Any]) -> bytes:
    return json.dumps(obj, ensure_ascii=False).encode("utf-8")

def loads_json(raw: bytes) -> Dict[str, Any]:
    return json.loads(raw.decode("utf-8"))
