from fastapi import Depends
from fastapi import status
from dependency_injector.wiring import inject, Provide
from pkgs.core import create_router, Request
from pkgs.core.transformer import transform
from pkgs.common.transformers import UserTransformer
from ..container import UserContainer
from ..services import UserService
from ..validators import CreateUserDTO, UpdateUserDTO

router = create_router('/api/v1')

@router.post('/users')
@inject
async def get_users(data: CreateUserDTO, user_service: UserService = Depends(Provide[UserContainer.user_service])):
    user = await user_service.create_user(data)
    return user

@router.get('/users')
@inject
@transform(UserTransformer)
async def get_users(user_service: UserService = Depends(Provide[UserContainer.user_service])):
    user = await user_service.get_all_users()
    return user


@router.get('/users/{id}')
@transform(UserTransformer)
@inject
async def get_users(id: int, request: Request, user_service: UserService = Depends(Provide[UserContainer.user_service])):
    user = await user_service.get_user_by_id(id)
    return user.to_dict()


@router.patch('/users/{id}', status_code=status.HTTP_204_NO_CONTENT)
@inject
async def get_users(id: int, data: UpdateUserDTO, user_service: UserService = Depends(Provide[UserContainer.user_service])):
    await user_service.update_user_by_id(data, { "id": id })

@router.delete('/users/{id}', status_code=status.HTTP_204_NO_CONTENT)
@inject
async def get_users(id: int, user_service: UserService = Depends(Provide[UserContainer.user_service])):
    await user_service.delete_user_by_id(id)