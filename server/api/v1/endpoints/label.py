from fastapi import APIRouter, Depends, Query
from fastapi_restful.cbv import cbv
from sqlalchemy.orm import Session

from server.database.config import get_db
from server.common.schemas.label import LabelOutSchema, LabelCreateSchema, LabelUpdateSchema
from server.services.label import LabelService

router = APIRouter(prefix='/labels', tags=['labels'])


@cbv(router)
class LabelAPI:
    db: Session = Depends(get_db)

    @router.get(path='/', response_model=list[LabelOutSchema])
    def get_all_labels(self, skip: int = Query(default=0, ge=0), limit: int | None = Query(default=100, ge=0)):
        return LabelService(self.db).get_all(skip=skip, limit=limit)

    @router.get(path='/{label_id}', response_model=LabelOutSchema)
    def get_label_by_id(self, label_id: int):
        return LabelService(self.db).get_by_id(id=label_id)

    @router.get(path='/names/{name}', response_model=LabelOutSchema)
    def get_label_by_name(self, name: str):
        return LabelService(self.db).get_by_name(name=name)

    @router.post(path='/', response_model=LabelOutSchema)
    def create_label(self, label: LabelCreateSchema):
        return LabelService(self.db).create(obj=label)

    @router.put(path='/{label_id}', response_model=LabelOutSchema)
    def update_label(self, label_id: int, label: LabelUpdateSchema):
        return LabelService(self.db).update(id=label_id, obj=label)

    @router.delete(path='/{label_id}', response_model=LabelOutSchema)
    def delete_label(self, label_id: int):
        return LabelService(self.db).delete(id=label_id)
