
from fastapi import FastAPI
from dependency_injector.containers import DeclarativeContainer

def create_server(Container: DeclarativeContainer, controllers) -> FastAPI:
    container = Container()
    container.wire(modules=controllers)
    app = FastAPI()
    app.container = container
    for controller in controllers:
        app.include_router(controller.router)
    return app