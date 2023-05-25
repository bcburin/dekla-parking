from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from server.database.config import Base

if TYPE_CHECKING:
    from server.common.models.lot import LotModel
    from server.common.models.user import UserModel


class BookingModel(Base):
    __tablename__ = 'booking'

    # Fields
    id: Mapped[int] = mapped_column(primary_key=True)
    fk_user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    fk_lot_id: Mapped[int] = mapped_column(ForeignKey('lot.id'))
    book_time: Mapped[str] = mapped_column()
    status: Mapped[str] = mapped_column()
    start_time: Mapped[datetime] = mapped_column()
    end_time: Mapped[datetime] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(server_default=func.current_timestamp())
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.current_timestamp(), onupdate=func.current_timestamp)

    # Relationships
    booking_user: Mapped['UserModel'] = relationship(
        back_populates='user_bookings', viewonly=True)
    booking_lot: Mapped['LotModel'] = relationship(back_populates='lot_bookings', viewonly=True)
