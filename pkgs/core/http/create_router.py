from fastapi import APIRouter
from .response import HTTPResponse 
from .exception import ExceptionHandler

def create_router(route_prefix: str):
    router = APIRouter(prefix=route_prefix)
    router.route_class = ExceptionHandler
    router.default_response_class = HTTPResponse
    
    return router