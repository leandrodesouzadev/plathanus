import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from presentation.http import property
from infrasctructure.database.models import DeclarativeBase
from sqlalchemy import create_engine


app = FastAPI()
app.include_router(property.router)
app.mount('/static', StaticFiles(directory='backend/presentation/static'), 'static')

@app.on_event("startup")
def handle_startup():
    DeclarativeBase.metadata.create_all(
        bind=create_engine(os.environ['DB_CONN_STR'])
    )
