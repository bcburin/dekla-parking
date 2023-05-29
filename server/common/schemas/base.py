from datetime import datetime
from enum import auto

from fastapi_restful.enums import CamelStrEnum
from fastapi_restful.api_model import APIModel


class BaseOutSchema(APIModel):
    created_at: datetime
    updated_at: datetime


class BaseUpdateSchema:

    def has_updates(self):
        return any(value is not None for value in self.__dict__.values() if value is not None)


class ActivityRequestType(CamelStrEnum):
    all = auto()
    active = auto()
    inactive = auto()
    expired = auto()
