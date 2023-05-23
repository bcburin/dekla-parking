from fastapi import APIRouter, Depends, Query
from fastapi_restful.cbv import cbv
from sqlalchemy.orm import Session

from server.database.config import get_db
from server.common.schemas.lot import LotOutSchema, LotCreateSchema, LotUpdateSchema
from server.services.lot import LotService

router = APIRouter(prefix='/lots', tags=['lots'])


@cbv(router)
class LotAPI:
    db: Session = Depends(get_db)

    @router.get(path='/', response_model=list[LotOutSchema])
    def get_all_lots(self, skip: int = Query(default=0, ge=0), limit: int | None = Query(default=100, ge=0)):
        return LotService(self.db).get_all(skip=skip, limit=limit)

    @router.get(path='/{lot_id}', response_model=LotOutSchema)
    def get_lot_by_id(self, lot_id: int):
        return LotService(self.db).get_by_id(id=lot_id)

    @router.get(path='/names/{name}', response_model=LotOutSchema)
    def lot(self, name: str):
        return LotService(self.db).get_by_unique_attribute(name, 'name')

    @router.post(path='/', response_model=LotOutSchema)
    def create_lot(self, label: LotCreateSchema):
        return LotService(self.db).create(obj=label)

    @router.put(path='/{label_id}', response_model=LotOutSchema)
    def update_label(self, label_id: int, label: LotUpdateSchema):
        return LotService(self.db).update(id=label_id, obj=label)

    @router.delete(path='/{label_id}', response_model=LotOutSchema)
    def delete_label(self, label_id: int):
        return LotService(self.db).delete(id=label_id)
