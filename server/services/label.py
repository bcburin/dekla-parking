from random import randint

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from server.common.models.label import LabelModel
from server.common.schemas.label import LabelCreateSchema, LabelUpdateSchema
from server.common.utils import IMockDataGenerator
from server.database.label import LabelDbManager
from server.services.dbservice import BaseDbService


class LabelService(BaseDbService[LabelModel, LabelCreateSchema, LabelUpdateSchema], IMockDataGenerator):

    def __init__(self, db: Session):
        self.db = db
        super().__init__(db=db, db_manager=LabelDbManager)

    def generate_mock_data(self, n: int, /) -> list[LabelModel]:
        created_labels = []
        for _ in range(n):
            name = 'Label ' + str(randint(1, 1_000_000))
            color = "%06x" % randint(0, 0xFFFFFF)
            priority = randint(0, 100)
            label = LabelCreateSchema(
                name=name,
                description='Description of ' + name + '.',
                priority=priority,
                color=color
            )
            try:
                created_label = self.create(obj=label)
            except IntegrityError:
                self.db.rollback()
                continue
            created_labels.append(created_label)
        return created_labels
