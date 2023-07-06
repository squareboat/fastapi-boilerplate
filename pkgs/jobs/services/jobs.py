from dependency_injector.wiring import inject

from ..repositories import JobRepository


@inject
class JobLibService:
    def __init__(self, repo: JobRepository) -> None:
        self.repo = repo
