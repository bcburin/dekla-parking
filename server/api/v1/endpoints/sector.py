from fastapi import APIRouter, Depends, Query
from fastapi_restful.cbv import cbv
from sqlalchemy.orm import Session

from server.database.config import get_db
from server.common.schemas.public_policy import SectorOutSchema, SectorCreateSchema, SectorUpdateSchema
from server.services.public_policy import SectorService

router = APIRouter(prefix='/public_policies', tags=['public_policies'])


@cbv(router)
class ExclusivePolicyAPI:
    db: Session = Depends(get_db)

    @router.get(path='/', response_model=list[SectorOutSchema])
    def get_all_exclusive_policies(self, skip: int = Query(default=0, ge=0), limit: int | None = Query(default=100, ge=0)):
        return SectorService(self.db).get_all(skip=skip, limit=limit)

    @router.get(path='/{sector_id}', response_model=SectorOutSchema)
    def get_exclusive_policy_by_id(self, sector_id: int):
        return SectorService(self.db).get_by_id(id=sector_id)

    @router.get(path='/names/{name}', response_model=SectorOutSchema)
    def public_policy(self, name: str):
        return SectorService(self.db).get_by_unique_attribute(name, 'name')

    @router.post(path='/', response_model=SectorOutSchema)
    def create_public_policy(self, sector: SectorCreateSchema):
        return SectorService(self.db).create(obj=sector)

    @router.put(path='/{sector_id}', response_model=SectorOutSchema)
    def update_public_policy(self, sector_id: int, sector: SectorUpdateSchema):
        return SectorService(self.db).update(id=sector_id, obj=sector)

    @router.delete(path='/{sector_id}', response_model=SectorOutSchema)
    def delete_public_policy(self, sector_id: int):
        return SectorService(self.db).delete(id=sector_id)