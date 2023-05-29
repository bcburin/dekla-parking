from fastapi_restful.api_model import APIModel

from server.common.schemas.base import BaseUpdateSchema


class SectorBaseSchema(APIModel):
    name: str
    available: bool = True


class SectorCreateSchema(SectorBaseSchema):
    pass


class SectorUpdateSchema(SectorBaseSchema, BaseUpdateSchema):
    name: str | None
    available: bool | None
    fk_pp_id: int
    fk_ep_id: int

class SectorOutSchema(SectorBaseSchema):
    id: int

    class Config:
        orm_mode = True
