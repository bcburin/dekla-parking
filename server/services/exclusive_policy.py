from sqlalchemy.orm import Session

from server.common.models.exclusive_policy import ExclusivePolicyModel
from server.common.schemas.exclusive_policy import ExclusivePolicyCreateSchema, ExclusivePolicyUpdateSchema
from server.database.exclusive_policy import ExclusivePolicyDbManager
from server.services.dbservice import BaseDbService


class ExclusivePolicyService(BaseDbService[ExclusivePolicyModel, ExclusivePolicyCreateSchema, ExclusivePolicyUpdateSchema]):

    def __init__(self, db: Session):
        self.db = db
        super().__init__(db=db, db_manager=ExclusivePolicyDbManager)