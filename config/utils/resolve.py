import re
from .. import config

def resolve(key: str):
    pattern = r'(\w+.\w+)*(\.\w+)+'
    if not re.match(pattern, key):
        raise ValueError("Invalid key")
    
    keys = key.split('.')
    value = config.get(keys.pop(0))
    for key in keys:
        value = value.get(key)
        if not value:
            return None
        
    return value