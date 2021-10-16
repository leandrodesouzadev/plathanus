import os
from . import DatabaseConnector
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine


class PostgreSQLConnector(DatabaseConnector):

    _db: Session

    @property
    def connection(self) -> Session:
        return self._db

    def connect(self):
        engine = create_engine(os.environ["DB_CONN_STR"])
        Sess = sessionmaker(engine)
        self._db = Sess()

    def disconnect(self):
        try:
            self._db.close()
        except Exception:
            return
