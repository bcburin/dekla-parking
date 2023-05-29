from sqlalchemy.orm import Session

from server.common.models.ep_permission import EpPermissionModel
from server.common.schemas.ep_permission import EpPermissionCreateSchema, EpPermissionUpdateSchema
from server.database.basedbmanager import BaseDbManager


class EpPermissionDbManager(BaseDbManager[EpPermissionModel, EpPermissionCreateSchema, EpPermissionUpdateSchema]):

    def __init__(self, db: Session):
        super().__init__(model=EpPermissionModel, db=db)

