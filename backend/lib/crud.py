from abc import abstractproperty, ABC


class BaseCrud(ABC):

    def __init__(self):
        ...

    @abstractproperty
    def collection(self) -> str:
        return ""

    def get_one(self):
        ...

    def get_multi(self):
        ...

    def create(self):
        ...

    def update(self):
        ...

    def delete(self):
        ...
