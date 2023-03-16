from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class DeklaParkingDb:
    NAME = 'dekla'
    USER = getenv('DB_USER')
    HOST = getenv('DB_HOST')
    PASSWORD = getenv('DB_PASSWORD')
    PORT = 5432

    SQLALCHEMY_URL = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}'

    ENGINE = create_engine(SQLALCHEMY_URL)

    Session = sessionmaker(
        autocommit=False,
        autoflush=False,
       bind=ENGINE
    )

    @staticmethod
    def get_db() -> Session:
        db = DeklaParkingDb.Session()
        try:
            yield db
        finally:
            db.close()


Base = declarative_base()
