from sqlalchemy.orm import Session

from server.common.models.label import LabelModel
from server.common.schemas.label import LabelCreateSchema, LabelUpdateSchema
from server.database.basedbmanager import BaseDbManager


class LabelDbManager(BaseDbManager[LabelModel, LabelCreateSchema, LabelUpdateSchema]):

    def __init__(self, db: Session):
        super().__init__(model=LabelModel, db=db)

    def get_by_name(self, name: str) -> LabelModel | None:
        return self.get_by_unique_attribute(name, 'name')

    def create(self, *, obj: LabelCreateSchema, refresh: bool = True) -> LabelModel:
        user_data = {
            **obj.dict(),
        }
        db_user = LabelModel(**user_data)
        self.db.add(db_user)
        self.db.commit()
        if refresh:
            self.db.refresh(db_user)
        return db_user


