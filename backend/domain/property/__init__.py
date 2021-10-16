from typing import List
from domain import DomainModel
from domain import DomainError
from .structures.image import ImageFile


class Property(DomainModel):
    name: str
    photos: List[ImageFile]

    def __init__(self, name: str, photos: List = None, **kwargs):
        self.name = name
        self.photos = photos

    def raise_for_invalid_property(self):
        self.__has_enough_photos()
        self.has_valid_name()
        self.__does_not_contains_duplicate_names()

    def __has_enough_photos(self):
        if not self.photos or not len(self.photos) > 2:
            raise DomainError("Not enough photos. At least 3 photos required.")
        elif len(self.photos) > 5:
            raise DomainError("Too many photos. The maximun number of photos is 5.")

    def has_valid_name(self):
        if len(self.name) < 10:
            raise DomainError(
                "Name is too short. It must contain at least 10 characteres")

    def __does_not_contains_duplicate_names(self):
        photos_names = [photo.filename for photo in self.photos]
        names_set = set(photos_names)
        if len(photos_names) > len(names_set):
            raise DomainError(
                "Duplicate filenames on images are not allowed."
            )
