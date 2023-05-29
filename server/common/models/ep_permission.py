from datetime import datetime

from server.common.models.base import IntervalModel, BaseModel
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


if TYPE_CHECKING:
    from server.common.models.exclusive_policy import ExclusivePolicyModel
    from server.common.models.label import LabelModel


class EpPermissionModel(BaseModel, IntervalModel):
    __tablename__ = 'ep_permission'

    # Fields
    id: Mapped[int] = mapped_column(primary_key=True)
    fk_ep_id: Mapped[int] = mapped_column(ForeignKey('exclusive_policy.id'))
    fk_label_id: Mapped[int] = mapped_column(ForeignKey('label.id'))

    # Relationships
'''
    ep_permission_exclusive_policy: Mapped['ExclusivePolicyModel'] = relationship(
        back_populates='exclusive_policy_ep_permissions',
        viewonly=True
    )
    ep_permission_label: Mapped['LabelModel'] = relationship(
        back_populates='label_ep_permissions',
        viewonly=True
    )

'''