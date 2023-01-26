from fastapi import Depends
from dependency_injector.wiring import inject, Provide
from pkgs.core import create_router
from ..container import UserContainer
from ..services import UserService

router = create_router('/api/v1')

@router.get('/users')
@inject
def get_users(user_service: UserService = Depends(Provide[UserContainer.user_service])):
    return user_service.greet()