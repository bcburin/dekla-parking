from random import randint

from faker import Faker
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from server.common.exceptions.db import AlreadyExistsDbException
from server.common.models.ep_permission import EpPermissionModel
from server.common.models.label import LabelModel
from server.common.models.labeling import LabelingModel
from server.common.schemas.base import IntervalSchema
from server.common.schemas.label import LabelCreateSchema, LabelUpdateSchema
from server.common.schemas.labeling import LabelingCreateSchema
from server.common.utils import IMockDataGenerator, get_is_active
from server.database.label import LabelDbManager
from server.database.labeling import LabelingDbManager
from server.services.dbservice import BaseDbService
from server.services.user import UserService


class LabelService(BaseDbService[LabelModel, LabelCreateSchema, LabelUpdateSchema], IMockDataGenerator):

    def __init__(self, db: Session):
        self.db = db
        super().__init__(db=db, db_manager=LabelDbManager)

    def assign_label_to_user(self, label_id: int, user_id: int, labeling_times: IntervalSchema | None) -> LabelingModel:
        db_labeling = LabelingDbManager(self.db).get_all(filters={
            'fk_label_id': label_id,
            'fk_user_id': user_id,
            'start_time': labeling_times.start_time if labeling_times else None,
            'end_time': labeling_times.end_time if labeling_times else None,
        })
        if db_labeling:
            raise AlreadyExistsDbException(origin=LabelingModel.__tablename__)
        db_label = self.get_by_id(label_id)
        db_user = UserService(self.db).get_by_id(user_id)
        labeling = LabelingCreateSchema(
            fk_label_id=db_label.id,
            fk_user_id=db_user.id)
        if labeling_times:
            labeling.start_time = labeling_times.start_time
            labeling.end_time = labeling_times.end_time
        created_labeling = LabelingDbManager(self.db).create(obj=labeling)
        return created_labeling

    def get_active_ep_permissions(self, label_id: int) -> set[EpPermissionModel]:
        db_label: LabelModel = self.get_by_id(label_id)
        ep_permissions = db_label.label_ep_permissions
        return set([ep_permission for ep_permission in ep_permissions if get_is_active(obj=ep_permission)])

    def generate_mock_data(self, n: int, /) -> list[LabelModel]:
        fake = Faker()
        created_labels = []
        for _ in range(n):
            name = fake.word().capitalize()
            color = fake.color()
            priority = randint(0, 100)
            label = LabelCreateSchema(
                name=name,
                description=fake.sentence(nb_words=50, variable_nb_words=True),
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
