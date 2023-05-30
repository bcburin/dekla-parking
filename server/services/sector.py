from random import randint

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from server.common.models.sector import SectorModel
from server.common.schemas.sector import SectorCreateSchema, SectorUpdateSchema
from server.common.utils import IMockDataGenerator
from server.database.sector import SectorDbManager
from server.services.dbservice import BaseDbService


class SectorService(BaseDbService[SectorModel, SectorCreateSchema, SectorUpdateSchema], IMockDataGenerator):

    def __init__(self, db: Session):
        self.db = db
        super().__init__(db=db, db_manager=SectorDbManager)

    def generate_mock_data(self, n: int, /) -> list[SectorModel]:
        created_sectors = []
        for _ in range(n):
            name = 'Sector ' + str(randint(1, 1_000_000))
            sector = SectorCreateSchema(name=name, description='Description of ' + name + '.')
            try:
                created_sector = self.create(obj=sector)
                created_sectors.append(created_sector)
            except IntegrityError:
                self.db.rollback()
                continue
        return created_sectors

