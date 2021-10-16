from typing import List
from fastapi import HTTPException
from fastapi import File
from fastapi import UploadFile
from fastapi import HTTPException
from domain import DomainError
from domain.property.structures.image import ImageFile


def get_image_files_from_images(images: List[UploadFile] = File(...)):
    photos = [
        ImageFile(
            filename=image.filename,
            content_type=image.content_type,
            content=image.file.read()
        ) for image in images
    ]
    try:
        for photo in photos:
            photo.raise_for_invalid_image()
    except DomainError as err:
        raise HTTPException(
            400,
            err.cause
        )
    return photos
