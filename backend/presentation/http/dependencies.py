from infrasctructure.database.connectors import DatabaseConnector
from infrasctructure.database.connectors.factory import ConnectorFactory


def get_connector() -> DatabaseConnector:
    connector = ConnectorFactory.get_connector()
    try:
        connector.connect()
        yield connector
    finally:
        connector.disconnect()
