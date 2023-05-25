from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from server.common.models.base import IntervalModel, BaseModel

if TYPE_CHECKING:
    from server.common.models.label import LabelModel
    from server.common.models.user import UserModel


class LabelingModel(BaseModel, IntervalModel):
    __tablename__ = 'labeling'

    # Fields
    id: Mapped[int] = mapped_column(primary_key=True)
    fk_user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    fk_label_id: Mapped[int] = mapped_column(ForeignKey('label.id'))

    # Relationships
    labeled_user: Mapped['UserModel'] = relationship(back_populates='user_labelings', viewonly=True)
    labeling_label: Mapped['LabelModel'] = relationship(back_populates='label_labelings', viewonly=True)
