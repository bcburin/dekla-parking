from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from server.database.config import Base

if TYPE_CHECKING:
    from server.common.models.labeling import LabelingModel
    from server.common.models.user import UserModel
    from server.common.models.ep_permission import EpPermissionModel
    from server.common.models.exclusive_policy import ExclusivePolicyModel


class LabelModel(Base):
    __tablename__ = 'label'

    # Fields
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str] = mapped_column()
    priority: Mapped[int] = mapped_column()

    # Relationships
    label_users: Mapped[list['UserModel']] = relationship(
        secondary='labeling', back_populates='user_labels', viewonly=True)
    label_labelings: Mapped[list['LabelingModel']] = relationship(back_populates='labeling_label', viewonly=True)
    # label_ep_permissions: Mapped[list['EpPermissionModel']] = relationship(
    #     back_populates='ep_permission_label', viewonly=True)
    # label_exclusive_policies: Mapped[list['ExclusivePolicyModel']] = relationship(
    #     secondary='ep_permission', back_populates='exclusive_policy_label', viewonly=True)
