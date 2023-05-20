from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from fastapi_restful.guid_type import GUID

from server.database.config import Base

if TYPE_CHECKING:
    from server.common.models.label import LabelModel
    from server.common.models.user import UserModel


class LabelingModel(Base):
    __tablename__ = 'labeling'

    # Fields
    fk_user_id: Mapped[GUID] = mapped_column(ForeignKey('user.id'), primary_key=True)
    fk_label_id: Mapped[GUID] = mapped_column(ForeignKey('label.id'), primary_key=True)
    start_time: Mapped[datetime] = mapped_column()
    end_time: Mapped[datetime] = mapped_column()

    # Relationships
    labeled_user: Mapped['UserModel'] = relationship(back_populates='user_labelings')
    labeling_label: Mapped['LabelModel'] = relationship(back_populates='label_labelings')
