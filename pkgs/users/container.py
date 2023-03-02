from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton
from pkgs.core import core_container
from pkgs.common.models.user import UserModel

from .services import UserLibService
from .repositories import UserRepository

class UserLibContainer(DeclarativeContainer):
    repo = Singleton(UserRepository, db=core_container.db, model=UserModel)
    service = Singleton(UserLibService, repo=repo)