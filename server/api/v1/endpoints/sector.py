from fastapi import APIRouter

from server.api.v1.endpoints.base import register_db_routes
from server.common.schemas.sector import SectorOutSchema, SectorCreateSchema, SectorUpdateSchema
from server.services.sector import SectorService
from server.common.models.sector import SectorModel

router = APIRouter(prefix='/sectors', tags=['sectors'])

register_db_routes(
    router=router,
    service=SectorService,
    model=SectorModel,
    create_schema=SectorCreateSchema,
    update_schema=SectorUpdateSchema,
    out_schema=SectorOutSchema
)
