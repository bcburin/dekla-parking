from fastapi_restful.api_model import APIModel

from server.common.schemas.base import BaseUpdateSchema


class LotBaseSchema(APIModel):
    location: str
    descriptor: str
    occupied: bool = False
    available: bool = True
    fk_sector_id: bool | None = None


class LotCreateSchema(LotBaseSchema):
    pass


class LotUpdateSchema(LotBaseSchema, BaseUpdateSchema):
    location: str | None
    descriptor: str | None
    occupied: bool | None
    available: bool | None


class LotOutSchema(LotBaseSchema):
    id: int

    class Config:
        orm_mode = True
