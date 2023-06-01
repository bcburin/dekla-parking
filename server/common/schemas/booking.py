from datetime import datetime

from fastapi_restful.api_model import APIModel

from server.common.schemas.base import BaseUpdateSchema, BaseOutSchema
from server.common.schemas.user import UserOutSchema
from server.common.schemas.lot import LotOutSchema


class BookingBaseSchema(APIModel):
    status: str
    start_time: datetime
    end_time: datetime


class BookingCreateSchema(BookingBaseSchema):
    fk_user_id: int
    fk_lot_id: int


class BookingCreateForUserSchema(BookingBaseSchema):
    fk_lot_id: int


class BookingUpdateSchema(BookingBaseSchema, BaseUpdateSchema):
    status: str | None
    start_time: datetime | None
    end_time: datetime | None


class BookingOutSchema(BookingBaseSchema, BaseOutSchema):
    id: int
    booking_lot: LotOutSchema
    booking_user: UserOutSchema

    class Config:
        orm_mode = True
