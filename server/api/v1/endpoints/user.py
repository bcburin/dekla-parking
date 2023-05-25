from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_restful.cbv import cbv
from sqlalchemy.orm import Session
from starlette.status import HTTP_400_BAD_REQUEST

from server.api.v1.endpoints.base import register_db_routes
from server.common.models.user import UserModel
from server.common.schemas.booking import BookingOutSchema
from server.common.schemas.label import LabelOutSchema
from server.common.schemas.labeling import LabelingCreateForUserSchema, LabelingOutSchema, \
    LabelingRequestType
from server.database.config import get_db
from server.common.schemas.user import UserOutSchema, UserCreateSchema, UserUpdateSchema
from server.common.utils.authentication import create_access_token, authenticate_user, get_current_user
from server.services.user import UserService

router = APIRouter(prefix='/users', tags=['users'])


register_db_routes(
    router=router,
    service=UserService,
    model=UserModel,
    create_schema=UserCreateSchema,
    update_schema=UserUpdateSchema,
    out_schema=UserOutSchema
)


@cbv(router)
class UserAPI:
    db: Session = Depends(get_db)

    @router.post(path='/login')
    async def login(self, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
        user = authenticate_user(self.db, email=form_data.username, password=form_data.password)
        if not user:
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail='Incorrect username or password.')
        access_token = create_access_token(data={'sub': user.username})
        return {'access_token': access_token, 'token_type': 'bearer'}

    @router.get(path='/me', response_model=UserOutSchema)
    def get_user_me(self, current_user: Annotated[UserOutSchema, Depends(get_current_user)]):
        return current_user

    @router.get(path='/emails/{email}', response_model=UserOutSchema)
    def get_user_by_email(self, email: str):
        return UserService(self.db).get_by_unique_attribute(email, 'email')

    @router.get(path='/usernames/{username}', response_model=UserOutSchema)
    def get_user_by_username(self, username: str):
        return UserService(self.db).get_by_unique_attribute(username, 'username')

    @router.put(path='/{user_id}/toggle-admin', response_model=UserOutSchema)
    def toggle_user_is_admin(self, user_id: int):
        return UserService(self.db).toggle_is_admin(user_id)

    @router.post(path='/{user_id}/labelings', response_model=list[LabelingOutSchema])
    def add_labeling_to_user(self, user_id: int, user_labelings: list[LabelingCreateForUserSchema]):
        UserService(self.db).add_labelings_to_user(user_id=user_id, user_labelings=user_labelings)
        return UserService(self.db).get_user_labelings(user_id=user_id, labeling_type=LabelingRequestType.all)

    @router.delete(path='/{user_id}/labelings', response_model=list[LabelingOutSchema])
    def remove_labeling_from_user(self, user_id: int, label_ids: list[int]):
        UserService(self.db).remove_labelings_from_user(user_id=user_id, labeling_ids=label_ids)
        return UserService(self.db).get_user_labelings(user_id=user_id, labeling_type=LabelingRequestType.all)

    @router.get('/{user_id}/labelings', response_model=list[LabelingOutSchema])
    def get_user_labelings(self, user_id: int, labeling_type: LabelingRequestType | None = None):
        return UserService(self.db).get_user_labelings(user_id=user_id, labeling_type=labeling_type)

    @router.get('/{user_id}/labels', response_model=list[LabelOutSchema])
    def get_user_active_labels(self, user_id: int):
        return UserService(self.db).get_active_user_labels(user_id)

    @router.get('{user_id}/bookings', response_model=list[BookingOutSchema])
    def get_user_bookings(self, user_id: int):
        return UserService(self.db).get_user_bookings(user_id)
