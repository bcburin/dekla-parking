from datetime import timedelta, datetime
from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext
from pydantic import ValidationError
from sqlalchemy.orm import Session
from starlette.status import HTTP_401_UNAUTHORIZED

from server.common.exceptions.auth import AuthException
from server.common.schemas.user import UserOutSchema
from server.database.config import get_db
import server.database.user as dbu


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="v1/users/login")


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def authenticate_user(db: Session, email: str, password: str):
    user = dbu.UserDbManager(db).get_by_email(email=email)
    if not user or not verify_password(password, user.password_hash):
        return False
    return user


def get_current_user(db: Annotated[Session, Depends(get_db)], token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        expire_time: datetime = payload.get('exp')
        converted_datetime = datetime.fromtimestamp(expire_time)
        currtime = datetime.utcnow() - timedelta(hours=3)
        print(converted_datetime, currtime)
        if username is None or currtime > converted_datetime:
            raise credentials_exception
    except (JWTError, ValidationError):
        raise credentials_exception
    user = dbu.UserDbManager(db).get_by_username(username=username)
    if user is None:
        raise credentials_exception
    return user


CurrentUser = Annotated[UserOutSchema, Depends(get_current_user)]


class AuthReq:
    """
    Contains static methods to be used in FastAPI's Depends() in order to enforce authentication requirements.
    """

    @staticmethod
    def current_user_has_permission(current_user: CurrentUser):
        if not current_user:
            raise AuthException('Not Authenticated')
        if not current_user.is_admin:
            raise AuthException('Not enough permissions')

    @staticmethod
    def current_user_is_authenticated(current_user: CurrentUser):
        if not current_user:
            raise AuthException('Not Authenticated')

    @staticmethod
    def no_auth_restrictions():
        pass
