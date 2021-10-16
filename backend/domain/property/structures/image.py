from typing import List
from domain import DomainModel
from domain import DomainError


class ImageFile(DomainModel):
    ALLOWED_CONTENT_TYPES: List[str] = [
        "image/png",
        "image/jpeg",
        "image/bmp"
    ]
    filename: str
    content_type: str
    content: bytes

    def __init__(
        self, filename: str, content_type: str, content: bytes
    ):

        self.filename = filename.lower()
        self.content_type = content_type.lower()
        self.content = content

    def raise_for_invalid_image(self):
        if self.content_type not in self.ALLOWED_CONTENT_TYPES:
            raise DomainError((
                f"Image type '{self.content_type}' not allowed. "
                f"Allowed types: {', '.join(self.ALLOWED_CONTENT_TYPES)}"
            ))
