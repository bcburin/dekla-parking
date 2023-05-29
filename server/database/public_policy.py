from sqlalchemy.orm import Session

from server.common.models.public_policy import PublicPolicyModel
from server.common.schemas.public_policy import PublicPolicyCreateSchema, PublicPolicyUpdateSchema
from server.database.basedbmanager import BaseDbManager


class PublicPolicyDbManager(BaseDbManager[PublicPolicyModel, PublicPolicyCreateSchema, PublicPolicyUpdateSchema]):

    def __init__(self, db: Session):
        super().__init__(model=PublicPolicyModel, db=db)

    def get_by_name(self, name: str) -> PublicPolicyModel | None:
        return self.get_by_unique_attribute(name, 'name')

    def create(self, *, obj: PublicPolicyCreateSchema, refresh: bool = True) -> PublicPolicyModel:
        user_data = {
            **obj.dict(),
        }
        db_user = PublicPolicyModel(**user_data)
        self.db.add(db_user)
        self.db.commit()
        if refresh:
            self.db.refresh(db_user)
        return db_user
