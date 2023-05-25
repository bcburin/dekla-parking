from sqlalchemy.orm import Session

from server.common.models.booking import BookingModel
from server.common.schemas.booking import BookingCreateSchema, BookingUpdateSchema
from server.database.basedbmanager import BaseDbManager


class BookingDbManager(BaseDbManager[BookingModel, BookingCreateSchema, BookingUpdateSchema]):

    def __init__(self, db: Session):
        super().__init__(model=BookingModel, db=db)

