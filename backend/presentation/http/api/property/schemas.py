from typing import List
from typing import Optional
from pydantic import BaseModel


class BaseProperty(BaseModel):
    name: str


class UpdateProperty(BaseProperty):
    ...


class ReadProperty(BaseProperty):

    id: int
    images_ids: Optional[List[int]] = None
