from datetime import datetime

from server.common.schemas.base import BaseUpdateSchema, BaseOutSchema, IntervalSchema
from server.common.schemas.label import LabelOutSchema
from server.common.schemas.exclusive_policy import ExclusivePolicyOutSchema


class EpPermissionBaseSchema(IntervalSchema):
    pass


class EpPermissionCreateSchema(EpPermissionBaseSchema):
    fk_ep_id: int
    fk_label_id: int


class EpPermissionUpdateSchema(EpPermissionBaseSchema, BaseUpdateSchema):
    start_time: datetime | None
    end_time: datetime | None


class EpPermissionOutSchema(EpPermissionBaseSchema, BaseOutSchema):
    id: int
    ep_permission_label: LabelOutSchema
    ep_permission_exclusive_policy: ExclusivePolicyOutSchema

    class Config:
        orm_mode = True
