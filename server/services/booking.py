from sqlalchemy.orm import Session

from server.common.models.booking import BookingModel
from server.common.schemas.booking import BookingCreateSchema, BookingUpdateSchema
from server.database.booking import BookingDbManager
from server.services.dbservice import BaseDbService


class BookingService(BaseDbService[BookingModel, BookingCreateSchema, BookingUpdateSchema]):

    def __init__(self, db: Session):
        self.db = db
        super().__init__(db=db, db_manager=BookingDbManager)
