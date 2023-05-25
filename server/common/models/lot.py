from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from server.common.models.base import BaseModel

if TYPE_CHECKING:
    from server.common.models.booking import BookingModel
    from server.common.models.user import UserModel
    from server.common.models.sector import SectorModel


class LotModel(BaseModel):
    __tablename__ = 'lot'

    # Fields
    id: Mapped[int] = mapped_column(primary_key=True)
    location: Mapped[str] = mapped_column()
    descriptor: Mapped[str] = mapped_column()
    occupied: Mapped[bool] = mapped_column()
    available: Mapped[bool] = mapped_column()
    fk_sector_id: Mapped[int] = mapped_column(ForeignKey('sector.id'))

    # Relationships
    lot_users: Mapped[list['UserModel']] = relationship(
        secondary='booking',
        back_populates='user_lots',
        viewonly=True
    )
    lot_bookings: Mapped[list['BookingModel']] = relationship(
        back_populates='booking_lot',
        viewonly=True
    )
    lot_sector: Mapped['SectorModel'] = relationship(
        back_populates='sector_lots',
        viewonly=True
    )
