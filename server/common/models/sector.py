from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from server.common.models.base import BaseModel

if TYPE_CHECKING:
    from server.common.models.lot import LotModel
    from server.common.models.public_policy import PublicPolicyModel
    from server.common.models.exclusive_policy import ExclusivePolicyModel


class SectorModel(BaseModel):
    __tablename__ = 'sector'

    # Fields
    id: Mapped[int] = mapped_column(primary_key=True)
    fk_pp_id: Mapped[int] = mapped_column(ForeignKey('public_policy.id'), nullable=True)
    fk_ep_id: Mapped[int] = mapped_column(ForeignKey('exclusive_policy.id'), nullable=True)
    name: Mapped[str] = mapped_column()
    available: Mapped[bool] = mapped_column()

    # Relationships
    sector_public_policy: Mapped['PublicPolicyModel'] = relationship(
      back_populates='public_policy_sectors',
        viewonly=True
    )
    sector_exclusive_policy: Mapped['ExclusivePolicyModel'] = relationship(
        back_populates='exclusive_policy_sectors',
        viewonly=True
    )
    sector_lots: Mapped[list['LotModel']] = relationship(
        back_populates='lot_sector',
        viewonly=True
    )
