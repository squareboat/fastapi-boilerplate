from fastapi import APIRouter

def create_router(route_prefix: str):
    return APIRouter(prefix=route_prefix)