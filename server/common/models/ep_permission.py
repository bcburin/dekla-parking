from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from server.database.config import Base

if TYPE_CHECKING:
    from server.common.models.exclusive_policy import ExclusivePolicyModel
    from server.common.models.label import LabelModel


class EpPermissionModel(Base):
    __tablename__ = 'ep_permission'

    # Fields
    fk_ExclusivePolicy_id: Mapped[int] = mapped_column(unique=True)
    fk_LabelPolicy_id: Mapped[int] = mapped_column(unique=True)
    start_time: Mapped[str] = mapped_column(unique=True)
    end_time: Mapped[str] = mapped_column(unique=True)

    # Relationships
    ep_permission_excluive_policy: Mapped['ExclusivePolicyModel'] = relationship(back_populates='exclusive_policy_ep_permission', viewonly=True)
    ep_permision_label: Mapped['LabelModel'] = relationship(back_populates='ep_permission_exclusive_policy', viewonly=True)