from fastapi import APIRouter, Depends
from fastapi_restful.cbv import cbv
from sqlalchemy.orm import Session

from server.api.v1.endpoints.base import register_db_routes
from server.common.models.label import LabelModel
from server.database.config import get_db
from server.common.schemas.label import LabelOutSchema, LabelCreateSchema, LabelUpdateSchema
from server.services.label import LabelService

router = APIRouter(prefix='/labels', tags=['labels'])


register_db_routes(
    router=router,
    service=LabelService,
    model=LabelModel,
    create_schema=LabelCreateSchema,
    update_schema=LabelUpdateSchema,
    out_schema=LabelOutSchema
)


@cbv(router)
class LabelAPI:
    db: Session = Depends(get_db)

    @router.get(path='/names/{name}', response_model=LabelOutSchema)
    def get_label_by_name(self, name: str):
        db_label = LabelService(self.db).get_by_unique_attribute(name, 'name')
        return db_label
