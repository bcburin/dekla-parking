from datetime import datetime
from enum import auto

from fastapi_restful.api_model import APIModel
from fastapi_restful.enums import CamelStrEnum

from server.common.schemas.base import BaseUpdateSchema, BaseOutSchema, IntervalSchema
from server.common.schemas.user import UserOutSchema
from server.common.schemas.lot import LotOutSchema


class BookingStatusType(CamelStrEnum):
    Pending = auto()
    Approved = auto()
    Rejected = auto()


class BookingBaseSchema(IntervalSchema):
    status: BookingStatusType = BookingStatusType.Pending
    start_time: datetime
    end_time: datetime

    class Config:
        use_enum_values = True


class BookingCreateSchema(BookingBaseSchema):
    fk_user_id: int
    fk_lot_id: int


class BookingCreateForUserSchema(BookingBaseSchema):
    fk_lot_id: int


class BookingCreateForUserAndLotSchema(APIModel):
    start_time: datetime
    end_time: datetime


class BookingUpdateSchema(BookingBaseSchema, BaseUpdateSchema):
    status: BookingStatusType | None
    start_time: datetime | None
    end_time: datetime | None


class BookingOutSchema(BookingBaseSchema, BaseOutSchema):
    id: int
    booking_lot: LotOutSchema
    booking_user: UserOutSchema

    class Config:
        orm_mode = True
