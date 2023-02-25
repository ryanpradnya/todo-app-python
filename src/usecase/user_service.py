import hashlib
from typing import Any
from fastapi import Depends, HTTPException, status
from fastapi.concurrency import run_in_threadpool
from fastapi.encoders import jsonable_encoder
from ..dataprovider.model.user_model import UserModel
from ..dataprovider.repository.user_repository import UserRepository
from ..delivery.dto.user import LoginDTO, RegisterDTO


class UserService:
    def __init__(
            self,
            repository: UserRepository = Depends()
    ) -> None:
        self.repository = repository

    def login(self, dto: LoginDTO):
        password = hashlib.md5(dto.password.encode("utf-8")).hexdigest()
        print(password)
        # result = await run_in_threadpool(lambda: self.repository.find_one_by_username(dto.username))
        result = self.repository.find_one_by_username(dto.username)
        print("=============>", result)
        if not result:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Unauthorized"
            )
        return result

    def register(self, dto: RegisterDTO):
        password = hashlib.md5(dto.password.encode("utf-8")).hexdigest()
        # user = UserModel(
        #     *dto,
        #     password=password
        # )
        # print("=======>", user)
        # result = await run_in_threadpool(
        #     lambda: self.repository.create(UserModel(
        #         **dto,
        #         password=password
        #     ))
        # )
        result = self.repository.create(
            jsonable_encoder(dto))
        if not result:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Bad Request"
            )
        return result

    def update(self, RegisterDTO: Any):
        pass

    def changePassword(self, RegisterDTO: Any):
        pass
