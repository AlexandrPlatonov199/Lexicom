"""All connectors in declarative container."""

from dependency_injector import containers, providers

from app.pkg.connectors.redis import RedisContainer

__all__ = ["Connectors", "RedisContainer"]


class Connectors(containers.DeclarativeContainer):
    """Declarative container with all connectors."""

    redis: RedisContainer = providers.Container(RedisContainer)
