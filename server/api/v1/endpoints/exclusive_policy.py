from fastapi import APIRouter, Depends, Query
from fastapi_restful.cbv import cbv
from sqlalchemy.orm import Session

from server.api.v1.endpoints.base import register_db_routes
from server.common.models.exclusive_policy import ExclusivePolicyModel
from server.database.config import get_db
from server.common.schemas.exclusive_policy import ExclusivePolicyOutSchema, ExclusivePolicyCreateSchema, ExclusivePolicyUpdateSchema
from server.services.exclusive_policy import ExclusivePolicyService

router = APIRouter(prefix='/exclusive_policies', tags=['exclusive_policies'])

register_db_routes(
    router=router,
    service=ExclusivePolicyService,
    model=ExclusivePolicyModel,
    create_schema=ExclusivePolicyCreateSchema,
    update_schema=ExclusivePolicyUpdateSchema,
    out_schema=ExclusivePolicyOutSchema
)


