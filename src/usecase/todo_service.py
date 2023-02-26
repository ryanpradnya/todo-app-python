from typing import Any
from fastapi import Depends, HTTPException, status
from fastapi.concurrency import run_in_threadpool
from fastapi.encoders import jsonable_encoder
from camel_converter import dict_to_snake, dict_to_camel

from ..delivery.query.pagination_query import BasePaginationQuery
from ..delivery.enum.todo_enum import TodoStatus
from ..usecase.user_service import UserService
from ..delivery.dto.todo import CreateTodoDTO, ResponseTodoDTO, UpdateTodoDTO
from ..dataprovider.repository.todo_repository import TodoRepository


class TodoService:
    def __init__(
            self,
            repository: TodoRepository = Depends(),
            user_service: UserService = Depends(),
    ) -> None:
        self.repository = repository
        self.user_service = user_service

    def find_by_user_id(self, query: BasePaginationQuery):
        pass

    async def find_one_by_id(self, id: str):
        result = await run_in_threadpool(
            lambda: self.repository.find_one_by_id(id)
        )

        return result

    async def create(self, dto: CreateTodoDTO):
        data = dict_to_snake(jsonable_encoder(dto))
        await self.user_service.user_validation(dto.userId)
        result = await run_in_threadpool(
            lambda: self.repository.create({
                **data,
                "status": TodoStatus.active.value
            })
        )
        return await self.find_one_by_id(result.inserted_id)

    async def update(self, id: str, dto: UpdateTodoDTO):
        todo = await self.find_one_by_id(id)
        print(todo)
        print(dto)

        if not todo:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Data not found"
            )
        elif todo["userId"] != dto.userId:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Unauthorized"
            )

        return await run_in_threadpool(
            lambda: self.repository.update(
                id,
                jsonable_encoder(obj=dto, exclude_none=True)
            )
        )
