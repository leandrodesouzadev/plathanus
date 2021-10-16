from typing import Dict
from . import DatabaseConnector
from .sql import PostgreSQLConnector


class ConnectorFactory:

    connectors: Dict[str, DatabaseConnector] = {
        'postgres': PostgreSQLConnector
    }

    @classmethod
    def get_connector(cls, key: str) -> DatabaseConnector:
        _class = cls.connectors.get(
            key, PostgreSQLConnector
        )
        return _class()
