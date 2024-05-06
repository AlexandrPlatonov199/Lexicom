"""Service layer."""

from dependency_injector import containers, providers

from app.internal.repository import Repositories, redis
from app.internal.services.phone_address import PhoneAddressService


class Services(containers.DeclarativeContainer):
    """Containers with services."""

    repositories: redis.Repositories = providers.Container(
        Repositories.rediss,
    )

    phone_address_service = providers.Factory(
        PhoneAddressService,
        phone_address_repository=repositories.phone_address_repository,
    )
