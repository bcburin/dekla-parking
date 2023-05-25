from fastapi import APIRouter

from server.api.v1.endpoints.base import register_db_routes
from server.common.models.lot import LotModel
from server.common.schemas.lot import LotOutSchema, LotCreateSchema, LotUpdateSchema
from server.services.lot import LotService

router = APIRouter(prefix='/lots', tags=['lots'])

register_db_routes(
    router=router,
    service=LotService,
    model=LotModel,
    create_schema=LotCreateSchema,
    update_schema=LotUpdateSchema,
    out_schema=LotOutSchema
)