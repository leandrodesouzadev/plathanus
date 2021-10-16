from typing import List
from fastapi import File
from fastapi import Request
from fastapi import UploadFile
from fastapi.templating import Jinja2Templates
from domain import DomainError
from domain.property.structures.image import ImageFile

templates_engine = Jinja2Templates("backend/presentation/http/ui/templates/")

def get_image_files_from_images(
    request: Request,
    images: List[UploadFile] = File(...)
):
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
        return templates_engine.TemplateResponse('property_create.html', context={
            'request': request,
            'has_errors': True,
            'error_message': err.cause
        })
    return photos
