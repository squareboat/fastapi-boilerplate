from typing import Dict
from fastapi import status
from fastapi.responses import ORJSONResponse
import orjson

class HTTPResponse(ORJSONResponse):
    media_type = 'application/json'
    
    def render(self, content: Dict) -> bytes:
        if self.status_code == status.HTTP_204_NO_CONTENT:
            return

        response = {}
        if 'meta' in content:
            response['meta'] = content.pop('meta')
        
        response['data'] = content
        response['code'] = self.status_code
        response['success'] = True if (self.status_code >= 200 or self.status_code < 300) else False
        return orjson.dumps(response)