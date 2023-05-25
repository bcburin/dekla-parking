from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from server.common.models.base import BaseModel

if TYPE_CHECKING:
    from server.common.models.sector import SectorModel


class PublicPolicyModel(BaseModel):
    __tablename__ = 'public_policy'

    # Fields
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    descriptor: Mapped[str] = mapped_column()
    price: Mapped[float] = mapped_column()

    # Relationships
    public_policy_sectors: Mapped[list['SectorModel']] = relationship(
        back_populates='sector_public_policy',
        viewonly=True
    )
