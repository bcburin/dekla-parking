from fastapi_restful.api_model import APIModel

from server.common.schemas.base import BaseUpdateSchema, BaseOutSchema
from server.common.schemas.lot import LotOutSchema


class SectorBaseSchema(APIModel):
    name: str
    description: str | None = None
    available: bool = True
    fk_pp_id: int | None = None
    fk_ep_id: int | None = None


class SectorCreateSchema(SectorBaseSchema):
    pass


class SectorUpdateSchema(SectorBaseSchema, BaseUpdateSchema):
    name: str | None
    available: bool | None


class SectorOutSchema(SectorBaseSchema, BaseOutSchema):
    id: int
    sector_lots: list[LotOutSchema]

    class Config:
        orm_mode = True
