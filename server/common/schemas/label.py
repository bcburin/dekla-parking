from fastapi_restful.api_model import APIModel

from server.common.schemas.base import BaseUpdateSchema, BaseOutSchema


class LabelBaseSchema(APIModel):
    name: str
    description: str
    priority: int


class LabelCreateSchema(LabelBaseSchema):
    pass


class LabelUpdateSchema(LabelBaseSchema, BaseUpdateSchema):
    name: str | None
    description: str | None
    priority: int | None


class LabelOutSchema(LabelBaseSchema, BaseOutSchema):
    id: int

    class Config:
        orm_mode = True
