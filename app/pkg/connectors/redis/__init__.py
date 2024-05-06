"""Container with PostgresSQL connector."""

from dependency_injector import containers, providers

from app.pkg.connectors.redis.resource import Redis
from app.pkg.settings import settings

__all__ = ["RedisContainer"]


class RedisContainer(containers.DeclarativeContainer):
    """Declarative container with PostgresSQL connector."""

    configuration = providers.Configuration(
        name="settings",
        pydantic_settings=[settings],
    )

    connector = providers.Resource(
        Redis,
        dsn=configuration.REDIS.DSN,
    )
