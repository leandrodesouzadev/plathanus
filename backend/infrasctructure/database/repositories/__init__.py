from abc import ABC, abstractmethod
from typing import List
from typing import TypeVar
from infrasctructure.database.connectors import DatabaseConnector
from infrasctructure.database.models import DeclarativeBase
from domain import DomainModel


DomainType = TypeVar("DomainType", bound=DomainModel)
ModelType = TypeVar("ModelType", bound=DeclarativeBase)


class RepositoryBase(ABC):

    model: ModelType

    @abstractmethod
    def get_one(self, db: DatabaseConnector, id: int) -> DomainType:
        ...

    @abstractmethod
    def get_multi(self, db: DatabaseConnector) -> List[DomainType]:
        ...

    @abstractmethod
    def create(self, db: DatabaseConnector, obj: DomainType) -> DomainType:
        ...

    @abstractmethod
    def update(self, db: DatabaseConnector, obj: DomainType, other: DomainType) -> DomainType:
        ...

    @abstractmethod
    def delete(self, db: DatabaseConnector, obj: ModelType) -> DomainType:
        ...


class RepositoryError(Exception):
    cause: str

    def __init__(self, cause: str) -> None:
        self.cause = cause
        super().__init__(cause)
