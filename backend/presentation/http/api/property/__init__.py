from typing import List
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Form
from fastapi import HTTPException
from fastapi import status
from domain.property import Property
from domain.property.structures.image import ImageFile
from .deps import get_image_files_from_images
from .schemas import UpdateProperty, ReadProperty
from services.exceptions import ServiceError
from services.property import PropertyService
from infrasctructure.database.repositories import RepositoryError
from infrasctructure.database.repositories.factory import RepositoryFactory


router = APIRouter(prefix='/property', tags=['Property', ])
repository = RepositoryFactory.get_repository(Property)


@router.get('/', response_model=List[ReadProperty])
def get_all_properties():
    with PropertyService(repository) as service:
        properties = service.get_multi()
    return properties


@router.get('/{id}', response_model=ReadProperty)
def get_property_by_id(id: int):
    with PropertyService(repository) as service:
        try:
            prop = service.get(id=id)
        except ServiceError as err:
            raise HTTPException(
                status.HTTP_404_NOT_FOUND,
                detail=err.cause
            )
    return prop


@router.post('/', response_model=ReadProperty)
def create_property(
    name: str = Form(...),
    photos: ImageFile = Depends(get_image_files_from_images)
):
    with PropertyService(repository) as service:
        try:
            prop = service.create(name, photos=photos)
        except (ServiceError, RepositoryError) as err:
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                detail=err.cause
            )
    return prop


@router.put('/{id}', response_model=ReadProperty)
def update_property(
    id: int,
    obj_in: UpdateProperty,
):
    with PropertyService(repository) as service:
        try:
            prop = service.update(id, obj_in)
        except ServiceError as err:
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                detail=err.cause
            )
    return prop


@router.delete('/{id}', response_model=ReadProperty)
def delete_property(id: int):
    with PropertyService(repository) as service:
        try:
            prop = service.delete(id)
        except ServiceError as err:
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                detail=err.cause
            )
    return prop
