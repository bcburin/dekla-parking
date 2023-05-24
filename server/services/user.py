from sqlalchemy.orm import Session

from server.common.exceptions.labeling import UnauthorizedLabelingRemovalException
from server.common.models.booking import BookingModel
from server.common.models.label import LabelModel
from server.common.models.labeling import LabelingModel
from server.common.models.user import UserModel
from server.common.schemas.labeling import LabelingCreateSchema, LabelingCreateForUserSchema, LabelingRequestType
from server.common.schemas.user import UserCreateSchema, UserUpdateSchema
from server.common.utils.labeling import get_labeling_is_active, get_labeling_is_expired
from server.database.labeling import LabelingDbManager
from server.database.user import UserDbManager
from server.services.dbservice import BasicDbService


class UserService(BasicDbService[UserModel, UserCreateSchema, UserUpdateSchema]):

    def __init__(self, db: Session):
        self.db: Session = db
        super().__init__(db=db, db_manager=UserDbManager)

    def toggle_is_admin(self, user_id: int) -> UserModel:
        db_user = self.get_by_id(user_id)
        updated_user = self.db_manager.update(db_obj=db_user, obj={'is_admin': not db_user.is_admin})
        return updated_user

    def add_labelings_to_user(self, *, user_id: int, user_labelings: list[LabelingCreateForUserSchema]) -> None:
        labelings = [
            LabelingCreateSchema(**user_labeling.dict(), fk_user_id=user_id) for user_labeling in user_labelings]
        for labeling in labelings:
            LabelingDbManager(self.db).create(obj=labeling)

    def remove_labelings_from_user(self, *, user_id: int, labeling_ids: list[int]) -> None:
        for labeling_id in labeling_ids:
            labeling = LabelingDbManager(self.db).get_by_id(labeling_id)
            if labeling.fk_user_id != user_id:
                raise UnauthorizedLabelingRemovalException(user_id=user_id, labeling_id=labeling_id)
            LabelingDbManager(self.db).remove(pk=labeling_id)

    def get_user_labelings(
            self, *, user_id: int, labeling_type: LabelingRequestType | None = None) -> list[LabelingModel]:
        db_user = self.get_by_id(user_id)
        if not labeling_type or labeling_type == LabelingRequestType.all:
            return db_user.user_labelings
        if labeling_type == LabelingRequestType.active:
            return [labeling for labeling in db_user.user_labelings if get_labeling_is_active(labeling)]
        if labeling_type == LabelingRequestType.inactive:
            return [labeling for labeling in db_user.user_labelings if not get_labeling_is_active(labeling)]
        if labeling_type == LabelingRequestType.expired:
            return [labeling for labeling in db_user.user_labelings if not get_labeling_is_expired(labeling)]
        return db_user.user_labelings

    def get_active_user_labels(self, user_id: int) -> set[LabelModel]:
        active_labelings = self.get_user_labelings(user_id=user_id, labeling_type=LabelingRequestType.active)
        return set([labeling.labeling_label for labeling in active_labelings])

    def get_user_bookings(self, user_id: int) -> list[BookingModel]:
        db_user = self.get_by_id(user_id)
        return db_user.user_bookings
