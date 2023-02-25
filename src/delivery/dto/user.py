from typing import Optional
from pydantic import BaseModel


class BaseUserDTO(BaseModel):
    username: str
    email: str
    name: str


class ResponseUserDTO(BaseUserDTO):
    id: str


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
