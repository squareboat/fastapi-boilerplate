from functools import wraps
from pkgs.core.validators import BaseValidator

def validate(validator: BaseValidator):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            inputs = await kwargs.get('request').all()
            kwargs.pop('inputs', {})
            result = await func(*args, inputs=validator(**inputs), **kwargs)
            return result
        return wrapper
    return decorator