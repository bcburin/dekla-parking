from sqlalchemy.orm import Session

from server.common.models.ep_permission import EpPermissionModel
from server.common.schemas.ep_permission import EpPermissionCreateSchema, EpPermissionUpdateSchema
from server.database.ep_permission import EpPermissionDbManager
from server.services.dbservice import BaseDbService


class EpPermissionService(BaseDbService[EpPermissionModel, EpPermissionCreateSchema, EpPermissionUpdateSchema]):

    def __init__(self, db: Session):
        self.db = db
        super().__init__(db=db, db_manager=EpPermissionDbManager)
