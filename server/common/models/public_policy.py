from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from server.database.config import Base

if TYPE_CHECKING:
    from server.common.models.sector import SectorModel


class PublicPolicyModel(Base):
    __tablename__ = 'public_policy'

    # Fields
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    descriptor: Mapped[str] = mapped_column()
    prince: Mapped[float] = mapped_column()

    # Relationships
    public_policy_sector: Mapped[list['SectorModel']] = relationship(back_populates='sector_public_policy', viewonly=True)