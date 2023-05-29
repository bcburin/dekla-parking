from pydantic import BaseModel

from server.common.schemas.base import BaseUpdateSchema


class PublicPolicyBaseSchema(BaseModel):
    name: str
    descriptor: str
    price: float


class PublicPolicyCreateSchema(PublicPolicyBaseSchema):
    pass


class PublicPolicyUpdateSchema(PublicPolicyBaseSchema, BaseUpdateSchema):
    name: str | None
    descriptor: str | None
    price: float | None


class PublicPolicyOutSchema(PublicPolicyBaseSchema):
    id: int

    class Config:
        orm_mode = True
