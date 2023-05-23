from sqlalchemy.orm import Session

from server.common.models.labeling import LabelingModel
from server.common.schemas.labeling import LabelingCreateSchema, LabelingUpdateSchema
from server.database.basedbmanager import BaseDbManager


class LabelingDbManager(BaseDbManager[LabelingModel, LabelingCreateSchema, LabelingUpdateSchema]):

    def __init__(self, db: Session):
        super().__init__(model=LabelingModel, db=db)
