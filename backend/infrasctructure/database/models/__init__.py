from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy import Column
from sqlalchemy import Integer


@as_declarative()
class DeclarativeBase:

    id = Column(Integer, primary_key=True)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
