from fastapi import Depends
from fastapi import status
from dependency_injector.wiring import inject, Provide
from pkgs.core import create_router
from pkgs.core.transformer import transform
from pkgs.core.validators import validate
from pkgs.common.transformers import JobTransformer
from pkgs.common.validators import CreateJob, PathParams
from pkgs.core.http import Request
from ..container import JobContainer
from ..services import JobService
from ..validators import UpdateJobDTO

router = create_router('/api/v1')

@router.post('/jobs')
@inject
@validate(CreateJob)
async def create_job(request: Request, inputs: CreateJob, job_service: JobService = Depends(Provide[JobContainer.job_service])):
    job = await job_service.create_job(inputs)
    return job

@router.get('/jobs')
@inject
@transform(JobTransformer)
async def get_jobs(request: Request, job_service: JobService = Depends(Provide[JobContainer.job_service])):
    jobs = await job_service.get_all_job()
    return list(map(lambda x: x.to_dict(), jobs))


@validate(PathParams)
@router.get('/jobs/{id}')
@inject
@transform(JobTransformer)
async def get_job(request: Request, id: int, job_service: JobService = Depends(Provide[JobContainer.job_service])):
    job = await job_service.get_job_by_id({})
    return job.to_dict()


@router.patch('/jobs/{id}', status_code=status.HTTP_204_NO_CONTENT)
@inject
async def update_job(id: int, data: UpdateJobDTO, job_service: JobService = Depends(Provide[JobContainer.job_service])):
    await job_service.update_job_by_id(data, { "id": id })

@router.delete('/jobs/{id}', status_code=status.HTTP_204_NO_CONTENT)
@inject
async def delete_job(id: int, job_service: JobService = Depends(Provide[JobContainer.job_service])):
    await job_service.delete_job(id)