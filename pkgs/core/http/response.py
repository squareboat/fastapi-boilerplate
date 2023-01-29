from typing import Dict
from fastapi import Response
import orjson

class HTTPResponse(Response):
    media_type = 'application/json'
    
    def render(self, content: Dict) -> bytes:
        response = {}
        if 'meta' in content:
            response['meta'] = content.pop('meta')
        
        response['data'] = content
        response['code'] = self.status_code
        response['success'] = True if (self.status_code >= 200 or self.status_code < 300) else False
        return orjson.dumps(content)