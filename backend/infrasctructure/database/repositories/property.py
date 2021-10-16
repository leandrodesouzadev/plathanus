import os
from . import RepositoryError
from sqlalchemy.exc import IntegrityError
from domain.property import Property
from infrasctructure.database.connectors import DatabaseConnector
from infrasctructure.database.repositories.sql_repo import SQLRepository
from infrasctructure.database.models.property import PropertyRegister, PropertyRegisterImage
from infrasctructure.storage.factory import StorageFactory


class PropertyRepository(SQLRepository):
    def __init__(self, model):
        super().__init__(model)

    def create(self, db: DatabaseConnector, obj: Property) -> PropertyRegister:
        storage = StorageFactory.get_storage(
            os.environ['STORAGE_TYPE']
        )
        obj_in = self.model()
        obj_in.name = obj.name
        for photo in obj.photos:
            image = PropertyRegisterImage(photo.filename)
            obj_in.photos.append(image)
        db.connection.add(obj_in)
        try:
            db.connection.commit()
        except IntegrityError:
            raise RepositoryError("An property with this name already exists")

        for idx, image in enumerate(obj_in.photos):
            filename = str(image.id)
            photo = obj.photos[idx]
            storage.save(filename, content=photo.content)
        return obj_in

    def delete(self, db: DatabaseConnector, obj: PropertyRegister):
        images = obj.photos
        db.connection.delete(obj)
        db.connection.commit()

        storage = StorageFactory.get_storage(
            os.environ['STORAGE_TYPE']
        )
        for image in images:
            filename = str(image.id)
            storage.delete(filename)
        return obj


property_repository = PropertyRepository(PropertyRegister)
