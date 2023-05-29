from sqlalchemy.orm import Session

from server.common.models.exclusive_policy import ExclusivePolicyModel
from server.common.schemas.exclusive_policy import ExclusivePolicyCreateSchema, ExclusivePolicyUpdateSchema
from server.database.basedbmanager import BaseDbManager


class ExclusivePolicyDbManager(BaseDbManager[ExclusivePolicyModel, ExclusivePolicyCreateSchema, ExclusivePolicyUpdateSchema]):

    def __init__(self, db: Session):
        super().__init__(model=ExclusivePolicyModel, db=db)

    def get_by_name(self, name: str) -> ExclusivePolicyModel | None:
        return self.get_by_unique_attribute(name, 'name')

