from typing import Any

from sqlalchemy.orm import Session

from server.common.models.sector import SectorModel
from server.common.schemas.sector import SectorCreateSchema, SectorUpdateSchema
from server.database.basedbmanager import BaseDbManager


class SectorDbManager(BaseDbManager[SectorModel, SectorCreateSchema, SectorUpdateSchema]):

    def __init__(self, db: Session):
        super().__init__(model=SectorModel, db=db)

