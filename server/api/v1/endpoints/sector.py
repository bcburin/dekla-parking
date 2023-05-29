from fastapi import APIRouter, Depends, Query
from fastapi_restful.cbv import cbv
from sqlalchemy.orm import Session

from server.api.v1.endpoints.base import register_db_routes, RouteType
from server.database.config import get_db
from server.common.schemas.sector import SectorOutSchema, SectorCreateSchema, SectorUpdateSchema
from server.services.sector import SectorService
from server.common.models.sector import SectorModel

router = APIRouter(prefix='/sector', tags=['sector'])

register_db_routes(
    router=router,
    service=SectorService,
    model=SectorModel,
    create_schema=SectorCreateSchema,
    update_schema=SectorUpdateSchema,
    out_schema=SectorOutSchema,
    omit=[RouteType.get_by_id, RouteType.update, RouteType.delete],
)

@cbv(router)
class LabelAPI:
    db: Session = Depends(get_db)