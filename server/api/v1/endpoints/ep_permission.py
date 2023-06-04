from fastapi import APIRouter

from server.api.v1.endpoints.base import register_db_routes
from server.common.models.ep_permission import EpPermissionModel
from server.common.schemas.ep_permission import EpPermissionCreateSchema, EpPermissionUpdateSchema, \
    EpPermissionOutSchema
from server.services.ep_permission import EpPermissionService

router = APIRouter(prefix='/epPermissions', tags=['exclusive policy permissions'])


register_db_routes(
    router=router,
    model=EpPermissionModel,
    service=EpPermissionService,
    create_schema=EpPermissionCreateSchema,
    update_schema=EpPermissionUpdateSchema,
    out_schema=EpPermissionOutSchema
)
