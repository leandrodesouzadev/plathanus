from typing import List
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi import File
from fastapi import Form
from fastapi import UploadFile
from fastapi import Depends
from fastapi import status
from fastapi import HTTPException
from domain.property import Property
from domain import DomainError
from presentation.http.dependencies import get_connector
from infrasctructure.database.connectors import DatabaseConnector
from infrasctructure.database.models.property import PropertyRegister
from infrasctructure.database.repositories.property import crud_property


def get_property_by_id(
    id: int,
    connector: DatabaseConnector = Depends(get_connector)
) -> PropertyRegister:

    prop = crud_property.get_one(connector, id=id)
    if not prop:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No such property"
        )
    return prop


def create_property_obj(
    name: str = Form(...),
    images: List[UploadFile] = File(...)
) -> Property:

    for image in images:
        if image.content_type != "image/png":
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                detail="Invalid type for image"
            )
    try:
        obj_in = Property(name, images)
    except DomainError as err:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail=err.cause
        )
    return obj_in