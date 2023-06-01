from random import randint, choice
from string import ascii_uppercase

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from server.common.exceptions.db import NotFoundDbException
from server.common.models.lot import LotModel
from server.common.schemas.lot import LotCreateSchema, LotUpdateSchema
from server.common.utils import IMockDataGenerator
from server.database.lot import LotDbManager
from server.database.sector import SectorDbManager
from server.services.dbservice import BaseDbService


class LotService(BaseDbService[LotModel, LotCreateSchema, LotUpdateSchema], IMockDataGenerator):

    def __init__(self, db: Session):
        self.db = db
        super().__init__(db=db, db_manager=LotDbManager)

    def assign_lot_to_sector(self, lot_id: int, sector_id: int):
        db_lot = self.get_by_id(lot_id)
        db_sector = SectorDbManager(self.db).get_by_id(sector_id)
        if not db_sector:
            raise NotFoundDbException(origin='sector')
        updates = LotUpdateSchema(fk_sector_id=sector_id)
        return self.db_manager.update(db_obj=db_lot, obj=updates)

    def toggle_occupied(self, lot_id):
        db_lot = self.get_by_id(lot_id)
        updates = LotUpdateSchema(occupied=not db_lot.occupied)
        return self.db_manager.update(db_obj=db_lot, obj=updates)

    def toggle_available(self, lot_id):
        db_lot = self.get_by_id(lot_id)
        updates = LotUpdateSchema(occupied=not db_lot.available)
        return self.db_manager.update(db_obj=db_lot, obj=updates)

    def generate_mock_data(self, n: int, /) -> list[LotModel]:
        created_lots = []
        db_sectors = SectorDbManager(self.db).get_all(limit=10)
        for _ in range(n):
            db_setor = choice(db_sectors)
            name = 'Lot ' + str(randint(1, 1_000_000))
            location = choice(ascii_uppercase)
            lot = LotCreateSchema(name=name, location=location, fk_sector_id=db_setor.id)
            try:
                created_lot = self.create(obj=lot)
                created_lots.append(created_lot)
            except IntegrityError:
                self.db.rollback()
                continue
        return created_lots

