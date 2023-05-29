from typing import Any

from sqlalchemy.orm import Session

from server.common.models.sector import SectorModel
from server.common.schemas.sector import SectorCreateSchema, SectorUpdateSchema
from server.database.basedbmanager import BaseDbManager


class SectorDbManager(BaseDbManager[SectorModel, SectorCreateSchema, SectorUpdateSchema]):

    def __init__(self, db: Session):
        super().__init__(model=SectorModel, db=db)

    def create(self, *, obj: SectorCreateSchema, refresh: bool = True) -> SectorModel:
        user_data = {
            **obj.dict(),
        }
        db_user = SectorModel(**user_data)
        self.db.add(db_user)
        self.db.commit()
        if refresh:
            self.db.refresh(db_user)
        return db_user

    def update(self, db_obj: SectorModel, obj: SectorUpdateSchema | dict[str, Any]) -> SectorModel:
        if isinstance(obj, dict):
            update_data = obj
        else:
            update_data = obj.dict(exclude_unset=True)
        if 'fk_pp_id' in update_data:
            update_data['fk_pp_id'] = obj.fk_pp_id
        else:
            update_data['fk_ep_id'] = obj.fk_ep_id
        return super().update(db_obj=db_obj, obj=update_data)