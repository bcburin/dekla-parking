from sqlalchemy.orm import Session
from faker import Faker
from sqlalchemy.exc import IntegrityError

from server.common.models.exclusive_policy import ExclusivePolicyModel
from server.common.schemas.exclusive_policy import ExclusivePolicyCreateSchema, ExclusivePolicyUpdateSchema
from server.database.exclusive_policy import ExclusivePolicyDbManager
from server.services.dbservice import BaseDbService


class ExclusivePolicyService(BaseDbService[ExclusivePolicyModel, ExclusivePolicyCreateSchema, ExclusivePolicyUpdateSchema]):

    def __init__(self, db: Session):
        self.db = db
        super().__init__(db=db, db_manager=ExclusivePolicyDbManager)

    def generate_mock_data(self, n: int, /) -> list[ExclusivePolicyModel]:
        created_policies = []
        fake = Faker()
        for _ in range(n):
            name: str = fake.job()
            policyname = (name[0:4]).lower()
            descriptor = "Policy for people with job " + name
            price = fake.random_int(0, 100)
            policy = ExclusivePolicyCreateSchema(
                name=policyname,
                descriptor=descriptor,
                price=price
            )
            try:
                created_policy = self.create(obj=policy)
                created_policies.append(created_policy)
            except IntegrityError:
                self.db.rollback()
                continue
        return created_policies
