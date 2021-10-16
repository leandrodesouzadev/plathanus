from typing import List
from fastapi import APIRouter
from fastapi import Depends
from domain.property import Property
from .deps import create_property_obj, get_property_by_id
from .schemas import UpdateProperty, ReadProperty
from presentation.http.dependencies import get_connector
from infrasctructure.database.models.property import PropertyRegister
from infrasctructure.database.connectors import DatabaseConnector
from infrasctructure.database.repositories.property import crud_property


router = APIRouter(prefix='/property')


@router.get('/', response_model=List[ReadProperty])
def get_all_properties(
    connector: DatabaseConnector = Depends(get_connector)
):
    properties = crud_property.get_multi(connector)
    return [prop.as_dict() for prop in properties]


@router.get('/{id}', response_model=ReadProperty)
def get_property_by_id(
    prop: PropertyRegister = Depends(get_property_by_id)
):
    return prop.as_dict()


@router.post('/', response_model=ReadProperty)
def create_property(
    obj_in: Property = Depends(create_property_obj),
    connector: DatabaseConnector = Depends(get_connector)
):
    
    prop = crud_property.create(connector, obj_in)
    return prop.as_dict()


@router.put('/{id}', response_model=ReadProperty)
def update_property(
    obj_in: UpdateProperty,
    prop: PropertyRegister = Depends(get_property_by_id),
    connector: DatabaseConnector = Depends(get_connector)
):
    prop = crud_property.update(connector, prop, obj_in)
    return prop.as_dict()


@router.delete('/{id}', response_model=ReadProperty)
def delete_property(
    prop: PropertyRegister = Depends(get_property_by_id),
    connector: DatabaseConnector = Depends(get_connector)
):
    deleted = crud_property.delete(connector, prop)
    return deleted.as_dict()
