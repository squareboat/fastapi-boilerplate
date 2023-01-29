from typing import Dict, TYPE_CHECKING
from fastapi import Depends
from dependency_injector.wiring import inject, Provide
from pkgs.core import create_router
from pkgs.core.http import HTTPResponse
from ..container import UserContainer
from ..services import UserService

router = create_router('/api/v1')
router.default_response_class = HTTPResponse

@router.get('/users')
@inject
def get_users(user_service: UserService = Depends(Provide[UserContainer.user_service])) -> Dict:
    return user_service.greet()