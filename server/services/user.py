from random import choice

from faker import Faker
from fastapi.logger import logger
from pydantic import EmailStr
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from server.common.exceptions.labeling import UnauthorizedLabelingRemovalException
from server.common.exceptions.booking import UnauthorizedBookingRemovalException
from server.common.models.booking import BookingModel
from server.common.models.label import LabelModel
from server.common.models.labeling import LabelingModel
from server.common.models.user import UserModel
from server.common.schemas.booking import BookingCreateSchema, BookingCreateForUserSchema
from server.common.schemas.labeling import LabelingCreateSchema, LabelingCreateForUserSchema
from server.common.schemas.base import ActivityRequestType
from server.common.schemas.user import UserCreateSchema, UserUpdateSchema
from server.common.utils import get_is_active, get_is_expired, IMockDataGenerator
from server.database.config import get_db
from server.database.labeling import LabelingDbManager
from server.database.user import UserDbManager
from server.database.booking import BookingDbManager
from server.services.dbservice import BaseDbService


class UserService(BaseDbService[UserModel, UserCreateSchema, UserUpdateSchema], IMockDataGenerator):

    def __init__(self, db: Session):
        self.db: Session = db
        super().__init__(db=db, db_manager=UserDbManager)

    def toggle_is_admin(self, user_id: int) -> UserModel:
        db_user = self.get_by_id(user_id)
        updated_user = self.db_manager.update(db_obj=db_user, obj={'is_admin': not db_user.is_admin})
        return updated_user

    def add_labelings_to_user(self, *, user_id: int, user_labelings: list[LabelingCreateForUserSchema]) -> None:
        labelings = [
            LabelingCreateSchema(**user_labeling.dict(), fk_user_id=user_id) for user_labeling in user_labelings]
        for labeling in labelings:
            LabelingDbManager(self.db).create(obj=labeling)

    def remove_labelings_from_user(self, *, user_id: int, labeling_ids: list[int]) -> None:
        for labeling_id in labeling_ids:
            labeling = LabelingDbManager(self.db).get_by_id(labeling_id)
            if labeling.fk_user_id != user_id:
                raise UnauthorizedLabelingRemovalException(user_id=user_id, labeling_id=labeling_id)
            LabelingDbManager(self.db).remove(pk=labeling_id)

    def get_user_labelings(
            self, *, user_id: int, labeling_type: ActivityRequestType | None = None) -> list[LabelingModel]:
        db_user = self.get_by_id(user_id)
        if not labeling_type or labeling_type == ActivityRequestType.all:
            return db_user.user_labelings
        if labeling_type == ActivityRequestType.active:
            return [labeling for labeling in db_user.user_labelings if get_is_active(obj=labeling)]
        if labeling_type == ActivityRequestType.inactive:
            return [labeling for labeling in db_user.user_labelings if not get_is_active(obj=labeling)]
        if labeling_type == ActivityRequestType.expired:
            return [labeling for labeling in db_user.user_labelings if not get_is_expired(obj=labeling)]
        return db_user.user_labelings

    def get_active_user_labels(self, user_id: int) -> set[LabelModel]:
        active_labelings = self.get_user_labelings(user_id=user_id, labeling_type=ActivityRequestType.active)
        return set([labeling.labeling_label for labeling in active_labelings])

    def add_bookings_to_user(self, *, user_id: int, user_bookings: list[BookingCreateForUserSchema]) -> None:
        bookings = [
            BookingCreateSchema(**user_booking.dict(), fk_user_id=user_id) for user_booking in user_bookings]
        for booking in bookings:
            BookingDbManager(self.db).create(obj=booking)

    def remove_bookings_from_user(self, *, user_id: int, booking_ids: list[int]) -> None:
        for booking_id in booking_ids:
            booking = BookingDbManager(self.db).get_by_id(booking_id)
            if booking.fk_user_id != user_id:
                raise UnauthorizedBookingRemovalException(user_id=user_id, booking_id=booking_id)
            LabelingDbManager(self.db).remove(pk=booking_id)

    def get_user_bookings(
            self, *, user_id: int, booking_type: ActivityRequestType | None = None) -> list[BookingModel]:
        db_user = self.get_by_id(user_id)
        if not booking_type or booking_type == ActivityRequestType.all:
            return db_user.user_bookings
        if booking_type == ActivityRequestType.active:
            return [booking for booking in db_user.user_bookings if get_is_active(obj=booking)]
        if booking_type == ActivityRequestType.inactive:
            return [booking for booking in db_user.user_bookings if not get_is_active(obj=booking)]
        if booking_type == ActivityRequestType.expired:
            return [booking for booking in db_user.user_bookings if not get_is_expired(obj=booking)]
        return db_user.user_bookings

    def generate_mock_data(self, n: int, /) -> list[UserModel]:
        created_users = []
        fake = Faker()
        for _ in range(n):
            first_name: str = fake.first_name()
            last_name: str = fake.last_name()
            username = (first_name[0:2] + last_name[0:4]).lower() + str(choice(range(0, 100)))
            email = EmailStr(username + '@example.com')
            user = UserCreateSchema(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                is_admin=False,
                password='123'
            )
            try:
                created_user = self.create(obj=user)
                created_users.append(created_user)
            except IntegrityError:
                self.db.rollback()
                continue
        return created_users

    @staticmethod
    def task_create_admin_if_none_exists() -> None:
        db = get_db().__next__()
        admins = UserDbManager(db).get_all(filters={'is_admin': True})
        if not admins:
            logger.warning(f'{"WARNING:"}  Creating default admin since none were found. '
                           'Delete it after creating a permanent one.')
            admin = UserCreateSchema(
                username='admin',
                email=EmailStr('admin@example.com'),
                first_name='Service',
                last_name='Admin',
                password='123',
                is_admin=True
            )
            UserDbManager(db).create(obj=admin)
