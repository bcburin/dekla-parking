from fastapi import APIRouter, Depends, Query
from fastapi_restful.cbv import cbv
from sqlalchemy.orm import Session

from server.api.v1.endpoints.base import register_db_routes, RouteType
from server.common.schemas.sector import SectorOutSchema, SectorCreateSchema, SectorUpdateSchema
from server.database.config import get_db
from server.services.auth import AuthReq, CurrentUser
from server.services.sector import SectorService
from server.common.models.sector import SectorModel

router = APIRouter(prefix='/sectors', tags=['sectors'])

register_db_routes(
    router=router,
    service=SectorService,
    model=SectorModel,
    create_schema=SectorCreateSchema,
    update_schema=SectorUpdateSchema,
    out_schema=SectorOutSchema,
    omit=[RouteType.get_all]
)


@cbv(router)
class SectorAPI:
    db: Session = Depends(get_db)

    @router.get(
        '/',
        response_model=list[SectorOutSchema],
        dependencies=[Depends(AuthReq.current_user_is_authenticated)])
    def get_all_sectors(
            self,
            current_user: CurrentUser,
            skip: int = Query(default=0, ge=0),
            limit: int | None = Query(default=100, ge=0),
    ):
        if current_user.is_admin:
            return SectorService(self.db).get_all(skip=skip, limit=limit)
        return SectorService(self.db).get_sectors_user_has_permission(user=current_user)

    @router.put(
        '/{sector_id}/assign-public-policy/{policy_id}',
        response_model=SectorOutSchema,
        dependencies=[Depends(AuthReq.current_user_has_permission)])
    def assign_public_policy_to_sector(self, sector_id: int, policy_id: int):
        return SectorService(self.db).assign_policy_to_sector(
            sector_id=sector_id, policy_id=policy_id, exclusive=False)

    @router.put(
        '/{sector_id}/assign-exclusive-policy/{policy_id}',
        response_model=SectorOutSchema,
        dependencies=[Depends(AuthReq.current_user_has_permission)])
    def assign_exclusive_policy_to_sector(self, sector_id: int, policy_id: int):
        return SectorService(self.db).assign_policy_to_sector(sector_id=sector_id, policy_id=policy_id, exclusive=True)
