"""Routes for phone address module."""

from dependency_injector.wiring import Provide, inject
from fastapi import Depends, status

from app.internal.routes import phone_address
from app.pkg import models


@phone_address.get(
    "/check_data",
    response_model=models.PhoneAddress,
    status_code=status.HTTP_200_OK,
    description="Get phone address",
)
@inject
async def read_phone_address(
        phone: str,
        phone_address_service: PhoneAddressService = Depends(Provide[Services.phone_address_service]),
):
    return await phone_address_service.read_phone_address(query=models.ReadPhoneAddressCommand(phone=phone))


@phone_address.post(
    "/write_data",
    response_model=models.PhoneAddress,
    status_code=status.HTTP_200_OK,
    description="Create phone address",
)
@inject
async def create_phone_address(
        cmd: models.CreatePhoneAddressCommand,
        phone_address_service: PhoneAddressService = Depends(Provide[Services.phone_address_service]),
):
    return await phone_address_service.create_phone_address(cmd=cmd)


@phone_address.put(
    "/write_data",
    response_model=models.PhoneAddress,
    status_code=status.HTTP_200_OK,
    description="Update phone address",
)
@inject
async def update_phone_address(
        cmd: models.UpdatePhoneAddressCommand,
        phone_address_service: PhoneAddressService = Depends(Provide[Services.phone_address_service]),
):
    return await phone_address_service.update_phone_address(cmd=cmd)