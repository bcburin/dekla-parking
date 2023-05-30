from fastapi import APIRouter

from server.api.v1.endpoints.base import register_db_routes
from server.common.models.labeling import LabelingModel
from server.common.schemas.labeling import LabelingOutSchema, LabelingUpdateSchema, LabelingCreateSchema
from server.services.labeling import LabelingService

router = APIRouter(prefix='/labelings', tags=['labelings'])

register_db_routes(
    router=router,
    service=LabelingService,
    model=LabelingModel,
    create_schema=LabelingCreateSchema,
    update_schema=LabelingUpdateSchema,
    out_schema=LabelingOutSchema
)
