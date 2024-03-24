from collections import deque


class PathSearch:
    def __init__(self):
        self.directions = [
            (row, col) for row in range(-1, 2) for col in range(-1, 2)
        ]

    def get_shortest_path(self, binary_matrix: list[list[int]]) -> int:
        if len(binary_matrix) > 0 and len(binary_matrix[0]) > 0:
            if self.__check_start_and_end(binary_matrix):
                return self.__bfs(binary_matrix)
        return -1

    def __check_start_and_end(self, binary_matrix: list[list[int]]) -> bool:
        n = len(binary_matrix)
        return self.__is_way(binary_matrix, 0, 0) and self.__is_way(
            binary_matrix, n - 1, n - 1
        )

    def __bfs(self, binary_matrix: list[list[int]]):
        n = len(binary_matrix)

        queue = deque([(0, 0, 1)])

        while queue:
            row, col, length = queue.popleft()

            if row == n - 1 and col == n - 1:
                return length

            for dr, dc in self.directions:
                new_row, new_col = row + dr, col + dc
                if (
                    0 <= new_row < n
                    and 0 <= new_col < n
                    and self.__is_way(binary_matrix, new_row, new_col)
                ):
                    queue.append((new_row, new_col, length + 1))
                    binary_matrix[new_row][new_col] = 1

        return -1

    @staticmethod
    def __is_way(binary_matrix: list[list[int]], row: int, col: int) -> bool:
        return binary_matrix[row][col] == 0


if __name__ == "__main__":
    matrix = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    shortest_path = PathSearch().get_shortest_path(matrix)
    print(f"{shortest_path=}")
