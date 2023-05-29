from datetime import datetime

from fastapi_restful.api_model import APIModel

from server.common.schemas.base import BaseUpdateSchema, BaseOutSchema
from server.common.schemas.label import LabelOutSchema
from server.common.schemas.user import UserOutSchema


class LabelingBaseSchema(APIModel):
    start_time: datetime | None
    end_time: datetime | None


class LabelingCreateForUserSchema(LabelingBaseSchema):
    fk_label_id: int


class LabelingCreateSchema(LabelingBaseSchema):
    fk_user_id: int
    fk_label_id: int


class LabelingUpdateSchema(LabelingBaseSchema, BaseUpdateSchema):
    pass


class LabelingOutSchema(LabelingBaseSchema, BaseOutSchema):
    id: int
    labeled_user: UserOutSchema
    labeling_label: LabelOutSchema

    class Config:
        orm_mode = True


