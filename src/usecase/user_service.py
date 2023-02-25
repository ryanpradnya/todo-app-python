import hashlib
from fastapi import Depends, HTTPException, status
from fastapi.concurrency import run_in_threadpool
from fastapi.encoders import jsonable_encoder

from ..dataprovider.repository.user_repository import UserRepository
from ..delivery.dto.user import UpdateUserDTO, ChangePasswordDTO, LoginDTO, RegisterDTO


class UserService:
    def __init__(
            self,
            repository: UserRepository = Depends()
    ) -> None:
        self.repository = repository

    async def login(self, dto: LoginDTO):
        password = hashlib.md5(dto.password.encode("utf-8")).hexdigest()
        result = await run_in_threadpool(lambda: self.repository.find_one_by_username(dto.username))
        if not result or result['password'] != password:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Unauthorized"
            )
        return result

    async def register(self, dto: RegisterDTO):
        password = hashlib.md5(dto.password.encode("utf-8")).hexdigest()
        exist = await run_in_threadpool(lambda: self.repository.find_one_by_username(dto.username))
        if exist:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already taken"
            )
        await run_in_threadpool(lambda: self.repository.create({**jsonable_encoder(dto), "password": password}))
        return await run_in_threadpool(lambda: self.repository.find_one_by_username(dto.username))

    async def update(self, id: str, dto: UpdateUserDTO):
        await self.user_validation(id)

        exist_user = await run_in_threadpool(lambda: self.repository.find_one_by_username(dto.username))
        if exist_user and exist_user["_id"] != id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already taken"
            )

        result = await run_in_threadpool(lambda: self.repository.update(id, jsonable_encoder(obj=dto, exclude_none=True)))
        return result

    async def changePassword(self, dto: ChangePasswordDTO):
        password = hashlib.md5(dto.password.encode("utf-8")).hexdigest()
        new_password = hashlib.md5(dto.newPassword.encode("utf-8")).hexdigest()
        if password == new_password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="New password same as old password"
            )

        exist = await run_in_threadpool(lambda: self.repository.find_one_by_id(dto.id))

        if not exist or exist["password"] != password:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Unauthorized"
            )

        await run_in_threadpool(lambda: self.repository.update(dto.id, {"password": new_password}))
        return {"message": "success"}

    async def user_validation(self, id: str):
        exist = await run_in_threadpool(lambda: self.repository.find_one_by_id(id))
        if not exist:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Unauthorized"
            )
