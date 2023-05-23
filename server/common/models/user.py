from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from server.database.config import Base

if TYPE_CHECKING:
    from server.common.models.label import LabelModel
    from server.common.models.labeling import LabelingModel
    from server.common.models.lot import LotModel


class UserModel(Base):
    __tablename__ = 'user'

    # Fields
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, index=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    password_hash: Mapped[str] = mapped_column()
    is_admin: Mapped[bool] = mapped_column()

    # Relationships
    user_labels: Mapped[list['LabelModel']] = relationship(
        secondary='labeling', back_populates='label_users', viewonly=True)
    user_labelings: Mapped[list['LabelingModel']] = relationship(back_populates='labeled_user', viewonly=True)
    user_lot: Mapped[list['LotModel']] = relationship(
        secondary='booking', back_populates='lot_user', viewonly=True)


