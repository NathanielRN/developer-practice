from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        visited = set([(0, 0)])
        m, n = len(grid), len(grid[0])
        queue = [(0, 0)]
        cost = 0

        while True:
            for i, j in queue:
                if grid[i][j] == 1:
                    if j + 1 < n and (i, j + 1) not in visited:
                        queue.append((i, j + 1))
                        visited.add((i, j + 1))
                elif grid[i][j] == 2:
                    if j - 1 >= 0 and (i, j - 1) not in visited:
                        queue.append((i, j - 1))
                        visited.add((i, j - 1))
                elif grid[i][j] == 3:
                    if i + 1 < m and (i + 1, j) not in visited:
                        queue.append((i + 1, j))
                        visited.add((i + 1, j))
                else:
                    if i - 1 >= 0 and (i - 1, j) not in visited:
                        queue.append((i - 1, j))
                        visited.add((i - 1, j))
            if (m - 1, n - 1) in visited:
                return cost
            cost += 1
            newqueue = []
            for x, y in queue:
                for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                    newx, newy = x + dx, y + dy
                    if (
                        0 <= newx < m
                        and 0 <= newy < n
                        and (newx, newy) not in visited
                    ):
                        newqueue.append((newx, newy))
                        visited.add((newx, newy))
            queue = newqueue
        return -1


answer = Solution().minCost(
    [
        [3, 4, 3],
        [2, 2, 2],
        [2, 1, 1],
        [4, 3, 2],
        [2, 1, 4],
        [2, 4, 1],
        [3, 3, 3],
        [1, 4, 2],
        [2, 2, 1],
        [2, 1, 1],
        [3, 3, 1],
        [4, 1, 4],
        [2, 1, 4],
        [3, 2, 2],
        [3, 3, 1],
        [4, 4, 1],
        [1, 2, 2],
        [1, 1, 1],
        [1, 3, 4],
        [1, 2, 1],
        [2, 2, 4],
        [2, 1, 3],
        [1, 2, 1],
        [4, 3, 2],
        [3, 3, 4],
        [2, 2, 1],
        [3, 4, 3],
        [4, 2, 3],
        [4, 4, 4],
    ]
)

print(answer)
