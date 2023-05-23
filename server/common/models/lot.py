from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from server.database.config import Base

if TYPE_CHECKING:
    from server.common.models.booking import BookingModel
    from server.common.models.user import UserModel
    from server.common.models.sector import SectorModel


class LotModel(Base):
    __tablename__ = 'lot'

    # Fields
    id: Mapped[int] = mapped_column(primary_key=True)
    location: Mapped[str] = mapped_column()
    descriptor: Mapped[str] = mapped_column()
    occupied: Mapped[str] = mapped_column()
    available: Mapped[str] = mapped_column()
    fk_Sector_id: Mapped[int] = mapped_column(unique=True)

    # Relationships
    lot_users: Mapped[list['UserModel']] = relationship(
        secondary='booking', back_populates='user_lot', viewonly=True)
    lot_booking: Mapped[list['BookingModel']] = relationship(back_populates='booking_lot', viewonly=True)
    lot_sector: Mapped['SectorModel'] = relationship(back_populates='sector_lot',viewonly=True)

