from typing import Any
from fastapi import Depends

from ..dataprovider.repository.todo_repository import TodoRepository


class TodoService:
    def __init__(
            self,
            repository: TodoRepository = Depends()
    ) -> None:
        self.repository = repository

    def find_by_user_id(self, LoginDTO: Any):
        pass

    def find_one_by_id(self, RegisterDTO: Any):
        pass

    def create(self, CreateTodoDTO: Any):
        pass

    def update(self, UpdateTodoDTO: Any):
        pass

    def update(self, DeleteTodoDTO: Any):
        pass
