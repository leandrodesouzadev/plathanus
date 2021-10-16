import os
from . import BaseStorage


class LocalStorage(BaseStorage):
    BASE_PATH = 'backend/presentation/static'

    def save(self, filename: str, content: bytes) -> str:
        path = f'{self.BASE_PATH}/{filename}'
        with open(path, 'wb') as f:
            f.write(content)
        return path

    def delete(self, filename: str):
        path = f'{self.BASE_PATH}/{filename}'
        try:
            os.remove(path)
        except FileNotFoundError:
            print(f"File '{path}' not found, ignoring")
