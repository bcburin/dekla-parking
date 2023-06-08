from datetime import datetime
from enum import auto

from fastapi_restful.enums import CamelStrEnum
from fastapi_restful.api_model import APIModel
from pydantic import validator


class BaseOutSchema(APIModel):
    created_at: datetime
    updated_at: datetime


class IntervalSchema(APIModel):
    start_time: datetime | None = None
    end_time: datetime | None = None

    @validator('end_time')
    def end_time_greater_than_start_time(cls, end_time, values):
        if end_time is None:
            return end_time
        if 'start_time' in values and values['start_time'] is not None and end_time <= values['start_time']:
            raise ValueError("End time must be greater than the start time")
        return end_time


class BaseUpdateSchema:

    def has_updates(self):
        return any(value is not None for value in self.__dict__.values() if value is not None)


class ActivityRequestType(CamelStrEnum):
    all = auto()
    active = auto()
    inactive = auto()
    expired = auto()
