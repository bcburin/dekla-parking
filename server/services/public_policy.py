from sqlalchemy.orm import Session

from server.common.models.public_policy import PublicPolicyModel
from server.common.schemas.public_policy import PublicPolicyCreateSchema, PublicPolicyUpdateSchema
from server.database.public_policy import PublicPolicyDbManager
from server.services.dbservice import BaseDbService


class PublicPolicyService(BaseDbService[PublicPolicyModel, PublicPolicyCreateSchema, PublicPolicyUpdateSchema]):

    def __init__(self, db: Session):
        self.db = db
        super().__init__(db=db, db_manager=PublicPolicyDbManager)