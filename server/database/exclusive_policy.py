from sqlalchemy.orm import Session

from server.common.models.exclusive_policy import ExclusivePolicyModel
from server.common.schemas.exclusive_policy import ExclusivePolicyCreateSchema, ExclusivePolicyUpdateSchema
from server.database.basedbmanager import BaseDbManager


class ExclusivePolicyDbManager(BaseDbManager[ExclusivePolicyModel, ExclusivePolicyCreateSchema, ExclusivePolicyUpdateSchema]):

    def __init__(self, db: Session):
        super().__init__(model=ExclusivePolicyModel, db=db)

    def get_by_name(self, name: str) -> ExclusivePolicyModel | None:
        return self.get_by_unique_attribute(name, 'name')

    def create(self, *, obj: ExclusivePolicyCreateSchema, refresh: bool = True) -> ExclusivePolicyModel:
        user_data = {
            **obj.dict(),
        }
        db_user = ExclusivePolicyModel(**user_data)
        self.db.add(db_user)
        self.db.commit()
        if refresh:
            self.db.refresh(db_user)
        return db_user