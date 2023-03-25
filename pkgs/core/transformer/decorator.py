from functools import wraps
from .parser import parse_includes
from .transformer import Transformer

def transform(transformer_cls: Transformer):
    def decorator(func):        
        @wraps(func)
        async def wrapper(*args, **kwargs):
            request = kwargs.get('request')
            all = await request.all()
            result = await func(*args, **kwargs)

            transformer = transformer_cls()
            transformer.set_includes(parse_includes(all.get('include')))
            
            if type(result) == dict:
                result = transformer.work(result)
            elif type(result) == list:
                output = []
                for datum in result:
                    output.append(transformer.work(datum))
                result = output

            return result
        return wrapper
    return decorator