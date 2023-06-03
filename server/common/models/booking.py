from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from server.common.models.base import BaseModel, IntervalModel

if TYPE_CHECKING:
    from server.common.models.lot import LotModel
    from server.common.models.user import UserModel


class BookingModel(BaseModel, IntervalModel):
    __tablename__ = 'booking'

    # Fields
    id: Mapped[int] = mapped_column(primary_key=True)
    fk_user_id: Mapped[int] = mapped_column(ForeignKey('user.id', ondelete='SET NULL', onupdate='SET NULL'))
    fk_lot_id: Mapped[int] = mapped_column(ForeignKey('lot.id', ondelete='SET NULL', onupdate='SET NULL'))
    status: Mapped[str] = mapped_column()

    # Relationships
    booking_user: Mapped['UserModel'] = relationship(
        back_populates='user_bookings', viewonly=True)
    booking_lot: Mapped['LotModel'] = relationship(back_populates='lot_bookings', viewonly=True)
