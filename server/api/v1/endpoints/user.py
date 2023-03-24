from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi_restful.cbv import cbv
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

from server.database.config import get_db
from server.database.user import UserCRUD
from server.schemas.user import UserOut, UserCreate, UserUpdate

router = APIRouter(prefix='/users', tags=['users'])


@cbv(router)
class UserCBV:
    db = Depends(get_db)

    @router.get(path='/', response_model=list[UserOut])
    def get_all_users(self, skip: int = Query(default=0, ge=0), limit: int | None = Query(default=100, ge=0)):
        return UserCRUD(self.db).get_all(skip=skip, limit=limit)

    @router.get(path='/{user_id}', response_model=UserOut)
    def get_user_by_id(self, user_id: int):
        user = UserCRUD(self.db).get_by_id(user_id)
        if not user:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND)
        return user

    @router.get(path='/find', response_model=UserOut)
    def get_user_by_index(self, username: str | None = None, email: str | None = None):
        if not username and not email:
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail='A username or email must be specified.')
        user = None
        if username:
            user = UserCRUD(self.db).get_by_username(username)
        elif email:
            user = UserCRUD(self.db).get_by_email(email)
        if not user:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND)
        return user

    @router.post(path='/', response_model=UserOut)
    def create_user(self, user: UserCreate):
        user_db = UserCRUD(self.db).get_by_username(username=user.username)
        if user_db:
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=f'{user_db.username} already exists')
        created_user = UserCRUD(self.db).create(user=user)
        return created_user

    @router.put(path='/{user_id}', response_model=UserOut)
    def update_user(self, user_id: int, user: UserUpdate):
        db_user, authenticated = UserCRUD(self.db).authenticate(id=user_id, password=user.password)
        if not authenticated:
            raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail='Password authentication failed.')
        if not db_user:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND)
        if not user.has_updates():
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail='No updates provided.')
        updated_user = UserCRUD(self.db).update(db_user=db_user, user=user)
        return updated_user

    @router.delete(path='/{user_id}', response_model=UserOut)
    def delete_user(self, user_id: int):
        deleted_user = UserCRUD(self.db).remove(pk=user_id)
        if not deleted_user:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND)
        return deleted_user
