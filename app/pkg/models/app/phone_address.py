"""Models of phone address object."""

from pydantic.fields import Field

from app.pkg.models.base import BaseModel

__all__ = [
    "PhoneAddress",
    "ReadPhoneAddressCommand",
    "CreatePhoneAddressCommand",
    "UpdatePhoneAddressCommand",
]


class BasePhoneAddress(BaseModel):
    """Base model for phone address."""


class PhoneAddressFields:
    phone: str = Field(description="Phone number.", example="89090000000", regex=r"^\d{11}$")
    address: str = Field(description="Address.", example="обл. Новосибирская, гор. Бердск")


class PhoneAddress(BasePhoneAddress):
    phone: str = PhoneAddressFields.phone
    address: str = PhoneAddressFields.address


class ReadPhoneAddressCommand(BasePhoneAddress):
    phone: str = PhoneAddressFields.phone


class CreatePhoneAddressCommand(BasePhoneAddress):
    phone: str = PhoneAddressFields.phone
    address: str = PhoneAddressFields.address


class UpdatePhoneAddressCommand(BasePhoneAddress):
    phone: str = PhoneAddressFields.phone
    address: str = PhoneAddressFields.address
