from sqlalchemy.orm import Session

from server.common.models.label import LabelModel
from server.common.schemas.label import LabelCreateSchema, LabelUpdateSchema
from server.database.basebdmanager import BaseBdManager


class LabelDbManager(BaseBdManager[LabelModel, LabelCreateSchema, LabelUpdateSchema]):

    def __init__(self, db: Session):
        super().__init__(model=LabelModel, db=db)

    def get_by_name(self, name: str) -> LabelModel | None:
        return self.get_by_unique_attribute(name, 'name')


