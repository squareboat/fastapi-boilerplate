from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton
from .services import UserService

class UserContainer(DeclarativeContainer):
    user_service = Singleton(UserService)