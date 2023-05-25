from sqlalchemy.orm import Session

from server.common.models.label import LabelModel
from server.common.schemas.label import LabelCreateSchema, LabelUpdateSchema
from server.database.label import LabelDbManager
from server.services.dbservice import BaseDbService


class LabelService(BaseDbService[LabelModel, LabelCreateSchema, LabelUpdateSchema]):

    def __init__(self, db: Session):
        self.db = db
        super().__init__(db=db, db_manager=LabelDbManager)
