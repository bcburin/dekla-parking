from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_restful.cbv import cbv
from sqlalchemy.orm import Session
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

from server.database.config import get_db
from server.database.user import UserCRUD
from server.schemas.user import UserOut, UserCreate, UserUpdate
from server.utils.security import create_access_token, authenticate_user, get_current_user

router = APIRouter(prefix='/users', tags=['users'])


@router.post(path='/token')
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db=Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail='Incorrect username or password.')
    access_token = create_access_token(data={'sub': user.username})
    return {'access_token': access_token, 'token_type': 'bearer'}


@cbv(router)
class UserCBV:
    db: Session = Depends(get_db)

    @router.get(path='/', response_model=list[UserOut])
    def get_all_users(self, skip: int = Query(default=0, ge=0), limit: int | None = Query(default=100, ge=0)):
        return UserCRUD(self.db).get_all(skip=skip, limit=limit)

    @router.get(path='/me', response_model=UserOut)
    def get_user_me(self, current_user: Annotated[UserOut, Depends(get_current_user)]):
        return current_user

    @router.get(path='/{user_id}', response_model=UserOut)
    def get_user_by_id(self, user_id: int):
        user = UserCRUD(self.db).get_by_id(user_id)
        if not user:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND)
        return user

    @router.get(path='/email/{email}', response_model=UserOut)
    def get_user_by_email(self, email: str):
        user = UserCRUD(self.db).get_by_email(email=email)
        if not user:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND)
        return user

    @router.get(path='/username/{username}', response_model=UserOut)
    def get_user_by_username(self, username: str):
        user = UserCRUD(self.db).get_by_username(username=username)
        if not user:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND)
        return user

    # @router.get(path='/me', response_model=UserOut)
    # def get_user_me(self, current_user: Annotated[UserOut, Depends(get_current_user)]):
    #     return current_user

    @router.post(path='/', response_model=UserOut)
    def create_user(self, user: UserCreate):
        user_db = UserCRUD(self.db).get_by_username(username=user.username)
        if user_db:
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=f'{user_db.username} already exists')
        created_user = UserCRUD(self.db).create(user=user)
        return created_user

    @router.put(path='/{user_id}', response_model=UserOut)
    def update_user(self, user_id: int, user: UserUpdate):
        db_user = UserCRUD(self.db).get_by_id(user_id)
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
