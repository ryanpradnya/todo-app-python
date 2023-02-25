from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from ...delivery.dto.user import UpdateUserDTO, ChangePasswordDTO, LoginDTO, RegisterDTO, ResponseUserDTO
from ...usecase.user_service import UserService


router = APIRouter(
    prefix="/users",
    tags=["user"]
)


@router.post(
    path="/login",
    status_code=status.HTTP_200_OK,
    response_model=ResponseUserDTO,
    response_model_exclude_unset=True
)
async def login(dto: LoginDTO, service: UserService = Depends()):
    result = await service.login(dto)
    return JSONResponse(content=jsonable_encoder(result))


@router.post(
    path="/register",
    status_code=status.HTTP_201_CREATED,
    response_model=ResponseUserDTO,
    response_model_exclude_unset=True
)
async def get_company(dto: RegisterDTO, service: UserService = Depends()):
    result = await service.register(dto)
    return JSONResponse(content=jsonable_encoder(result))


@router.put(
    path='/update/{id}',
    status_code=status.HTTP_200_OK,
    response_model=ResponseUserDTO,
    response_model_exclude_unset=True
)
async def add_company(id: str, dto: UpdateUserDTO, service: UserService = Depends()):
    result = await service.update(id, dto)
    return JSONResponse(content=jsonable_encoder(result))


@router.put(
    path='/change-password',
    status_code=status.HTTP_200_OK,
)
async def update_company(dto: ChangePasswordDTO, service: UserService = Depends()):
    result = await service.changePassword(dto)
    return JSONResponse(content=jsonable_encoder(result))
