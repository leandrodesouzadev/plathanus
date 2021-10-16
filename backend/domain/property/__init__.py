from typing import List
from domain import DomainModel
from domain import DomainError


class Property(DomainModel):
    name: str
    photos: List

    def __init__(self, name: str, photos: List = None, **kwargs):
        self.name = name
        self.photos = photos
        self.has_enough_photos()
        self.has_valid_name()

    def has_enough_photos(self):
        if not self.photos or not len(self.photos) > 2:
            raise DomainError("Not enough photos. At least 3 photos required.")
    
    def has_valid_name(self):
        if len(self.name) < 10:
            raise DomainError("Name is too short. It must contain at least 10 characteres")
