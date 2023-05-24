from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from server.database.config import Base

if TYPE_CHECKING:
    from server.common.models.sector import SectorModel
    from server.common.models.ep_permission import EpPermissionModel
    from server.common.models.label import LabelModel


class ExclusivePolicyModel(Base):
    __tablename__ = 'exclusive_policy'

    # Fields
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    descriptor: Mapped[str] = mapped_column()
    price: Mapped[float] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(server_default=func.current_timestamp())
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.current_timestamp(), onupdate=func.current_timestamp)

    # Relationships
    #exclusive_policy_sectors: Mapped[list['SectorModel']] = relationship(back_populates='sector_exclusive_policy', viewonly=True)
    #exclusive_policy_ep_permisions: Mapped[list['EpPermissionModel']] = relationship(back_populates='ep_permission_exclusive_policy', viewonly=True)
    #exclusive_policy_labels: Mapped[list['LabelModel']] = relationship(
        #secondary='ep_permission', back_populates='label_exclusive_policy',viewonly=True)
