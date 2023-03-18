from typing import Callable, Dict, List
from fastapi import Request, Response
from fastapi.responses import ORJSONResponse
from fastapi.routing import APIRoute
from fastapi.exceptions import HTTPException, RequestValidationError

class ExceptionHandler(APIRoute):
    def get_route_handler(self) -> Callable:
        route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Request:
            try:
                response: Response = await route_handler(request)
                return response
            except HTTPException as httpe:
                return ORJSONResponse({ "success": False, "code": httpe.status_code, "message": httpe.detail }, status_code=httpe.status_code)
            except RequestValidationError as rve:
                return ORJSONResponse(self.parse_validation_error(rve.errors()), status_code=422)

        return custom_route_handler
    
    def parse_validation_error(self, errors: List[Dict]):
        responses = []
        for error in errors:
            responses.append({
                "location": '->'.join(error['loc']),
                "message": error['msg'],
                "type": error['type']
            })
        return responses