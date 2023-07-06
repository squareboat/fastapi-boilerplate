from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton
from pkgs.jobs import JobLibContainer

from .services import JobService

class JobContainer(DeclarativeContainer):
    job_container = JobLibContainer()
    job_service = Singleton(JobService, service=job_container.service)