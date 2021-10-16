from abc import ABC, abstractmethod
from typing import List
from typing import TypeVar
from infrasctructure.database.connectors import DatabaseConnector
from infrasctructure.database.models import DeclarativeBase
from domain import DomainModel


DomainType = TypeVar("DomainType", bound=DomainModel)
ModelType = TypeVar("ModelType", bound=DeclarativeBase)


class CrudBase(ABC):

    model: ModelType

    @abstractmethod
    def get_one(self, db: DatabaseConnector) -> DomainType:
        ...

    @abstractmethod
    def get_multi(self, db: DatabaseConnector) -> List[DomainType]:
        ...

    @abstractmethod
    def create(self, db: DatabaseConnector) -> DomainType:
        ...

    @abstractmethod
    def update(self, db: DatabaseConnector) -> DomainType:
        ...

    @abstractmethod
    def delete(self, db: DatabaseConnector) -> DomainType:
        ...
