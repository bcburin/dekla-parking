from typing import Any

from sqlalchemy.orm import Session

from server.common.models.user import UserModel
from server.common.schemas.user import UserCreate, UserUpdate
import server.common.utils.security as sec
from server.database.basecrud import BaseCRUD


class UserCRUD(BaseCRUD[UserModel, UserCreate, UserUpdate]):

    def __init__(self, db: Session):
        super().__init__(UserModel, db)

    def get_by_username(self, username: str) -> UserModel | None:
        return self.get_by_id(username, 'username')

    def get_by_email(self, email: str) -> UserModel | None:
        return self.get_by_id(email, 'email')

    def create(self, *, user: UserCreate, refresh: bool = True) -> UserModel:
        password_hash = sec.get_password_hash(user.password)
        user_data = {
            **user.dict(),
            'password_hash': password_hash,
        }
        del user_data['password']
        db_user = UserModel(**user_data)
        self.db.add(db_user)
        self.db.commit()
        if refresh:
            self.db.refresh(db_user)
        return db_user

    def update(self, db_user: UserModel, user: UserUpdate | dict[str, Any]) -> UserModel:
        if isinstance(user, dict):
            update_data = user
        else:
            update_data = user.dict(exclude_unset=True)
        if 'password_new' in update_data:
            password_new_hash = sec.get_password_hash(update_data['password_new'])
            update_data['password_hash'] = password_new_hash
            del update_data['password_new']
        return super().update(db_obj=db_user, obj=update_data)
