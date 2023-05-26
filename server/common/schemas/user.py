from fastapi_restful.api_model import APIModel
from pydantic import EmailStr

from server.common.schemas.base import BaseOutSchema, BaseUpdateSchema


class UserBaseSchema(APIModel):
    username: str
    email: EmailStr
    first_name: str
    last_name: str
    is_admin: bool


class UserCreateSchema(UserBaseSchema):
    password: str


class UserUpdateSchema(UserBaseSchema, BaseUpdateSchema):
    username: str | None
    email: EmailStr | None
    first_name: str | None
    last_name: str | None
    is_admin: bool | None
    password: str | None = None


class UserOutSchema(UserBaseSchema, BaseOutSchema):
    id: int

    class Config:
        orm_mode = True
