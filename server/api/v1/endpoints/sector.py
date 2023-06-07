from fastapi import APIRouter, Depends, Query
from fastapi_restful.cbv import cbv
from sqlalchemy.orm import Session

from server.api.v1.endpoints.base import register_db_routes, RouteType
from server.common.models.ep_permission import EpPermissionModel
from server.common.schemas.sector import SectorOutSchema, SectorCreateSchema, SectorUpdateSchema
from server.database.config import get_db
from server.services.auth import AuthReq, CurrentUser
from server.services.label import LabelService
from server.services.public_policy import PublicPolicyService
from server.services.sector import SectorService
from server.common.models.sector import SectorModel
from server.services.user import UserService

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
        # Find exclusive sectors the current user has access to
        active_user_labels = UserService(self.db).get_active_user_labels(user_id=current_user.id)
        active_user_ep_permissions: set[EpPermissionModel] = set()
        for label in active_user_labels:
            active_label_ep_permissions = LabelService(self.db).get_active_ep_permissions(label_id=label.id)
            active_user_ep_permissions |= active_label_ep_permissions
        ep_ids = set([ep_permission.fk_ep_id for ep_permission in active_user_ep_permissions])
        exclusive_sectors = set(SectorService(self.db).get_all(filters={'fk_ep_id': ep_ids}))
        # Find public sectors
        pp_ids = set([ppolicy.id for ppolicy in PublicPolicyService(self.db).get_all()])
        public_sectors = set(SectorService(self.db).get_all(filters={'fk_pp_id': pp_ids}))
        return list(public_sectors | exclusive_sectors)

