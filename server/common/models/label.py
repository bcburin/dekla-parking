from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from server.database.config import Base

if TYPE_CHECKING:
    from server.common.models.labeling import LabelingModel
    from server.common.models.user import UserModel


class LabelModel(Base):
    __table_name__ = 'label'

    # Fields
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    priority: Mapped[int] = mapped_column()

    # Relationships
    label_users: Mapped[list['UserModel']] = relationship(secondary='labeling', back_populates='user_labels')
    label_labelings: Mapped[list['LabelingModel']] = relationship(back_populates='labeling_label')
