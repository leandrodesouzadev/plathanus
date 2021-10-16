from abc import ABC, abstractmethod


class BaseStorage(ABC):

    @abstractmethod
    def save(self, filename: str, content: bytes) -> str:
        return "ID of file"

    @abstractmethod
    def delete(self, filename: str):
        ...
