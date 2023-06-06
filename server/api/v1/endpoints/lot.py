from fastapi import APIRouter, Depends, Query
from fastapi_restful.cbv import cbv
from sqlalchemy.orm import Session

from server.api.v1.endpoints.base import register_db_routes, RouteType
from server.common.models.lot import LotModel
from server.common.schemas.booking import BookingOutSchema, BookingCreateSchema, BookingStatusType, \
    BookingCreateForUserAndLotSchema
from server.common.schemas.lot import LotOutSchema, LotCreateSchema, LotUpdateSchema
from server.services.auth import AuthReq, CurrentUser
from server.services.booking import BookingService
from server.services.lot import LotService
from server.database.config import get_db

router = APIRouter(prefix='/lots', tags=['lots'])

register_db_routes(
    router=router,
    service=LotService,
    model=LotModel,
    create_schema=LotCreateSchema,
    update_schema=LotUpdateSchema,
    out_schema=LotOutSchema,
    omit=[RouteType.get_all]
)


@cbv(router)
class LotAPI:
    db: Session = Depends(get_db)

    @router.get(
        '/',
        response_model=list[LotOutSchema],
        dependencies=[Depends(AuthReq.current_user_has_permission)])
    def get_all_lots(
            self,
            skip: int = Query(default=0, ge=0),
            limit: int | None = Query(default=100, ge=0),
            unassigned: bool = False
    ):
        return LotService(self.db).get_all(
            skip=skip,
            limit=limit,
            filters={'fk_sector_id': None} if unassigned else None)

    @router.put(
        '/{lot_id}/assign/{sector_id}',
        response_model=LotOutSchema,
        dependencies=[Depends(AuthReq.current_user_has_permission)]
    )
    def assign_lot_to_sector(self, lot_id: int, sector_id: int):
        return LotService(self.db).assign_lot_to_sector(lot_id=lot_id, sector_id=sector_id)

    @router.put(
        '/{lot_id}/toggle-occupied',
        response_model=LotOutSchema,
        dependencies=[Depends(AuthReq.current_user_has_permission)]
    )
    def toggle_lot_occupied(self, lot_id: int):
        return LotService(self.db).toggle_occupied(lot_id)

    @router.put(
        '/{lot_id}/toggle-available',
        response_model=LotOutSchema,
        dependencies=[Depends(AuthReq.current_user_has_permission)]
    )
    def toggle_lot_available(self, lot_id: int):
        return LotService(self.db).toggle_available(lot_id)

    @router.post(
        '/{lot_id}/book-for-me',
        response_model=BookingOutSchema,
        dependencies=[Depends(AuthReq.current_user_is_authenticated)])
    def book_lot_for_me(self, lot_id, current_user: CurrentUser, booking_times: BookingCreateForUserAndLotSchema):
        booking = BookingCreateSchema(
            status=BookingStatusType.Pending if not current_user.is_admin else BookingStatusType.Approved,
            start_time=booking_times.start_time,
            end_time=booking_times.end_time,
            fk_user_id=current_user.id,
            fk_lot_id=lot_id
        )
        return BookingService(self.db).create(obj=booking)

    @router.post(
        '/{lot_id}/book-for-user/{user_id}',
        response_model=BookingOutSchema,
        dependencies=[Depends(AuthReq.current_user_has_permission)])
    def book_lot_for_user(
            self,
            lot_id: int,
            user_id: int,
            booking_times: BookingCreateForUserAndLotSchema,
            status: BookingStatusType = Query(default=BookingStatusType.Approved)
    ):
        booking = BookingCreateSchema(
            status=status,
            start_time=booking_times.start_time,
            end_time=booking_times.end_time,
            fk_user_id=user_id,
            fk_lot_id=lot_id
        )
        return BookingService(self.db).create(obj=booking)
