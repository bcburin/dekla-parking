from pydantic import EmailStr
from fastapi_restful.api_model import APIModel

from server.common.schemas.base import BaseOutSchema


class UserBaseSchema(APIModel):
    username: str
    email: EmailStr
    is_admin: bool


class UserCreateSchema(UserBaseSchema):
    password: str


class UserUpdateSchema(UserBaseSchema):
    username: str | None
    email: EmailStr | None
    is_admin: bool | None
    password_old: str
    password_new: str | None = None

    def has_updates(self) -> bool:
        return bool(self.username) or bool(self.email) or bool(self.password_new) or bool(self.is_admin)


class UserOutSchema(UserBaseSchema, BaseOutSchema):
    id: int

    class Config:
        orm_mode = True
