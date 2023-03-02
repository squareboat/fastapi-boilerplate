from typing import Dict
from fastapi import Depends, HTTPException
from dependency_injector.wiring import inject, Provide
from pkgs.core import create_router
from ..container import UserContainer
from ..services import UserService
from ..validators.user import UserModel
router = create_router('/api/v1')

@router.post('/users')
@inject
async def get_users(user: UserModel, user_service: UserService = Depends(Provide[UserContainer.user_service]), db = Depends(Provide[UserContainer.db])) -> Dict:
    return user_service.greet()
