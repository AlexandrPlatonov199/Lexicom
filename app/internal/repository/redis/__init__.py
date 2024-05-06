"""All redis repositories are defined here."""

from dependency_injector import containers, providers

from app.internal.repository.redis.phone_address import PhoneAddressRepository


class Repositories(containers.DeclarativeContainer):
    """Container for redis repositories."""

    phone_address_repository = providers.Factory(PhoneAddressRepository)
