from enum import Enum, auto
from typing import Any

from fastapi import APIRouter, Query, Depends
from pydantic import BaseModel as BaseSchema
from sqlalchemy.orm import Session

from server.database.config import get_db
from server.common.models.base import BaseModel
from server.services.auth import AuthReq
from server.services.dbservice import BaseDbService


class RouteType(str, Enum):
    get_all = auto()
    create = auto()
    delete_multiple = auto()
    get_by_id = auto()
    update = auto()
    delete = auto()


def register_db_routes(
        *,
        router: APIRouter,
        service: type[BaseDbService],
        model: type[BaseModel],
        create_schema: type[BaseSchema],
        update_schema: type[BaseSchema],
        out_schema: type[BaseSchema],
        omit: list[RouteType] | None = None,
        names: dict[RouteType, str] | None = None,
        auth: dict[RouteType, Any] | None = None
) -> None:
    omit = omit if omit is not None else []
    names = names if names is not None else {}
    auth = auth if auth is not None else {}

    name = model.__tablename__.capitalize()

    if RouteType.get_all not in omit:
        @router.get(
            '/',
            response_model=list[out_schema],
            name=names.get(RouteType.get_all) or f'Get All {name}s',
            dependencies=[Depends(auth.get(RouteType.get_all) or AuthReq.current_user_has_permission)]
        )
        def get_all(
                skip: int = Query(default=0, ge=0),
                limit: int | None = Query(default=100, ge=0),
                db: Session = Depends(get_db)
        ):
            return service(db=db).get_all(skip=skip, limit=limit)

    if RouteType.create not in omit:
        @router.post(
            '/',
            response_model=out_schema,
            name=names.get(RouteType.create) or f'Create {name}',
            dependencies=[Depends(auth.get(RouteType.create) or AuthReq.current_user_has_permission)]
        )
        def create(item: create_schema, db: Session = Depends(get_db)):
            return service(db=db).create(obj=item)

    if RouteType.delete_multiple not in omit:
        @router.delete(
            '/',
            response_model=list[out_schema],
            name=names.get(RouteType.delete_multiple) or f'Delete Multiple {name}s',
            dependencies=[Depends(auth.get(RouteType.delete_multiple) or AuthReq.current_user_has_permission)]
        )
        def delete_multiple(ids: list[int], db: Session = Depends(get_db)):
            deleted_users = []
            for id in ids:
                deleted_user = service(db=db).delete(id=id)
                deleted_users.append(deleted_user)
            return deleted_users

    if RouteType.get_by_id not in omit:
        @router.get(
            '/{id}',
            response_model=out_schema,
            name=names.get(RouteType.get_by_id) or f'Get {name} By Id',
            dependencies=[Depends(auth.get(RouteType.get_by_id) or AuthReq.current_user_has_permission)]
        )
        def get_by_id(id: int, db: Session = Depends(get_db)):
            return service(db=db).get_by_id(id=id)

    if RouteType.update not in omit:
        @router.put(
            '/{id}',
            response_model=out_schema,
            name=names.get(RouteType.update) or f'Update {name}',
            dependencies=[Depends(auth.get(RouteType.update) or AuthReq.current_user_has_permission)]
        )
        def update(
                id: int,
                item: update_schema,
                db: Session = Depends(get_db)
        ):
            return service(db=db).update(id=id, obj=item)

    if RouteType.delete not in omit:
        @router.delete(
            '/{id}',
            response_model=out_schema,
            name=names.get(RouteType.delete) or f'Delete {name}',
            dependencies=[Depends(auth.get(RouteType.delete) or AuthReq.current_user_has_permission)]
        )
        def delete(
                id: int,
                db: Session = Depends(get_db)
        ):
            return service(db=db).delete(id=id)
