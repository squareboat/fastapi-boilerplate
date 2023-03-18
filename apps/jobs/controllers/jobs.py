from fastapi import Depends
from fastapi import status
from dependency_injector.wiring import inject, Provide
from pkgs.core import create_router
# from pkgs.core.transformer import transform
# from pkgs.common.transformers import UserTransformer
from ..container import JobContainer
from ..services import JobService
from ..validators import CreateJobDTO, UpdateJobDTO

router = create_router('/api/v1')

@router.post('/jobs')
@inject
async def create_job(data: CreateJobDTO, job_service: JobService = Depends(Provide[JobContainer.job_service])):
    job = await job_service.create_job(data)
    return job

@router.get('/jobs')
@inject
# @transform(UserTransformer)
async def get_jobs(job_service: JobService = Depends(Provide[JobContainer.job_service])):
    jobs = await job_service.get_all_job()
    return jobs


@router.get('/jobs/{id}')
# @transform(UserTransformer)
@inject
async def get_job(id: int, job_service: JobService = Depends(Provide[JobContainer.job_service])):
    job = await job_service.get_job_by_id(id)
    return job.to_dict()


@router.patch('/jobs/{id}', status_code=status.HTTP_204_NO_CONTENT)
@inject
async def update_job(id: int, data: UpdateJobDTO, job_service: JobService = Depends(Provide[JobContainer.job_service])):
    await job_service.update_job_by_id(data, { "id": id })

@router.delete('/jobs/{id}', status_code=status.HTTP_204_NO_CONTENT)
@inject
async def delete_job(id: int, job_service: JobService = Depends(Provide[JobContainer.job_service])):
    await job_service.delete_job(id)