from errors.search_errors import PathNotFoundException
from services.search.abstract_search_service import AbstractSearchService


class SearchService(AbstractSearchService):
    def __init__(self, structure_file: str = "./data/structure.json"):
        super().__init__(structure_file)

    def get_path(self, target_id: str) -> list[str]:
        for node in self.structure:
            result = self.__dfs(node, target_id, list())
            if result:
                return result
        raise PathNotFoundException(f"ID '{target_id}' was not found")

    def __dfs(self, node: dict, target_id: str, path: list[str]) -> list[str]:
        path.append(node["uuid"])

        if node["uuid"] == target_id:
            return path

        for child in node["children"]:
            result = self.__dfs(child, target_id, path)
            if result:
                return result

        path.pop()
        return []
