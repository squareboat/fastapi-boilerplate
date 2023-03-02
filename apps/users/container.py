from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton
from pkgs.core import core_container
from .services import UserService

class UserContainer(DeclarativeContainer):
    user_service = Singleton(UserService)
    db = core_container.db