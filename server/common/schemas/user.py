from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str | None = None
    email: EmailStr | None = None


class UserCreate(UserBase):
    username: str
    email: EmailStr
    password: str


class UserUpdate(UserBase):
    password: str
    password_new: str | None = None

    def has_updates(self) -> bool:
        return bool(self.username) or bool(self.email) or bool(self.password_new)


class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True
