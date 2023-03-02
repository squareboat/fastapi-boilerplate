from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Resource
from .database import init_db, close_db
class CoreContainer:
    db = Resource(
        init_db
    )

core_container = CoreContainer()