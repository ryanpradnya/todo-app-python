from fastapi import APIRouter, Depends, Path, status

from ...delivery.dto.user import UpdateUserDTO, ChangePasswordDTO, LoginDTO, RegisterDTO, ResponseUserDTO
from ...usecase.user_service import UserService


router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@router.post(
    path="/login",
    status_code=status.HTTP_200_OK,
    response_model=ResponseUserDTO,
    response_model_exclude_unset=True
)
async def login(dto: LoginDTO, service: UserService = Depends()):
    return await service.login(dto)


@router.post(
    path="/register",
    status_code=status.HTTP_201_CREATED,
    response_model=ResponseUserDTO,
    response_model_exclude_unset=True
)
async def get_company(dto: RegisterDTO, service: UserService = Depends()):
    return await service.register(dto)


@router.put(
    path='/update/{id}',
    response_model=ResponseUserDTO,
    response_model_exclude_unset=True
)
async def add_company(dto: UpdateUserDTO, id: str = Path(min_length=24), service: UserService = Depends()):
    return await service.update(id, dto)


@router.put(
    path='/change-password',
)
async def update_company(dto: ChangePasswordDTO, service: UserService = Depends()):
    return await service.changePassword(dto)
