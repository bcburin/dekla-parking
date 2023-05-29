from sqlalchemy.orm import Session

from server.common.models.sector import SectorModel
from server.common.schemas.sector import SectorCreateSchema, SectorUpdateSchema
from server.database.sector import SectorDbManager
from server.services.dbservice import BaseDbService


class SectorService(BaseDbService[SectorModel, SectorCreateSchema, SectorUpdateSchema]):

    def __init__(self, db: Session):
        self.db = db
        super().__init__(db=db, db_manager=SectorDbManager)

