from fastapi import HTTPException

from api.abstract_router import AbstractRouter
from errors.search_errors import PathNotFoundException
from services import AbstractSearchService


class SearchRouter(AbstractRouter):
    service: AbstractSearchService

    def __init__(self, service: AbstractSearchService):
        super().__init__(service=service, prefix="/search", tags=["gazprom"])

    def init_routes(self):
        self.add_api_route(
            path="/get_path",
            methods=["GET"],
            endpoint=self.get_path,
        )

    async def get_path(self, target_id: str) -> list[str]:
        try:
            return self.service.get_path(target_id)
        except PathNotFoundException as error:
            raise HTTPException(status_code=404, detail=str(error))
