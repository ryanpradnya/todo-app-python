from typing import Any, List, Optional
from pydantic import BaseModel, Field

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
    userId: str = Field(default="",
                        min_length=24, description="Must be 24-character hex string")
    title: Optional[str] = "Title"
    todoList: Optional[List[TodoList]] = []


class UpdateTodoDTO(BaseModel):
    userId: str = Field(default=None,
                        min_length=24, description="Must be 24-character hex string")
    title: Optional[str]
    status: Optional[TodoStatus] = Field(include=[])
    todoList: Optional[List[TodoList]]


class TodoQuery:
    _id: str = Field(default=None)
    user_id: str = Field(default=None)
    title: str = Field(default=None)
    status: str = Field(default=None)
