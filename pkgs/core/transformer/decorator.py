from functools import wraps

def transform(transformer_cls):
    def decorator(func):        
        @wraps(func)
        async def wrapper(*args, **kwargs):
            result = await func(*args, **kwargs)

            transformer = transformer_cls()
            
            if type(result) == dict:
                result = transformer.work(result)
            elif type(result) == list:
                result = result = transformer.collection(result)

            return result
        return wrapper
    return decorator