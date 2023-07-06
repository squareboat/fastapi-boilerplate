from json import loads
from fastapi import Request as BaseRequest

class Request(BaseRequest):
    async def all(self):
        body = await self.body()
        if body != b'':
            body = loads(body)
        else:
            body = {}
        return {
            **self.query_params._dict,
            **self.path_params,
            **body
        }
        