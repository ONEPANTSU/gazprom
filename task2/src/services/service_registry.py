from services.search.search_service import SearchService


class ServiceRegistry:
    def __init__(self):
        self.search_service = SearchService()
