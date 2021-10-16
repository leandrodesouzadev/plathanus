from typing import List
from ..exceptions import ServiceError
from .. import BaseService
from infrasctructure.database.repositories import RepositoryBase
from domain.property import Property
from domain import DomainError
from domain.property.structures.image import ImageFile


class PropertyService(BaseService):

    repository: RepositoryBase

    def __init__(self, repository: RepositoryBase):
        self.repository = repository
        super().__init__()

    def create(self, name: str, photos: List[ImageFile]):
        prop = Property(name, photos=photos)
        try:
            prop.raise_for_invalid_property()
        except DomainError as err:
            raise ServiceError(err.cause)
        new_prop = self.repository.create(self.connector, prop)
        return {
            'id': new_prop.id,
            'name': new_prop.name,
            'images_ids': [photo.id for photo in new_prop.photos]
        }

    def get_multi(self):
        props: List[Property] = self.repository.get_multi(
            self.connector
        )
        return [{
            'id': prop.id,
            'name': prop.name,
            'images_ids': [photo.id for photo in prop.photos]
        } for prop in props]

    def get(self, id: int):
        prop = self.repository.get_one(self.connector, id=id)
        if not prop:
            raise ServiceError("No such property")
        return {
            'id': prop.id,
            'name': prop.name,
            'images_ids': [photo.id for photo in prop.photos]
        }

    def update(self, id: int, other: dict):
        prop = self.repository.get_one(self.connector, id=id)
        if not prop:
            raise ServiceError("No such property")
        try:
            Property(other.name).has_valid_name()
        except DomainError as err:
            raise ServiceError(err.cause)

        new_prop = self.repository.update(self.connector, prop, other)
        return {
            'id': new_prop.id,
            'name': new_prop.name,
            'images_ids': [photo.id for photo in new_prop.photos]
        }

    def delete(self, id: int):
        prop = self.repository.get_one(self.connector, id=id)
        if not prop:
            raise ServiceError("No such property")
        del_prop = self.repository.delete(self.connector, prop)
        return {
            'id': del_prop.id,
            'name': del_prop.name
        }
