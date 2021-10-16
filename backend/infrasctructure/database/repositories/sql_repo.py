from typing import List
from typing import Optional
from . import CrudBase, DomainType, ModelType
from infrasctructure.database.connectors import DatabaseConnector


class SQLCrudOperations(CrudBase):

    def __init__(self, model: ModelType):
        self.model = model

    def get_one(self, db: DatabaseConnector, *, id: int) -> Optional[ModelType]:
        return db.connection.query(self.model).filter_by(id=id).first()
    
    def get_multi(self, db: DatabaseConnector) -> List[ModelType]:
        return db.connection.query(self.model).all()

    def create(self, db: DatabaseConnector, obj: DomainType) -> ModelType:
        inst = self.model()
        for key, value in obj.__dict__.items():
            setattr(inst, key, value)
        db.connection.add(inst)
        db.connection.commit()
        return obj

    def update(self, db: DatabaseConnector, obj: ModelType, other: DomainType) -> ModelType:
        
        encoded = obj.as_dict()
        for key, value in other.__dict__.items():
            if key in encoded:
                setattr(obj, key, value)
        db.connection.add(obj)
        db.connection.commit()
        return obj

    def delete(self, db: DatabaseConnector, obj: ModelType) -> ModelType:
        db.connection.remove(obj)
        db.commit()
        return obj
