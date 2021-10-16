from typing import Any
from abc import ABC, abstractmethod, abstractproperty


class DatabaseConnector(ABC):

    _db: Any

    @abstractproperty
    def connection(self):
        ...

    @abstractmethod
    def connect(self) -> None:
        ...
    
    @abstractmethod
    def disconnect(self) -> None:
        ...
