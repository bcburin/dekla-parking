from fastapi import APIRouter

from server.api.v1.endpoints.base import register_db_routes
from server.common.schemas.public_policy import (
    PublicPolicyOutSchema, PublicPolicyCreateSchema, PublicPolicyUpdateSchema)
from server.services.public_policy import PublicPolicyService
from server.common.models.public_policy import PublicPolicyModel

router = APIRouter(prefix='/public_policies', tags=['public policies'])

register_db_routes(
    router=router,
    service=PublicPolicyService,
    model=PublicPolicyModel,
    create_schema=PublicPolicyCreateSchema,
    update_schema=PublicPolicyUpdateSchema,
    out_schema=PublicPolicyOutSchema
)


