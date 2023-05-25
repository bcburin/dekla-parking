from fastapi import APIRouter, Depends, HTTPException
from fastapi_restful.cbv import cbv
from sqlalchemy.orm import Session

from server.api.v1.endpoints.base import register_db_routes
from server.common.models.lot import LotModel
from server.common.schemas.lot import LotOutSchema, LotCreateSchema, LotUpdateSchema
from server.common.schemas.booking import BookingCreateforLotSchema, BookingOutSchema
from server.common.schemas.base import ActivityRequestType
from server.services.lot import LotService
from server.database.config import get_db

router = APIRouter(prefix='/lots', tags=['lots'])

register_db_routes(
    router=router,
    service=LotService,
    model=LotModel,
    create_schema=LotCreateSchema,
    update_schema=LotUpdateSchema,
    out_schema=LotOutSchema
)


