from pydantic import BaseModel

from server.common.utils.classes import NonNullAttributeVerifier


class LabelBaseSchema(BaseModel):
    name: str
    description: str
    priority: int


class LabelCreateSchema(LabelBaseSchema):
    pass


class LabelUpdateSchema(LabelBaseSchema, NonNullAttributeVerifier):
    name: str | None
    description: str | None
    priority: int | None


class LabelOutSchema(LabelBaseSchema):
    id: int

    class Config:
        orm_mode = True
