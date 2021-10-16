from fastapi import APIRouter
from fastapi import Request
from fastapi import Form
from fastapi import Depends
from fastapi.responses import RedirectResponse
from presentation.http.api.property.deps import get_image_files_from_images
from fastapi.templating import Jinja2Templates
from services.exceptions import ServiceError
from services.property import PropertyService
from infrasctructure.database.repositories import RepositoryError
from domain.property.structures.image import ImageFile
from infrasctructure.database.repositories.factory import RepositoryFactory
from domain.property import Property


router = APIRouter(prefix='/ui', include_in_schema=False)
templates_engine = Jinja2Templates("backend/presentation/http/ui/templates/")
repository = RepositoryFactory.get_repository(Property)


@router.get("/")
def index(request: Request):
    return RedirectResponse('/ui/properties')


@router.get('/properties')
@router.post('/properties')
def properties_view(request: Request):
    with PropertyService(repository) as service:
        props = service.get_multi()
    return templates_engine.TemplateResponse('properties_view.html', context={'request': request, 'properties': props})


@router.get('/properties/new')
def show_add_form(request: Request):
    return templates_engine.TemplateResponse('property_create.html', context={
        'request': request,
        'has_errors': False,
        'error_message': None
    })


@router.get('/properties/{id}')
def property_view(id: int, request: Request):
    with PropertyService(repository) as service:
        prop = service.get(id)
    return templates_engine.TemplateResponse('property_view.html', context={'request': request, 'property': prop})


@router.post('/properties/')
def create_property(
    request: Request,
    name: str = Form(...),
    photos: ImageFile = Depends(get_image_files_from_images)
):
    with PropertyService(repository) as service:
        try:
            service.create(name, photos=photos)
        except (ServiceError, RepositoryError) as err:
            return templates_engine.TemplateResponse('property_create.html', context={
                'request': request,
                'has_errors': True,
                'error_message': err.cause
            })
    return RedirectResponse('/ui/properties')