from typing import List
from heapq import heappop, heappush

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        rows = len(heightMap)
        cols = len(heightMap[0])
        visited = set()
        heap = []
        max_int = float("-inf")
        total = 0
        # heap push edges
        for c in range(cols):
            heappush(heap, (heightMap[0][c], 0, c))
            visited.add((0, c))
            heappush(heap, (heightMap[rows - 1][c], rows - 1, c))
            visited.add((rows - 1, c))

        for r in range(rows):
            heappush(heap, (heightMap[r][0], r, 0))
            visited.add((r, 0))
            heappush(heap, (heightMap[r][cols - 1], r, cols - 1))
            visited.add((r, cols - 1))

        while heap:
            num, r, c = heappop(heap)
            if num < max_int:
                total += max_int - num
            max_int = max(max_int, num)
            for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                nr, nc = dr + r, dc + c
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and (nr, nc) not in visited
                ):
                    heappush(heap, (heightMap[nr][nc], nr, nc))
                    visited.add((nr, nc))
        return total


answer = Solution().trapRainWater(
    [
        [12, 13, 1, 12],
        [13, 4, 13, 12],
        [13, 8, 10, 12],
        [12, 13, 12, 12],
        [13, 13, 13, 13],
    ]
)

print(answer)
