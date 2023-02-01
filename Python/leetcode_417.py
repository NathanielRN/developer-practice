from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        # Initialize dimensions (row/col)
        rows, cols = len(heights), len(heights[0])
        atlanticQ = deque()  # List all coordinates that touch the Atlantic
        pacificQ = deque()  # List all coordinates that touch the Pacific
        aVisited = set()
        pVisited = set()

        for row in range(rows):
            pacificQ.append((row, 0))
            atlanticQ.append((row, cols - 1))
        for col in range(cols):
            pacificQ.append((0, col))
            atlanticQ.append((rows - 1, col))

        for q, visited in [(atlanticQ, aVisited), (pacificQ, pVisited)]:
            while q:
                row, col = q.pop()
                currentHeight = heights[row][col]
                if (row, col) not in visited:
                    visited.add((row, col))
                    if (
                        row + 1 in range(rows)
                        and heights[row + 1][col] >= currentHeight
                    ):
                        q.append((row + 1, col))
                    if row > 0 and heights[row - 1][col] >= currentHeight:
                        q.append((row - 1, col))
                    if (
                        col + 1 in range(cols)
                        and heights[row][col + 1] >= currentHeight
                    ):
                        q.append((row, col + 1))
                    if col > 0 and heights[row][col - 1] >= currentHeight:
                        q.append((row, col - 1))

        return aVisited.intersection(pVisited)


answer = Solution().pacificAtlantic(
    [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
)

print(answer)
