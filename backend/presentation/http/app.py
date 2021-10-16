import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from presentation.http import api
from presentation.http import ui
from infrasctructure.database.models import DeclarativeBase
from sqlalchemy import create_engine


app = FastAPI(
    title="Tabas Property Manager",
    version="0.1.0"
)
app.mount('/static', StaticFiles(directory='backend/presentation/static'), 'static')
app.include_router(api.router)
app.include_router(ui.router)


@app.on_event("startup")
def handle_startup():
    DeclarativeBase.metadata.create_all(
        bind=create_engine(os.environ['DB_CONN_STR'])
    )


@app.get('/')
def index():
    return RedirectResponse('/ui/properties')
