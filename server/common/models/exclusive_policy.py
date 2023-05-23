from typing import TYPE_CHECKING

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
    prince: Mapped[float] = mapped_column()

    # Relationships
    exclusive_policy_sector: Mapped[list['SectorModel']] = relationship(back_populates='sector_exclusive_policy', viewonly=True)
    exclusive_policy_ep_permision: Mapped[list['EpPermissionModel']] = relationship(back_populates='ep_permission_exclusive_policy', viewonly=True)
    exclusive_policy_label: Mapped[list['LabelModel']] = relationship(
        secondary='ep_permission', back_populates='label_exclusive_policy',viewonly=True)