from typing import List
from fastapi import UploadFile
from pydantic import BaseModel


class BaseProperty(BaseModel):
    name: str


class UpdateProperty(BaseProperty):
    ...


class ReadProperty(BaseProperty):

    class Config:
        orm_mode = True
        