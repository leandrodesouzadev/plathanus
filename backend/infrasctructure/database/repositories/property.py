from domain.property import Property
from infrasctructure.database.connectors import DatabaseConnector
from infrasctructure.database.repositories.sql_repo import SQLCrudOperations
from infrasctructure.database.models.property import PropertyRegister


class PropertyCrud(SQLCrudOperations):
    def __init__(self, model):
        super().__init__(model)
    
    def create(self, db: DatabaseConnector, obj: Property) -> PropertyRegister:
        obj_in = super().create(db, obj)
        for photo in Property.photos:
            print(photo)


crud_property = PropertyCrud(PropertyRegister)
