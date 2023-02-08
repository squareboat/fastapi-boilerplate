from fastapi import FastAPI
from dependency_injector.containers import DeclarativeContainer
from .response import HTTPResponse 

def create_server(container: DeclarativeContainer, controllers) -> FastAPI:
    container = container()
    container.wire(modules=controllers)
    app = FastAPI(default_response_class=HTTPResponse)
    app.container = container
    for controller in controllers:
        app.include_router(controller.router)
    return app
