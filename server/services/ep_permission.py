from random import choice
from datetime import datetime, timedelta

from faker import Faker
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from server.common.models.ep_permission import EpPermissionModel
from server.common.schemas.ep_permission import EpPermissionCreateSchema, EpPermissionUpdateSchema
from server.database.ep_permission import EpPermissionDbManager
from server.database.exclusive_policy import ExclusivePolicyDbManager
from server.database.label import LabelDbManager
from server.services.dbservice import BaseDbService


class EpPermissionService(BaseDbService[EpPermissionModel, EpPermissionCreateSchema, EpPermissionUpdateSchema]):

    def __init__(self, db: Session):
        self.db = db
        super().__init__(db=db, db_manager=EpPermissionDbManager)

    def generate_mock_data(self, n: int, /) -> list[EpPermissionModel]:
        if n == 0:
            return []
        fake = Faker()
        db_policies = ExclusivePolicyDbManager(self.db).get_all(limit=n)
        db_labels = LabelDbManager(self.db).get_all(limit=5)
        created_eppermissions = []
        for db_policy in db_policies:
            db_label = choice(db_labels)
            start_time = fake.date_time_between(
                start_date=datetime.now(),
                end_date=datetime.now() + timedelta(days=2))
            end_time = fake.date_time_between(
                start_date=start_time + timedelta(hours=8),
                end_date=start_time + timedelta(days=1))
            ep_permission = EpPermissionCreateSchema(
                start_time=choice([start_time, None]),
                end_time=choice([end_time, None]),
                fk_ep_id=db_policy.id,
                fk_label_id=db_label.id
            )
            try:
                created_eppermission = self.create(obj=ep_permission)
                created_eppermissions .append(created_eppermission)
            except IntegrityError:
                self.db.rollback()
                continue
        return created_eppermissions
