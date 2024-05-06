"""Service for manage phone address."""

from app.internal.repository.repository import BaseRepository
from app.pkg import models

__all__ = ["PhoneAddressService"]


class PhoneAddressService:
    """Service for manage phone address."""

    def __init__(self, phone_address_repository: BaseRepository):
        self.repository = phone_address_repository

    async def read_phone_address(
            self,
            query: models.ReadPhoneAddressCommand,
    ) -> models.PhoneAddress:
        """Read phone address.

        Args:
            query: ReadPhoneAddressCommand command.

        Returns:
            PhoneAddress: Read phone address.
        """
        return await self.repository.read(query=query)

    async def create_phone_address(
            self,
            cmd: models.CreatePhoneAddressCommand
    ) -> models.PhoneAddress:
        """Create phone address.

        Args:
            cmd: CreatePhoneAddressCommand command.

        Returns:
            PhoneAddress: Created phone address.
        """
        return await self.repository.create(cmd=cmd)

    async def update_phone_address(
            self,
            cmd: models.UpdatePhoneAddressCommand,
    ) -> models.PhoneAddress:
        """Update phone address.

        Args:
            cmd: UpdatePhoneAddressCommand command.

        Returns:
            PhoneAddress: Updated phone address.
        """
        return await self.repository.update(cmd=cmd)
