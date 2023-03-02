from typing import Dict
from dependency_injector.wiring import inject

from pkgs.users.services import UserLibService

@inject
class UserService:
    def __init__(self, service: UserLibService) -> None:
        self.service = service

    async def get_all(self):
        users = await self.service.repo.all()
        return users