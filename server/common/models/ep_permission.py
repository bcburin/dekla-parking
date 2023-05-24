from server.database.config import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import func
from sqlalchemy import ForeignKey
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship


if TYPE_CHECKING:
    from server.common.models.exclusive_policy import ExclusivePolicyModel
    from server.common.models.label import LabelModel


class EpPermissionModel(Base):
    __tablename__ = 'ep_permission'

    # Fields
    fk_ep_id: Mapped[int] = mapped_column(ForeignKey('exclusive_policy.id'))
    fk_label_id: Mapped[int] = mapped_column(ForeignKey('label.id'))
    start_time: Mapped[datetime] = mapped_column()
    end_time: Mapped[datetime] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.current_timestamp())
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.current_timestamp(), onupdate=func.current_timestamp)

    # Relationships
    #ep_permission_excluive_policy: Mapped['ExclusivePolicyModel'] = relationship(back_populates='exclusive_policy_ep_permissions', viewonly=True)
    #ep_permission_label: Mapped['LabelModel'] = relationship(back_populates='label_ep_permissions', viewonly=True)
