from typing import Optional
import uuid
from pydantic import BaseModel, EmailStr, Field


class UserModel(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    username: str = Field(...)
    email: str = Field(...)
    name: str = Field()
    password: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "username": "johndoe",
                "email": "jdoe@email.com",
                "name": "John Doe",
                "password": "password"
            }
        }


class UserUpdateModel(BaseModel):
    username: Optional[str]
    email: Optional[str]
    name: Optional[str]
    password: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "username": "johndoe",
                "email": "jdoe@email.com",
                "name": "John Doe",
                "password": "password"
            }
        }
