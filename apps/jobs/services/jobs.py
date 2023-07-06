from dependency_injector.wiring import inject

from uuid import uuid4
from pkgs.jobs.services import JobLibService
from ..validators import CreateJobDTO, UpdateJobDTO

@inject
class JobService:
    def __init__(self, service: JobLibService) -> None:
        self.service = service

    async def create_job(self, data: CreateJobDTO):
        payload = data.dict()
        payload['uuid'] = uuid4()
        return await self.service.repo.create(payload)
    
    async def get_all_job(self):
        return await self.service.repo.all(relations=['created_by'])
    
    async def get_job_by_id(self, id: int):
        return await self.service.repo.first_where({ "id": id }, relations=['created_by'])
    
    async def update_job_by_id(self, data: UpdateJobDTO, filter):
        return await self.service.repo.update_where(filter, data.dict(exclude_none=True))
    
    async def delete_job_by_id(self, id: int):
        return await self.service.repo.delete_where({ "id": id })

