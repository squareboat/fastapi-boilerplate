from dependency_injector.wiring import inject

from pkgs.core.database import DBRepository

@inject
class JobRepository(DBRepository):
    pass