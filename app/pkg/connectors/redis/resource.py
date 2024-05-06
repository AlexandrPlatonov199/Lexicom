import redis.asyncio as aioredis
from app.pkg.connectors.resources import BaseAsyncResource

__all__ = ["Redis"]


class Redis(BaseAsyncResource):
    """Redis connector using aioredis."""

    async def init(self, dsn: str, *args, **kwargs):
        """Getting connection to Redis in asynchronous.

        Args:
            dsn: D.S.N - Data Source Name.

        Returns:
            Created connection to Redis.
        """

        pool = aioredis.ConnectionPool.from_url(dsn)

        return await aioredis.Redis.from_pool(pool)

    async def shutdown(self, resource: aioredis):
        """Close connection.

        Args:
            resource: Resource returned by :meth:`.Redis.init()` method.

        Notes:
            This method is called automatically
            when the application is stopped
            or
            ``Closing`` provider is used.
        """

        await resource.close()
