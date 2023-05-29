from fastapi import APIRouter, Depends
from fastapi_restful.cbv import cbv
from sqlalchemy.orm import Session

from server.api.v1.endpoints.base import register_db_routes
from server.common.models.lot import LotModel
from server.common.schemas.lot import LotOutSchema, LotCreateSchema, LotUpdateSchema
from server.services.lot import LotService
from server.database.config import get_db

router = APIRouter(prefix='/lots', tags=['lots'])

register_db_routes(
    router=router,
    service=LotService,
    model=LotModel,
    create_schema=LotCreateSchema,
    update_schema=LotUpdateSchema,
    out_schema=LotOutSchema
)

@cbv(router)
class LotAPI:
    db: Session = Depends(get_db)

    @router.put('/{lot_id}/assign/{sector_id}', response_model=LotOutSchema)
    def assign_lot_to_sector(self, lot_id: int, sector_id: int):
        return LotService(self.db).update(id=lot_id, obj={'fk_sector_id': sector_id})
