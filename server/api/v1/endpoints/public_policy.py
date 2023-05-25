from fastapi import APIRouter, Depends, Query
from fastapi_restful.cbv import cbv
from sqlalchemy.orm import Session

from server.database.config import get_db
from server.common.schemas.public_policy import PublicPolicyOutSchema, PublicPolicyCreateSchema, PublicPolicyUpdateSchema
from server.services.public_policy import PublicPolicyService

router = APIRouter(prefix='/public_policies', tags=['public_policies'])


@cbv(router)
class PublicPolicyAPI:
    db: Session = Depends(get_db)

    @router.get(path='/', response_model=list[PublicPolicyOutSchema])
    def get_all_public_policies(self, skip: int = Query(default=0, ge=0), limit: int | None = Query(default=100, ge=0)):
        return PublicPolicyService(self.db).get_all(skip=skip, limit=limit)

    @router.get(path='/{pp_id}', response_model=PublicPolicyOutSchema)
    def get_public_policy_by_id(self, pp_id: int):
        return PublicPolicyService(self.db).get_by_id(id=pp_id)

    @router.post(path='/', response_model=PublicPolicyOutSchema)
    def create_public_policy(self, public_policy: PublicPolicyCreateSchema):
        return PublicPolicyService(self.db).create(obj=public_policy)

    @router.put(path='/{pp_id}', response_model=PublicPolicyOutSchema)
    def update_public_policy(self, pp_id: int, public_policy: PublicPolicyUpdateSchema):
        return PublicPolicyService(self.db).update(id=pp_id, obj=public_policy)

    @router.delete(path='/{pp_id}', response_model=PublicPolicyOutSchema)
    def delete_public_policy(self, pp_id: int):
        return PublicPolicyService(self.db).delete(id=pp_id)
