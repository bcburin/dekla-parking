from datetime import datetime

from fastapi_restful.api_model import APIModel


class BaseOutSchema(APIModel):
    created_at: datetime
    updated_at: datetime


class BaseUpdateSchema:

    def has_updates(self):
        return any(value is not None for value in self.__dict__.values() if value is not None)
