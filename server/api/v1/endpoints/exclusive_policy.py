from fastapi import APIRouter, Depends, Query
from fastapi_restful.cbv import cbv
from sqlalchemy.orm import Session

from server.api.v1.endpoints.base import register_db_routes
from server.common.models.exclusive_policy import ExclusivePolicyModel
from server.database.config import get_db
from server.common.schemas.public_policy import ExclusivePolicyOutSchema, ExclusivePolicyCreateSchema, ExclusivePolicyUpdateSchema
from server.services.public_policy import ExclusivePolicyService

router = APIRouter(prefix='/public_policies', tags=['public_policies'])

register_db_routes(
    router=router,
    service=ExclusivePolicyService,
    model=ExclusivePolicyModel,
    create_schema=ExclusivePolicyCreateSchema,
    update_schema=ExclusivePolicyUpdateSchema,
    out_schema=ExclusivePolicyOutSchema
)

@cbv(router)
class ExclusivePolicyAPI:
    db: Session = Depends(get_db)

    @router.get(path='/', response_model=list[ExclusivePolicyOutSchema])
    def get_all_exclusive_policies(self, skip: int = Query(default=0, ge=0), limit: int | None = Query(default=100, ge=0)):
        return ExclusivePolicyService(self.db).get_all(skip=skip, limit=limit)

    @router.get(path='/{ep_id}', response_model=ExclusivePolicyOutSchema)
    def get_exclusive_policy_by_id(self, ep_id: int):
        return ExclusivePolicyService(self.db).get_by_id(id=ep_id)

