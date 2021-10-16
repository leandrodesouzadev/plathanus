from fastapi import APIRouter
from . import property


router = APIRouter(prefix='/api')
router.include_router(property.router)
