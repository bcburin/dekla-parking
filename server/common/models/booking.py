from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from server.database.config import Base

if TYPE_CHECKING:
    from server.common.models.lot import LotModel
    from server.common.models.user import UserModel


class BookingModel(Base):
    __tablename__ = 'booking'

    # Fields
    id: Mapped[int] = mapped_column(primary_key=True)
    fk_User_id: Mapped[int] = mapped_column(unique=True)
    fk_Lot_id: Mapped[int] = mapped_column(unique=True)
    book_time: Mapped[str] = mapped_column()
    status: Mapped[str] = mapped_column()
    start_time: Mapped[str] = mapped_column()
    end_time: Mapped[str] = mapped_column()

    # Relationships
    booking_users: Mapped['UserModel'] = relationship(
        back_populates='user_booking', viewonly=True)
    booking_lot: Mapped['LotModel'] = relationship(back_populates='lot_booking', viewonly=True)
