from fastapi import APIRouter, Depends
from fastapi_restful.cbv import cbv
from sqlalchemy.orm import Session

from server.api.v1.endpoints.base import register_db_routes
from server.common.models.booking import BookingModel
from server.common.schemas.booking import BookingOutSchema, BookingUpdateSchema, BookingCreateSchema
from server.database.config import get_db
from server.services.booking import BookingService

router = APIRouter(prefix='/bookings', tags=['bookings'])

register_db_routes(
    router=router,
    service=BookingService,
    model=BookingModel,
    create_schema=BookingCreateSchema,
    update_schema=BookingUpdateSchema,
    out_schema=BookingOutSchema
)


@cbv(router)
class BookingAPI:
    db: Session = Depends(get_db)

    @router.put('/{booking_id}/approve', response_model=BookingOutSchema)
    def approve_booking(self, booking_id: int):
        updates = BookingUpdateSchema(status='Approved')
        return BookingService(self.db).update(id=booking_id, obj=updates)

    @router.put('/{booking_id}/reject', response_model=BookingOutSchema)
    def approve_booking(self, booking_id: int):
        updates = BookingUpdateSchema(status='Rejected')
        return BookingService(self.db).update(id=booking_id, obj=updates)

