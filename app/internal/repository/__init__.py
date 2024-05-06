"""Repositories should be dumb, while services, on the contrary, should be
smart. That's why :class:`.Repository` must contain a minimum set of.

**C.R.U.D.** methods.

- **C** - Create
- **R** - Read
- **U** - Update
- **D** - Delete

Note:
    The repository must contain a minimum set of instructions for interacting with the
    target database.
"""

from dependency_injector import containers, providers

from app.internal.repository import redis

__all__ = ["Repositories"]


class Repositories(containers.DeclarativeContainer):
    """Container for repositories.

    Attributes:
        rediss (providers.Container): Container for redis repositories.

    Notes:
        If you want to add a new repository,
        you **must** add it to this container.
    """

    rediss = providers.Container(redis.Repositories)
