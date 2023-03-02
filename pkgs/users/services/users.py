from dependency_injector.wiring import inject

from ..repositories import UserRepository


@inject
class UserLibService:
    def __init__(self, repo: UserRepository) -> None:
        self.repo = repo
