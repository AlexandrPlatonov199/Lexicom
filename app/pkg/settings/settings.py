"""Module for load settings form `.env` or if server running with parameter
`dev` from `.env.dev`"""
import typing
from functools import lru_cache

from pydantic import RedisDsn, root_validator
from dotenv import find_dotenv
from pydantic.env_settings import BaseSettings
from pydantic.types import PositiveInt, SecretStr


__all__ = ["Settings", "get_settings"]


class _Settings(BaseSettings):
    """Base settings for all settings.

    Use double underscore for nested env variables.
    """

    class Config:
        """Configuration of settings."""

        #: str: env file encoding.
        env_file_encoding = "utf-8"
        #: str: allow custom fields in model.
        arbitrary_types_allowed = True
        #: bool: case-sensitive for env variables.
        case_sensitive = True
        #: str: delimiter for nested env variables.
        env_nested_delimiter = "__"


class APIServer(_Settings):
    """API settings."""

    INSTANCE_APP_NAME: str = "project_name"

    HOST: str = "localhost"

    PORT: PositiveInt = 5000


class Redis(_Settings):
    """Redis settings."""

    HOST: str = "localhost"

    PORT: PositiveInt = 6379

    PASSWORD: str = ""

    DSN: typing.Optional[str] = None

    @root_validator(pre=True)
    def build_dsn(cls, values: dict):
        """Build DSN for Redis.

        Args:
            values: dict with all settings.

        Notes:
            This method is called before any other validation.
            I use it to build DSN for Redis.

        Returns:
            dict with all settings and DSN.
        """

        # Constructing the DSN using RedisDsn
        values["DSN"] = RedisDsn.build(
            scheme="redis",
            host=f"@{values.get('HOST')}",
            port=f"{values.get('PORT')}",
            password=f"{values.get('PASSWORD')}"
        )

        return values


class Settings(_Settings):
    """Server settings."""

    #: APIServer: API settings. Contains all settings for API.
    API: APIServer

    REDIS: Redis


@lru_cache
def get_settings(env_file: str = ".env") -> Settings:
    """Create settings instance."""

    return Settings(_env_file=find_dotenv(env_file))
