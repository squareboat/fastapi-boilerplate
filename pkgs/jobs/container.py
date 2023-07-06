from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton
from pkgs.core import core_container

from .models import JobModel
from .services import JobLibService
from .repositories import JobRepository

class JobLibContainer(DeclarativeContainer):
    repo = Singleton(JobRepository, db=core_container.db, model=JobModel)
    service = Singleton(JobLibService, repo=repo)