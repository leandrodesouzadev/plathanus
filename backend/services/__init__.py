import os
from abc import ABC
from infrasctructure.database.connectors import DatabaseConnector
from infrasctructure.database.connectors.factory import ConnectorFactory


class BaseService(ABC):

    connector: DatabaseConnector

    def __init__(self):
        self.connector = ConnectorFactory.get_connector(
            os.environ['DB_TYPE']
        )

    def __enter__(self):
        self.connector.connect()
        return self

    def __exit__(self, *args):
        self.connector.disconnect()
