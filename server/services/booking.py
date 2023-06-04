from datetime import datetime, timedelta
from random import choice

from faker import Faker
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from server.common.models.booking import BookingModel
from server.common.schemas.booking import BookingCreateSchema, BookingUpdateSchema, BookingStatusType
from server.common.utils import IMockDataGenerator
from server.database.booking import BookingDbManager
from server.database.lot import LotDbManager
from server.database.user import UserDbManager
from server.services.dbservice import BaseDbService


class BookingService(BaseDbService[BookingModel, BookingCreateSchema, BookingUpdateSchema], IMockDataGenerator):

    def __init__(self, db: Session):
        self.db = db
        super().__init__(db=db, db_manager=BookingDbManager)

    def generate_mock_data(self, n: int, /) -> list[BookingModel]:
        if n == 0:
            return []
        fake = Faker()
        db_users = UserDbManager(self.db).get_all(limit=n)
        db_lots = LotDbManager(self.db).get_all(limit=5)
        created_bookings = []
        for db_user in db_users:
            db_lot = choice(db_lots)
            b_status = choice([BookingStatusType.Pending, BookingStatusType.Approved, BookingStatusType.Rejected])
            start_time = fake.date_time_between(
                start_date=datetime.now(),
                end_date=datetime.now() + timedelta(days=2))
            end_time = fake.date_time_between(
                start_date=start_time + timedelta(hours=8),
                end_date=start_time + timedelta(days=1))
            booking = BookingCreateSchema(
                status=b_status,
                start_time=start_time,
                end_time=end_time,
                fk_user_id=db_user.id,
                fk_lot_id=db_lot.id
            )
            try:
                created_booking = self.create(obj=booking)
                created_bookings.append(created_booking)
            except IntegrityError:
                self.db.rollback()
                continue
        return created_bookings
