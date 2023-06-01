from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_restful.cbv import cbv
from sqlalchemy.orm import Session
from starlette.status import HTTP_400_BAD_REQUEST

from server.api.v1.endpoints.base import register_db_routes, RouteType
from server.common.exceptions.auth import AuthException
from server.common.models.user import UserModel
from server.common.schemas.booking import BookingOutSchema, BookingCreateForUserSchema
from server.common.schemas.label import LabelOutSchema
from server.common.schemas.labeling import LabelingCreateForUserSchema, LabelingOutSchema
from server.common.schemas.base import ActivityRequestType
from server.database.config import get_db
from server.common.schemas.user import UserOutSchema, UserCreateSchema, UserUpdateSchema
from server.services.auth import create_access_token, authenticate_user, AuthReq, CurrentUser
from server.services.user import UserService

router = APIRouter(prefix='/users', tags=['users'])


register_db_routes(
    router=router,
    service=UserService,
    model=UserModel,
    create_schema=UserCreateSchema,
    update_schema=UserUpdateSchema,
    out_schema=UserOutSchema,
    omit=[RouteType.get_by_id, RouteType.update, RouteType.delete],
    auth={
        RouteType.create: AuthReq.no_auth_restrictions,
    }
)


@cbv(router)
class UserAPI:
    db: Session = Depends(get_db)

    @router.get(path='/me', response_model=UserOutSchema)
    def get_user_me(self, current_user: CurrentUser):
        if not current_user:
            raise AuthException('Not Authenticated')
        return current_user

    @router.get(
        '/{id}',
        response_model=UserOutSchema,
        dependencies=[Depends(AuthReq.current_user_is_authenticated)]
    )
    def get_user_by_id(self, id: int, current_user: CurrentUser, db: Session = Depends(get_db)):
        if id != current_user.id and not current_user.is_admin:
            raise AuthException('Not Authenticated')
        return UserService(db=db).get_by_id(id=id)

    @router.put(
        '/{id}',
        response_model=UserOutSchema,
        dependencies=[Depends(AuthReq.current_user_is_authenticated)]
    )
    def update_user(
            self,
            id: int,
            user: UserUpdateSchema,
            current_user: CurrentUser,
            db: Session = Depends(get_db)
    ):
        if id != current_user.id and not current_user.is_admin:
            raise AuthException('Not Authenticated')
        return UserService(db=db).update(id=id, obj=user)

    @router.delete(
        '/{id}',
        response_model=UserOutSchema,
        dependencies=[Depends(AuthReq.current_user_is_authenticated)]
    )
    def delete_user(
            self,
            id: int,
            current_user: CurrentUser,
            db: Session = Depends(get_db)
    ):
        if id != current_user.id and not current_user.is_admin:
            raise AuthException('Not Authenticated')
        return UserService(db=db).delete(id=id)

    @router.post(path='/login')
    async def login(self, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
        user = authenticate_user(self.db, email=form_data.username, password=form_data.password)
        if not user:
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail='Incorrect email or password.')
        access_token = create_access_token(data={'sub': user.username})
        return {'access_token': access_token, 'token_type': 'bearer'}

    @router.get(
        path='/emails/{email}',
        response_model=UserOutSchema,
        dependencies=[Depends(AuthReq.current_user_has_permission)])
    def get_user_by_email(self, email: str):
        return UserService(self.db).get_by_unique_attribute(email, 'email')

    @router.get(
        path='/usernames/{username}',
        response_model=UserOutSchema,
        dependencies=[Depends(AuthReq.current_user_has_permission)])
    def get_user_by_username(self, username: str):
        return UserService(self.db).get_by_unique_attribute(username, 'username')

    @router.put(
        path='/{user_id}/toggle-admin',
        response_model=UserOutSchema,
        dependencies=[Depends(AuthReq.current_user_has_permission)])
    def toggle_user_is_admin(self, user_id: int):
        return UserService(self.db).toggle_is_admin(user_id)

    @router.post(
        path='/{user_id}/labelings',
        response_model=list[LabelingOutSchema],
        dependencies=[Depends(AuthReq.current_user_has_permission)])
    def add_labeling_to_user(self, user_id: int, user_labelings: list[LabelingCreateForUserSchema]):
        UserService(self.db).add_labelings_to_user(user_id=user_id, user_labelings=user_labelings)
        return UserService(self.db).get_user_labelings(user_id=user_id, labeling_type=ActivityRequestType.all)

    @router.delete(
        path='/{user_id}/labelings',
        response_model=list[LabelingOutSchema],
        dependencies=[Depends(AuthReq.current_user_has_permission)])
    def remove_labeling_from_user(self, user_id: int, label_ids: list[int]):
        UserService(self.db).remove_labelings_from_user(user_id=user_id, labeling_ids=label_ids)
        return UserService(self.db).get_user_labelings(user_id=user_id, labeling_type=ActivityRequestType.all)

    @router.get(
        '/{user_id}/labelings',
        response_model=list[LabelingOutSchema],
        dependencies=[Depends(AuthReq.current_user_has_permission)])
    def get_user_labelings(self, user_id: int, labeling_type: ActivityRequestType | None = None):
        return UserService(self.db).get_user_labelings(user_id=user_id, labeling_type=labeling_type)

    @router.get(
        '/{user_id}/labels',
        response_model=list[LabelOutSchema],
        dependencies=[Depends(AuthReq.current_user_has_permission)])
    def get_user_active_labels(self, user_id: int):
        return UserService(self.db).get_active_user_labels(user_id)

    @router.post(
        path='/{user_id}/bookings',
        response_model=list[BookingOutSchema],
        dependencies=[Depends(AuthReq.current_user_has_permission)])
    def add_booking_to_user(self, user_id: int, user_bookings: list[BookingCreateForUserSchema]):
        UserService(self.db).add_bookings_to_user(user_id=user_id, user_bookings=user_bookings)
        return UserService(self.db).get_user_bookings(user_id=user_id, booking_type=ActivityRequestType.all)

    @router.delete(
        path='/{user_id}/bookings',
        response_model=list[LabelingOutSchema],
        dependencies=[Depends(AuthReq.current_user_has_permission)])
    def remove_booking_from_user(self, user_id: int, label_ids: list[int]):
        UserService(self.db).remove_bookings_from_user(user_id=user_id, booking_ids=label_ids)
        return UserService(self.db).get_user_bookings(user_id=user_id, booking_type=ActivityRequestType.all)

    @router.get(
        '{user_id}/bookings',
        response_model=list[BookingOutSchema],
        dependencies=[Depends(AuthReq.current_user_has_permission)])
    def get_user_bookings(self, user_id: int, booking_type: ActivityRequestType):
        return UserService(self.db).get_user_bookings(user_id=user_id, booking_type=booking_type)
