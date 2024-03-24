from src.path_search import PathSearch


class TestPathSearch:
    path_search = PathSearch()

    def test_get_shortest_path(self, shortest_path_cases):
        for case in shortest_path_cases:
            matrix = case["matrix"]
            answer = case["answer"]
            assert self.path_search.get_shortest_path(matrix) == answer
