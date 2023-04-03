from dependency_injector.wiring import inject

from pkgs.core import DBRepository

@inject
class UserRepository(DBRepository):
    pass