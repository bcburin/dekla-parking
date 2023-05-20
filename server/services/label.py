from sqlalchemy.orm import Session

from server.common.exceptions.db import NotFoundDbException
from server.common.models.label import LabelModel
from server.common.schemas.label import LabelCreateSchema, LabelUpdateSchema
from server.database.label import LabelDbManager
from server.services.dbservice import BasicDbService


class LabelService(BasicDbService[LabelModel, LabelCreateSchema, LabelUpdateSchema]):

    def __init__(self, db: Session):
        self.db = db
        super().__init__(db=db, db_manager=LabelDbManager)

    def get_by_name(self, name: str):
        db_label = LabelDbManager(self.db).get_by_unique_attribute(id_value=name, id_name='name')
        if not db_label:
            raise NotFoundDbException(LabelModel.name)
        return db_label
