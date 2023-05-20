from pydantic import BaseModel


class LabelBaseSchema(BaseModel):
    name: str
    description: str
    priority: int


class LabelCreateSchema(LabelBaseSchema):
    pass


class LabelUpdateSchema(LabelBaseSchema):
    name: str | None
    description: str | None
    priority: int | None

    def has_updates(self):
        return any(value is not None for value in self.__dict__.values() if value is not None)


class LabelOutSchema(LabelBaseSchema):
    id: int

    class Config:
        orm_mode = True
