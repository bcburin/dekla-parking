from datetime import datetime

from server.common.schemas.base import BaseUpdateSchema, BaseOutSchema, IntervalSchema
from server.common.schemas.label import LabelOutSchema
from server.common.schemas.user import UserOutSchema


class LabelingBaseSchema(IntervalSchema):
    pass


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
