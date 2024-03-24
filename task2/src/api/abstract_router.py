from abc import ABC, abstractmethod

from fastapi import APIRouter
from services.abstract_service import AbstractService


class AbstractRouter(APIRouter, ABC):
    service: AbstractService

    def __init__(self, service: AbstractService, prefix: str, tags: list[str]):
        super().__init__(prefix=prefix, tags=tags)
        self.service = service
        self.init_routes()

    @abstractmethod
    def init_routes(self):
        pass
