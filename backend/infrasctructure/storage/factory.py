from .local import LocalStorage
from . import BaseStorage


class StorageFactory():
    storages = {
        'local': LocalStorage()
    }

    @classmethod
    def get_storage(cls, key: str) -> BaseStorage:
        return cls.storages[key]
