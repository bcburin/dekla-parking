from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from server.database.config import Base

if TYPE_CHECKING:
    from server.common.models.lot import LotModel
    from server.common.models.public_policy import PublicPolicyModel
    from server.common.models.exclusive_policy import ExclusivePolicyModel


class SectorModel(Base):
    __tablename__ = 'sector'

    # Fields
    id: Mapped[int] = mapped_column(primary_key=True)
    fk_PublicPolicy_id: Mapped[int] = mapped_column()
    fk_ExclusivePolicy_id: Mapped[int] = mapped_column()
    name: Mapped[str] = mapped_column()
    available: Mapped[bool] = mapped_column()

    # Relationships
    sector_public_policy: Mapped['PublicPolicyModel'] = relationship(
        back_populates='public_policy_sector', viewonly=True)
    sector_exclusive_policy: Mapped['ExclusivePolicyModel'] = relationship(
        back_populates='exclusive_policy_sector', viewonly=True)
    sector_lot: Mapped[list['LotModel']] = relationship(back_populates='lot_sector', viewonly=True)
