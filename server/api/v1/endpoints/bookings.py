from fastapi import APIRouter, Depends, Query
from fastapi_restful.cbv import cbv
from sqlalchemy.orm import Session

from server.api.v1.endpoints.base import register_db_routes, RouteType
from server.common.models.booking import BookingModel
from server.common.schemas.booking import BookingOutSchema, BookingUpdateSchema, BookingCreateSchema, BookingStatusType
from server.database.config import get_db
from server.services.auth import AuthReq, CurrentUser
from server.services.booking import BookingService

router = APIRouter(prefix='/bookings', tags=['bookings'])

register_db_routes(
    router=router,
    service=BookingService,
    model=BookingModel,
    create_schema=BookingCreateSchema,
    update_schema=BookingUpdateSchema,
    out_schema=BookingOutSchema,
    omit=[RouteType.get_all, RouteType.update]
)


@cbv(router)
class BookingAPI:
    db: Session = Depends(get_db)

    @router.get(
        '/',
        response_model=list[BookingOutSchema],
        dependencies=[Depends(AuthReq.current_user_is_authenticated)])
    def get_all_bookings(
            self,
            current_user: CurrentUser,
            skip: int = Query(default=0, ge=0),
            limit: int | None = Query(default=100, ge=0)
    ):
        filters = None
        if not current_user.is_admin:
            filters = {'fk_user_id': current_user.id}
        return BookingService(self.db).get_all(skip=skip, limit=limit, filters=filters)

    @router.put('/{booking_id}/approve', response_model=BookingOutSchema)
    def approve_booking(self, booking_id: int):
        updates = BookingUpdateSchema(status=BookingStatusType.Approved)
        return BookingService(self.db).update(id=booking_id, obj=updates)

    @router.put('/{booking_id}/reject', response_model=BookingOutSchema)
    def approve_booking(self, booking_id: int):
        updates = BookingUpdateSchema(status=BookingStatusType.Rejected)
        return BookingService(self.db).update(id=booking_id, obj=updates)

