from typing import Type, Any, Generic

from fastapi_restful.api_model import APIModel
from sqlalchemy.orm import Session

from server.common.exceptions.db import NotFoundDbException, NoUpdatesProvidedDbException
from server.common.schemas.base import BaseUpdateSchema
from server.database.basedbmanager import BaseDbManager, ModelType, CreateSchemaType, UpdateSchemaType


class BaseDbService(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):

    def __init__(self, *, db: Session, db_manager: Type[BaseDbManager] | None = None):
        self.db_manager = db_manager(db=db)

    def get_all(
            self,
            skip: int = 0,
            limit: int | None = None,
            filters: dict[str, Any | set[Any]] | None = None,
            order_by: str = 'id',
            columns: list | None = None
    ) -> list[ModelType]:
        return self.db_manager.get_all(skip=skip, limit=limit, filters=filters, order_by=order_by, columns=columns)

    def get_by_id(self, id: Any) -> ModelType:
        db_obj = self.db_manager.get_by_id(id)
        if not db_obj:
            raise NotFoundDbException(origin=self.db_manager.model.__tablename__)
        return db_obj

    def get_by_unique_attribute(self, value: Any, name: str):
        db_obj = self.db_manager.get_by_unique_attribute(value, name)
        if not db_obj:
            raise NotFoundDbException(origin=self.db_manager.model.__tablename__)
        return db_obj

    def create(self, obj: CreateSchemaType | APIModel) -> ModelType:
        # TODO: check for unique key violations
        created_obj = self.db_manager.create(obj=obj)
        return created_obj

    def update(self, id: Any, obj: UpdateSchemaType | BaseUpdateSchema | dict[str, Any]) -> ModelType:
        db_obj = self.db_manager.get_by_id(id)
        if not db_obj:
            raise NotFoundDbException(origin=self.db_manager.model.__tablename__)
        if hasattr(obj, 'has_updates') and not obj.has_updates():
            raise NoUpdatesProvidedDbException(origin=self.db_manager.model.__tablename__)
        updated_obj = self.db_manager.update(obj=obj, db_obj=db_obj)
        return updated_obj

    def delete(self, id: Any):
        deleted_obj = self.db_manager.remove(pk=id)
        if not deleted_obj:
            raise NotFoundDbException(origin=self.db_manager.model.__tablename__)
        return deleted_obj

