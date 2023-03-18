from dependency_injector.wiring import inject

from uuid import uuid4
from pkgs.users.services import UserLibService
from ..validators import CreateUserDTO, UpdateUserDTO

@inject
class UserService:
    def __init__(self, service: UserLibService) -> None:
        self.service = service

    async def create_user(self, data: CreateUserDTO):
        payload = data.dict()
        payload['uuid'] = uuid4()
        return await self.service.repo.create(payload)
    
    async def get_all_users(self):
        return await self.service.repo.all()
    
    async def get_user_by_id(self, id: int):
        return await self.service.repo.first_where({ "id": id })
    
    async def update_user_by_id(self, data: UpdateUserDTO, filter):
        return await self.service.repo.update_where(filter, data.dict(exclude_none=True))
    
    async def delete_user_by_id(self, id: int):
        return await self.service.repo.delete_where({ "id": id })

