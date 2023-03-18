from typing import Any, Dict, Generic, List, Optional, Type, TypeVar

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from server.database.config import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseCRUD(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType], db: Session):
        self.model = model
        self.db = db

    def get_by_id(
            self,
            id_value: Any,
            id_name: str = 'id'
    ) -> Optional[ModelType]:
        return self.db.query(self.model).filter(getattr(self.model, id_name) == id_value).first()

    def get_all(
            self,
            *,
            skip: int = 0,
            limit: int | None = None
    ) -> List[ModelType]:
        if limit:
            return self.db.query(self.model).offset(skip).limit(limit).all()
        return self.db.query(self.model).offset(skip).all()

    def create(
            self,
            *,
            obj: CreateSchemaType,
            refresh: bool = True
    ) -> ModelType:
        obj_in_data = jsonable_encoder(obj)
        db_obj = self.model(**obj_in_data)  # type: ignore
        self.db.add(db_obj)
        self.db.commit()
        if refresh:
            self.db.refresh(db_obj)
        return db_obj

    def update(
            self,
            *,
            db_obj: ModelType,
            obj: UpdateSchemaType | Dict[str, Any]
    ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        if not obj_data:
            self.db.refresh(db_obj)
            obj_data = jsonable_encoder(db_obj)
        if isinstance(obj, dict):
            update_data = obj
        else:
            update_data = obj.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def remove(self, *, pk: Any) -> ModelType:
        obj = self.db.query(self.model).get(pk)
        if not obj:
            return None
        self.db.delete(obj)
        self.db.commit()
        return obj
