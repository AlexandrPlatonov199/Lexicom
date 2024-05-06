from app.internal.repository.redis.connection import get_connection
from app.internal.repository.repository import Repository
from fastapi import HTTPException

__all__ = ["PhoneAddressRepository"]

from app.pkg import models


class PhoneAddressRepository(Repository):
    """Repository for managing phone addresses."""

    async def read(self, query: models.ReadPhoneAddressCommand) -> models.PhoneAddress:
        """Read phone address from Redis.

        Args:
            query: ReadPhoneAddressCommand command.

        Returns:
            PhoneAddress: Read phone address.
        """
        async with get_connection() as conn:
            res = await conn.get(query.phone)
            return models.PhoneAddress(phone=query.phone, address=res.decode())

    async def create(self, cmd: models.CreatePhoneAddressCommand) -> models.PhoneAddress:
        """Create phone address in Redis.

        Args:
            cmd: CreatePhoneAddressCommand command.

        Returns:
            PhoneAddress: Created phone address.
        """
        async with get_connection() as conn:
            await conn.set(cmd.phone, cmd.address)
            return models.PhoneAddress(phone=cmd.phone, address=cmd.address)

    async def update(self, cmd: models.UpdatePhoneAddressCommand) -> models.PhoneAddress:
        """Update phone address in Redis.

        Args:
            cmd: UpdatePhoneAddressCommand command.

        Returns:
            PhoneAddress: Updated phone address.
        """
        async with get_connection() as conn:
            if not await conn.exists(cmd.phone):
                raise HTTPException(status_code=404, detail="Phone number not found")
            await conn.set(cmd.phone, cmd.address)
            return models.PhoneAddress(phone=cmd.phone, address=cmd.address)

