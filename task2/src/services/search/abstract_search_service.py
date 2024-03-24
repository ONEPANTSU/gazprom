import json
from abc import ABC, abstractmethod

from services.abstract_service import AbstractService


class AbstractSearchService(AbstractService, ABC):
    structure: list

    def __init__(self, structure_file: str):
        self.load_file(structure_file)

    def load_file(self, structure_file: str):
        with open(structure_file, "r") as structure_file:
            self.structure = json.load(structure_file)

    @abstractmethod
    def get_path(self, target_id: str) -> list[str]:
        raise NotImplementedError
