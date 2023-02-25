from typing import List, Optional
from pydantic import BaseModel

from ...delivery.enum.todo_enum import TodoStatus


class TodoList(BaseModel):
    description: str
    isDone: bool


class ResponseTodoDTO(BaseModel):
    id: str
    userId: str
    title: str
    status: TodoStatus
    todoList: List[TodoList]


class CreateTodoDTO(BaseModel):
    userId: str
    title: Optional[str] = ""
    todoList: Optional[List[TodoList]] = []


class UpdateTodoDTO(BaseModel):
    title: Optional[str]
    status: Optional[TodoStatus]
    todoList: Optional[List[TodoList]]
