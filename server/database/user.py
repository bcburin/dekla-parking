from typing import Any

from sqlalchemy.orm import Session

from server.common.models.user import UserModel
from server.common.schemas.user import UserCreateSchema, UserUpdateSchema
import server.services.auth as auth
from server.database.basedbmanager import BaseDbManager


class UserDbManager(BaseDbManager[UserModel, UserCreateSchema, UserUpdateSchema]):

    def __init__(self, db: Session):
        super().__init__(model=UserModel, db=db)

    def get_by_username(self, username: str) -> UserModel | None:
        return self.get_by_unique_attribute(username, 'username')

    def get_by_email(self, email: str) -> UserModel | None:
        return self.get_by_unique_attribute(email, 'email')

    def create(self, *, obj: UserCreateSchema, refresh: bool = True) -> UserModel:
        password_hash = auth.get_password_hash(obj.password)
        user_data = {
            **obj.dict(),
            'password_hash': password_hash,
        }
        del user_data['password']
        db_user = UserModel(**user_data)
        self.db.add(db_user)
        self.db.commit()
        if refresh:
            self.db.refresh(db_user)
        return db_user

    def update(self, db_obj: UserModel, obj: UserUpdateSchema | dict[str, Any]) -> UserModel:
        if isinstance(obj, dict):
            update_data = obj
        else:
            update_data = obj.dict(exclude_unset=True)
        if 'password_new' in update_data:
            password_new_hash = auth.get_password_hash(update_data['password_new'])
            update_data['password_hash'] = password_new_hash
            del update_data['password_new']
        return super().update(db_obj=db_obj, obj=update_data)
