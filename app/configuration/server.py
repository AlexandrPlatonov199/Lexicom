"""Server configuration."""


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.configuration.events import on_shutdown, on_startup
from app.internal.routes import __routes__
from app.pkg.models.types.fastapi import FastAPITypes
from app.pkg.settings import settings

__all__ = ["Server"]


class Server:
    """Register all requirements for the correct work of server instance.

    Attributes:
        __app:
            ``FastAPI`` application instance.
        __app_name:
            Name of application used for prometheus metrics and for loki logs.
            Getting from :class:`.Settings`:attr:`.INSTANCE_APP_NAME`.
    """

    __app: FastAPI
    __app_name: str = settings.API.INSTANCE_APP_NAME

    def __init__(self, app: FastAPI):
        """Initialize server instance. Register all requirements for the
        correct work of server instance.

        Args:
            app:
                ``FastAPI`` application instance.
        """

        self.__app = app
        self._register_routes(app)
        self._register_events(app)
        self._register_middlewares(app)

    def get_app(self) -> FastAPI:
        """Getter of the current application instance.

        Returns:
            ``FastAPI`` application instance.
        """
        return self.__app

    @staticmethod
    def _register_events(app: FastAPITypes.instance) -> None:
        """Register :func:`.on_startup` and :func:`.on_shutdown` events.

        Args:
            app:
                ``FastAPI`` application instance.

        Returns:
            None
        """

        app.on_event("startup")(on_startup)
        app.on_event("shutdown")(on_shutdown)

    @staticmethod
    def _register_routes(app: FastAPITypes.instance) -> None:
        """Include routers in ``FastAPI`` instance from ``__routes__``.

        Args:
            app:
                ``FastAPI`` application instance.

        Returns:
            None
        """

        __routes__.register_routes(app)

    @staticmethod
    def __register_cors_origins(app: FastAPITypes.instance) -> None:
        """Register cors origins. In production, you should use only trusted
        origins.

        Args:
            app:
                ``FastAPI`` application instance.

        Returns:
            None
        """

        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def _register_middlewares(self, app) -> None:
        """Apply routes middlewares.

        Args:
            app:
                ``FastAPI`` application instance.

        Returns:
            None
        """

        self.__register_cors_origins(app)
