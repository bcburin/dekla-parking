from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from server.common.models.base import BaseModel

if TYPE_CHECKING:
    from server.common.models.sector import SectorModel
    from server.common.models.ep_permission import EpPermissionModel
    from server.common.models.label import LabelModel


class ExclusivePolicyModel(BaseModel):
    __tablename__ = 'exclusive_policy'

    # Fields
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    descriptor: Mapped[str] = mapped_column()
    price: Mapped[float] = mapped_column()

    # Relationships
    exclusive_policy_sectors: Mapped[list['SectorModel']] = relationship(
        back_populates='sector_exclusive_policy',
        viewonly=True
    )
'''
    exclusive_policy_ep_permissions: Mapped[list['EpPermissionModel']] = relationship(
        back_populates='ep_permission_exclusive_policy',
        cascade='all, delete',
        viewonly=True
    )
    exclusive_policy_labels: Mapped[list['LabelModel']] = relationship(
        secondary='ep_permission',
        back_populates='label_exclusive_policies',
        viewonly=True
    )

'''