from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.exc import IntegrityError

from server.database.config import DeklaParkingDb
from server.database.user import UserCRUD
from server.schemas.user import UserOut, UserCreate, UserUpdate

router = APIRouter(
    prefix='/users',
    tags=['users'],
)


@router.get(
    path='/',
    response_model=list[UserOut],
)
def get_users(
        skip: int = Query(
            default=0,
            ge=0,
            description='number of users to skip sequentially in the database'
        ),
        limit: int | None = Query(
            default=100,
            ge=0,
            description='maximum number of users to return '
                        '(may be set to null to return all users in database)'
        ),
        db=Depends(DeklaParkingDb.get_db)
):
    return UserCRUD(db).get_all(skip=skip, limit=limit)


@router.get(
    path='/{user_id}',
    response_model=UserOut,
    responses={404: {'detail': 'No such user.'}}
)
def get_user_by_id(user_id: int, db=Depends(DeklaParkingDb.get_db)):
    user = UserCRUD(db).get_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail='No such user.')
    return user


@router.get(
    path='/find',
    response_model=UserOut,
    responses={
        404: {'detail': 'No such user.'},
        400: {'detail': 'A username or email must be specified.'}
    }
)
def get_user_by_index(username: str | None = None, email: str | None = None, db=Depends(DeklaParkingDb.get_db)):
    if not username and not email:
        raise HTTPException(status_code=400, detail='A username or email must be specified.')
    user = None
    if username:
        user = UserCRUD(db).get_by_username(username)
    elif email:
        user = UserCRUD(db).get_by_email(email)
    if not user:
        raise HTTPException(status_code=404, detail='No such user.')
    return user


@router.post(
    path='/',
    response_model=UserOut,
    responses={400: {'detail': 'DB error string'}}
)
def create_user(user: UserCreate, db=Depends(DeklaParkingDb.get_db)):
    try:
        created_user = UserCRUD(db).create(user=user)
        return created_user
    except IntegrityError as dbe:
        raise HTTPException(status_code=400, detail=dbe.orig.args)


@router.put(
    path='/{user_id}',
    response_model=UserOut,
    responses={
        404: {'detail': 'No such user.'},
        401: {'detail': 'Password authentication is required.'},
        400: {'detail': 'No updates provided.'}
    },
)
def update_user(user_id: int, user: UserUpdate, db=Depends(DeklaParkingDb.get_db)):
    db_user, authenticated = UserCRUD(db).authenticate(id=user_id, password=user.password)
    if not authenticated:
        raise HTTPException(status_code=401, detail='Password authentication failed.')
    if not db_user:
        raise HTTPException(status_code=404, detail='No such user.')
    if not user.has_updates():
        raise HTTPException(status_code=400, detail='No updates provided.')
    updated_user = UserCRUD(db).update(db_user=db_user, user=user)
    return updated_user


@router.delete(
    path='/{user_id}',
    response_model=UserOut,
    responses={404: {'detail': 'No such user'}}
)
def delete_user(user_id: int, db=Depends(DeklaParkingDb.get_db)):
    deleted_user = UserCRUD(db).remove(pk=user_id)
    if not deleted_user:
        raise HTTPException(status_code=404, detail='No such user.')
    return deleted_user
