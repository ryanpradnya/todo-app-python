from typing import Optional
from pydantic import BaseModel, Field, EmailStr


class UpdateUserDTO(BaseModel):
    username: Optional[str] = Field(default=None, regex="^[a-zA-Z0-9]*$",
                                    description="Username must be alpha numeric")
    email: Optional[EmailStr] = Field(default=None)
    name: Optional[str] = Field(
        default=None, regex="^[a-zA-Z0-9\s]*$", description="Name must be alpha numeric and space")


class ResponseUserDTO(BaseModel):
    id: str
    username: str
    email: str
    name: str


class LoginDTO(BaseModel):
    username: str = Field(default="username", regex="^[a-zA-Z0-9]*$",
                          description="Username must be alpha numeric")
    password: str = Field(
        min_length=6, description="Password minimum length 6 character")


class RegisterDTO(LoginDTO):
    email: EmailStr = Field()
    name: Optional[str] = Field(
        default="Name", regex="^[a-zA-Z0-9\s]*$", description="Name must be alpha numeric and space")


class ChangePasswordDTO(BaseModel):
    id: str
    password: str = Field(
        min_length=6, description="Password minimum length 6 character")
    newPassword: str = Field(
        min_length=6, description="New password minimum length 6 character")
