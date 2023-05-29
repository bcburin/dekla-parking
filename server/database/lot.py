from typing import Any

from sqlalchemy.orm import Session

from server.common.models.lot import LotModel
from server.common.schemas.lot import LotCreateSchema, LotUpdateSchema
from server.database.basedbmanager import BaseDbManager


class LotDbManager(BaseDbManager[LotModel, LotCreateSchema, LotUpdateSchema]):

    def __init__(self, db: Session):
        super().__init__(model=LotModel, db=db)

