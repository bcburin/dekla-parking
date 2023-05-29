from sqlalchemy.orm import Session

from server.common.exceptions.db import NotFoundDbException
from server.common.models.lot import LotModel
from server.common.schemas.lot import LotCreateSchema, LotUpdateSchema
from server.database.lot import LotDbManager
from server.database.sector import SectorDbManager
from server.services.dbservice import BaseDbService


class LotService(BaseDbService[LotModel, LotCreateSchema, LotUpdateSchema]):

    def __init__(self, db: Session):
        self.db = db
        super().__init__(db=db, db_manager=LotDbManager)

    def assign_lot_to_sector(self, lot_id: int, sector_id: int):
        db_lot = self.get_by_id(lot_id)
        db_sector = SectorDbManager(self.db).get_by_id(sector_id)
        if not db_sector:
            raise NotFoundDbException(origin='sector')
        updates = LotUpdateSchema(fk_sector_id=sector_id)
        self.db_manager.update(db_obj=db_lot, obj=updates)

