from functools import lru_cache
from os import getenv
from typing import Iterator

from fastapi_restful.session import FastAPISessionMaker
from sqlalchemy.orm import Session, DeclarativeBase


class Base(DeclarativeBase):
    pass


class DBConfig:
    DEFAULT_NAME = 'dekla'
    DEFAULT_DBMS = 'postgresql'
    DEFAULT_HOST = '127.0.0.1'
    DEFAULT_PORT = '5432'

    def __init__(self):
        self.dbms = getenv('DB_DBMS') or self.DEFAULT_DBMS
        self.host = getenv('DB_HOST') or self.DEFAULT_HOST
        self.port = getenv('DB_PORT') or self.DEFAULT_PORT
        self.name = getenv('DB_NAME') or self.DEFAULT_NAME
        self.user = getenv('DB_USER')
        self.password = getenv('DB_PASSWORD')

    def get_uri(self):
        return f'{self.dbms}://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}'


def get_db() -> Iterator[Session]:
    yield from _get_fastapi_sessionmaker().get_db()


@lru_cache()
def _get_fastapi_sessionmaker() -> FastAPISessionMaker:
    database_uri = DBConfig().get_uri()
    return FastAPISessionMaker(database_uri)
