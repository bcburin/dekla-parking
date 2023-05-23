from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from server.database.config import Base
from datetime import datetime

if TYPE_CHECKING:
    from server.common.models.exclusive_policy import ExclusivePolicyModel
    from server.common.models.label import LabelModel


class EpPermissionModel(Base):
    __tablename__ = 'ep_permission'

    # Fields
    fk_ep_id: Mapped[int] = mapped_column()
    fk_label_id: Mapped[int] = mapped_column()
    start_time: Mapped[datetime] = mapped_column()
    end_time: Mapped[datetime] = mapped_column()

    # Relationships
    ep_permission_excluive_policy: Mapped['ExclusivePolicyModel'] = relationship(back_populates='exclusive_policy_ep_permission', viewonly=True)
    ep_permision_label: Mapped['LabelModel'] = relationship(back_populates='ep_permission_exclusive_policy', viewonly=True)