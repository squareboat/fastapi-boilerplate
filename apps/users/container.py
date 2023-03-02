from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton
from pkgs.users import UserLibContainer

from .services import UserService

class UserContainer(DeclarativeContainer):
    user_container = UserLibContainer()
    user_service = Singleton(UserService, service=user_container.service)