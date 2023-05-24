from pydantic import BaseModel

from server.common.schemas.base import BaseUpdateSchema, BaseOutSchema


class LabelBaseSchema(BaseModel):
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
