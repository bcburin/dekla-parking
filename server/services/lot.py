from sqlalchemy.orm import Session

from server.common.models.lot import LotModel
from server.common.schemas.lot import LotCreateSchema, LotUpdateSchema
from server.database.lot import LotDbManager
from server.services.dbservice import BasicDbService


class LotService(BasicDbService[LotModel, LotCreateSchema, LotUpdateSchema]):

    def __init__(self, db: Session):
        self.db = db
        super().__init__(db=db, db_manager=LotDbManager)
