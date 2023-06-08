from faker import Faker
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from server.common.models.ep_permission import EpPermissionModel
from server.common.models.sector import SectorModel
from server.common.models.user import UserModel
from server.common.schemas.sector import SectorCreateSchema, SectorUpdateSchema
from server.common.utils import IMockDataGenerator
from server.database.sector import SectorDbManager
from server.services.dbservice import BaseDbService
from server.services.label import LabelService
from server.services.public_policy import PublicPolicyService
from server.services.user import UserService


class SectorService(BaseDbService[SectorModel, SectorCreateSchema, SectorUpdateSchema], IMockDataGenerator):

    def __init__(self, db: Session):
        self.db = db
        super().__init__(db=db, db_manager=SectorDbManager)

    def get_sectors_user_has_permission(self, user: UserModel) -> list[SectorModel]:
        # Find exclusive sectors the current user has access to
        active_user_labels = UserService(self.db).get_active_user_labels(user_id=user.id)
        active_user_ep_permissions: set[EpPermissionModel] = set()
        for label in active_user_labels:
            active_label_ep_permissions = LabelService(self.db).get_active_ep_permissions(label_id=label.id)
            active_user_ep_permissions |= active_label_ep_permissions
        ep_ids = set([ep_permission.fk_ep_id for ep_permission in active_user_ep_permissions])
        exclusive_sectors = set(self.get_all(filters={'fk_ep_id': ep_ids}))
        # Find public sectors
        pp_ids = set([ppolicy.id for ppolicy in PublicPolicyService(self.db).get_all()])
        public_sectors = set(self.get_all(filters={'fk_pp_id': pp_ids}))
        return list(public_sectors | exclusive_sectors)

    def assign_policy_to_sector(self, *, sector_id: int, policy_id: int, exclusive: bool):
        updates = {
            'fk_pp_id': policy_id if not exclusive else None,
            'fk_ep_id': policy_id if exclusive else None
        }
        return self.update(id=sector_id, obj=updates)

    def generate_mock_data(self, n: int, /) -> list[SectorModel]:
        fake = Faker()
        created_sectors = []
        for _ in range(n):
            sector = SectorCreateSchema(
                name=fake.word().capitalize(),
                description=fake.sentence(nb_words=50, variable_nb_words=True)
            )
            try:
                created_sector = self.create(obj=sector)
                created_sectors.append(created_sector)
            except IntegrityError:
                self.db.rollback()
                continue
        return created_sectors

