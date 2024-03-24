from api.search_router import *
from services import ServiceRegistry


class RouterRegistry:

    def __init__(self, services: ServiceRegistry):
        self.search_router = SearchRouter(services.search_service)

        self.routes = [
            self.__dict__[router]
            for router in self.__dict__
            if router.endswith("_router")
        ]

    def __iter__(self):
        return iter(self.routes)
