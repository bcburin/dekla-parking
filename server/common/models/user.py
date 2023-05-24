from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from server.database.config import Base

if TYPE_CHECKING:
    from server.common.models.label import LabelModel
    from server.common.models.labeling import LabelingModel
    from server.common.models.lot import LotModel
    from server.common.models.booking import BookingModel


class UserModel(Base):
    __tablename__ = 'user'

    # Fields
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, index=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    first_name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column()
    password_hash: Mapped[str] = mapped_column()
    is_admin: Mapped[bool] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(server_default=func.current_timestamp())
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.current_timestamp(), onupdate=func.current_timestamp)

    # Relationships
    user_labels: Mapped[list['LabelModel']] = relationship(
        secondary='labeling', back_populates='label_users', viewonly=True)
    user_labelings: Mapped[list['LabelingModel']] = relationship(back_populates='labeled_user', viewonly=True)
    #user_lots: Mapped[list['LotModel']] = relationship(
        #secondary='booking', back_populates='lot_users', viewonly=True)
    #user_bookings: Mapped[list['BookingModel']] = relationship(back_populates='booking_user', viewonly=True)

