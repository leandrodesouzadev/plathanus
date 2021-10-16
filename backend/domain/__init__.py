from abc import ABC


class DomainModel(ABC):

    id: int = None

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id})"


class DomainError(Exception):
    cause: str

    def __init__(self, cause: str) -> None:
        self.cause = cause
        super().__init__(cause)
