from fastapi_restful.api_model import APIModel

from server.common.schemas.base import BaseUpdateSchema


class ExclusivePolicyBaseSchema(APIModel):
    name: str
    descriptor: str
    price: float


class ExclusivePolicyCreateSchema(ExclusivePolicyBaseSchema):
    pass


class ExclusivePolicyUpdateSchema(ExclusivePolicyBaseSchema, BaseUpdateSchema):
    name: str | None
    descriptor: str | None
    price: float | None


class ExclusivePolicyOutSchema(ExclusivePolicyBaseSchema):
    id: int

    class Config:
        orm_mode = True
