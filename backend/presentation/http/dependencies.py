from infrasctructure.database.connectors.sql import PostgreSQLConnector


def get_connector() -> PostgreSQLConnector:
    connector = PostgreSQLConnector()
    try:
        connector.connect()
        yield connector
    finally:
        connector.disconnect()
