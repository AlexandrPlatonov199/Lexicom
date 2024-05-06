"""Global point for collected routers. __routes__ is a :class:`.Routes`
instance that contains all routers in your application.
"""

from fastapi import APIRouter

from app.pkg.models.core.routes import Routes

__all__ = [
    "__routes__",
    "phone_address",
]


phone_address = APIRouter(
    prefix="/phone",
    tags=["Phone address"],
)


__routes__ = Routes(
    routers=(
        phone_address,
    ),
)
