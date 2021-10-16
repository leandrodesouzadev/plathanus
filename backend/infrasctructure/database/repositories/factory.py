from domain import DomainModel
from domain.property import Property
from .property import property_repository
from . import RepositoryBase


class RepositoryFactory:

    repos = {
        Property: property_repository
    }

    @classmethod
    def get_repository(
        cls,
        domain_class: DomainModel
    ) -> RepositoryBase:
        return cls.repos[domain_class]
