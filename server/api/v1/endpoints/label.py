from fastapi import APIRouter, Depends
from fastapi_restful.cbv import cbv
from sqlalchemy.orm import Session

from server.api.v1.endpoints.base import register_db_routes
from server.common.models.label import LabelModel
from server.common.schemas.base import IntervalSchema
from server.common.schemas.labeling import LabelingOutSchema
from server.database.config import get_db
from server.common.schemas.label import LabelOutSchema, LabelCreateSchema, LabelUpdateSchema
from server.services.auth import AuthReq
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

    @router.post(path='/{label_id}/assign-to/{user_id}', response_model=LabelingOutSchema, dependencies=[Depends(AuthReq.current_user_has_permission)])
    def assign_label_to_user(self, label_id: int, user_id: int, labeling_times: IntervalSchema | None = None):
        return LabelService(self.db).assign_label_to_user(
            label_id=label_id,
            user_id=user_id,
            labeling_times=labeling_times
        )
