from api.router_registry import RouterRegistry
from fastapi import FastAPI
from services.service_registry import ServiceRegistry
from starlette.middleware.cors import CORSMiddleware


class App(FastAPI):

    def __init__(self, title="gazprom", *args, **kwargs) -> None:
        super().__init__(*args, **kwargs, title=title)

        self.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
            allow_headers=[
                "Content-Type",
                "Set-Cookie",
                "Access-Control-Allow-Headers",
                "Access-Control-Allow-Origin",
                "Authorization",
            ],
        )

        services = ServiceRegistry()
        routers = RouterRegistry(services)
        self.include_routers(routers)

    def include_routers(self, routers):
        for router in routers:
            self.include_router(router, prefix="/api")
