from contextlib import asynccontextmanager

import redis.asyncio as aioredis
from dependency_injector.wiring import Provide, inject
from app.pkg.connectors import Connectors

__all__ = ["get_connection"]


@asynccontextmanager
@inject
async def get_connection(
    pool: aioredis.Redis = Provide[Connectors.redis.connector],
):
    """Get async connection to Redis.

    Args:
        pool:
            Redis pool.

    Returns:
        Async connection to Redis.
    """

    yield await pool
