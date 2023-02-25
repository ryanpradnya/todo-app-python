from typing import List, Optional
import uuid
from pydantic import BaseModel, EmailStr, Field


class TodoListModel(BaseModel):
    description: str = Field()
    is_done: bool = Field(False, ...)


class TodoModel(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    user_id: str = Field(...)
    title: str = Field(...)
    is_active: bool = Field(True, ...)
    todo_list: List[TodoListModel] = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "title": "work",
                "is_active": True,
                "todo_list": [
                    {
                        "description": "javascript",
                        "is_done": False
                    },
                    {
                        "description": "python",
                        "is_done": True
                    }
                ]
            }
        }


class TodoUpdateModel(BaseModel):
    title: Optional[str]
    is_active: Optional[bool]
    todo_list: Optional[List[TodoListModel]]

    class Config:
        schema_extra = {
            "example": {
                "title": "work",
                "is_active": True,
                "todo_list": [
                    {
                        "description": "javascript",
                        "is_done": False
                    },
                    {
                        "description": "python",
                        "is_done": True
                    }
                ]
            }
        }
