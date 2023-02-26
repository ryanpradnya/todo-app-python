from typing import Any, List, Optional
from pydantic import BaseModel

from ...delivery.enum.todo_enum import TodoStatus


class TodoList(BaseModel):
    description: str = "Todo list"
    isDone: Optional[bool] = False


class ResponseTodoDTO(BaseModel):
    id: str
    userId: str
    title: str
    status: TodoStatus
    todoList: List[TodoList]


class CreateTodoDTO(BaseModel):
    userId: str = ""
    title: Optional[str] = "Title"
    todoList: Optional[List[TodoList]] = []


class UpdateTodoDTO(BaseModel):
    userId: str
    title: Optional[str]
    status: Optional[TodoStatus]
    todoList: Optional[List[TodoList]]
