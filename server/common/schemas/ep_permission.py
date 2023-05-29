from datetime import datetime

from fastapi_restful.api_model import APIModel

from server.common.schemas.base import BaseUpdateSchema, BaseOutSchema
from server.common.schemas.label import LabelOutSchema
from server.common.schemas.exclusive_policy import ExclusivePolicyOutSchema

class EpPermissionBaseSchema(APIModel):
    start_time: datetime
    end_time: datetime


class EpPermissionCreateSchema(EpPermissionBaseSchema):
    fk_ep_id: int
    fk_label_id: int


class EpPermissionUpdateSchema(EpPermissionBaseSchema, BaseUpdateSchema):
    start_time: datetime | None
    end_time: datetime | None


class EpPermissionOutSchema(EpPermissionBaseSchema, BaseOutSchema):
    ep_permission_label = LabelOutSchema
    ep_permission_ep = ExclusivePolicyOutSchema
    class Config:
        orm_mode = True
