from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str | None = None
    email: EmailStr | None = None


class UserCreate(UserBase):
    username: str
    email: EmailStr
    password: str


class UserUpdate(UserBase):
    password: str | None = None


class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True
