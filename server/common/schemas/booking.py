from datetime import datetime

from pydantic import BaseModel


class BookingBaseSchema(BaseModel):
    book_time: datetime
    status: str
    start_time: datetime
    end_time: datetime


class BookingCreateSchema(BookingBaseSchema):
    fk_user_id: int
    fk_lot_id: int


class BookingUpdateSchema(BookingBaseSchema):
    book_time: datetime | None
    status: str | None
    start_time: datetime | None
    end_time: datetime | None


class BookingOutSchema(BookingBaseSchema):
    id: int

    class Config:
        orm_mode = True
