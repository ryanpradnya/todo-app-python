from typing import Optional
from pydantic import BaseModel


class UpdateUserDTO(BaseModel):
    username: Optional[str]
    email: Optional[str]
    name: Optional[str]


class ResponseUserDTO(BaseModel):
    id: str
    username: str
    email: str
    name: str


class LoginDTO(BaseModel):
    username: str
    password: str


class RegisterDTO(LoginDTO):
    email: str
    name: Optional[str]


class ChangePasswordDTO(BaseModel):
    id: str
    password: str
    newPassword: str
