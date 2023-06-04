from sqlalchemy.orm import Session
from faker import Faker
from sqlalchemy.exc import IntegrityError

from server.common.models.public_policy import PublicPolicyModel
from server.common.schemas.public_policy import PublicPolicyCreateSchema, PublicPolicyUpdateSchema
from server.database.public_policy import PublicPolicyDbManager
from server.services.dbservice import BaseDbService
from server.common.utils import get_is_active, get_is_expired, IMockDataGenerator

class PublicPolicyService(BaseDbService[PublicPolicyModel, PublicPolicyCreateSchema, PublicPolicyUpdateSchema]):

    def __init__(self, db: Session):
        self.db = db
        super().__init__(db=db, db_manager=PublicPolicyDbManager)

    def generate_mock_data(self, n: int, /) -> list[PublicPolicyModel]:
        created_policies = []
        fake = Faker()
        for _ in range(n):
            name: str = fake.job()
            policyname = (name[0:4]).lower()
            descriptor = "Policy for people with job " + name
            price = fake.random_int(0, 100)
            policy = PublicPolicyCreateSchema(
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
