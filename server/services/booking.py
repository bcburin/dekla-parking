from datetime import datetime, timedelta
from random import choice

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from server.common.models.booking import BookingModel
from server.common.schemas.booking import BookingCreateSchema, BookingUpdateSchema
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
        db_users = UserDbManager(self.db).get_all(limit=n)
        db_lots = LotDbManager(self.db).get_all(limit=5)
        created_bookings = []
        for db_user in db_users:
            db_lot = choice(db_lots)
            booking = BookingCreateSchema(
                book_time=datetime.now(),
                status='Pending',
                start_time=datetime.now(),
                end_time=datetime.now() + timedelta(days=1),
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
