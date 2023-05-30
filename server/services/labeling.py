from random import choice

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from server.common.models.labeling import LabelingModel
from server.common.schemas.labeling import LabelingCreateSchema, LabelingUpdateSchema
from server.common.utils import IMockDataGenerator
from server.database.label import LabelDbManager
from server.database.labeling import LabelingDbManager
from server.database.user import UserDbManager
from server.services.dbservice import BaseDbService


class LabelingService(BaseDbService[LabelingModel, LabelingCreateSchema, LabelingUpdateSchema], IMockDataGenerator):

    def __init__(self, db: Session):
        self.db = db
        super().__init__(db=db, db_manager=LabelingDbManager)

    def generate_mock_data(self, n: int, /) -> list[LabelingModel]:
        if n == 0:
            return []
        db_users = UserDbManager(self.db).get_all(limit=n)
        db_labels = LabelDbManager(self.db).get_all(limit=5)
        created_labelings = []
        for db_user in db_users:
            db_label = choice(db_labels)
            labeling = LabelingCreateSchema(fk_user_id=db_user.id, fk_label_id=db_label.id)
            try:
                created_labeling = self.create(obj=labeling)
                created_labelings.append(created_labeling)
            except IntegrityError:
                self.db.rollback()
                continue
        return created_labelings
