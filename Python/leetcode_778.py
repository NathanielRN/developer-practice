from typing import List


class Graph:
    def __init__(self, grid):
        self.grid = grid
        
        self.m = len(grid)
        self.n = len(grid[0])
        self.V = self.m * self.n
        self.current_height = 0

    def minDistance(self, dist, sptSet):
        my_min = float("inf")

        for v in range(self.V):
            if dist[v] < my_min and sptSet[v] == False:
                my_min = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src, initial_distance):

        dist = [float("inf")] * self.V
        dist[src] = initial_distance
        self.current_height = initial_distance
        sptSet = [False] * self.V

        for cout in range(self.V):
            u = self.minDistance(dist, sptSet)
            row = u // self.m
            col = u - (row * self.m)
            self.current_height = max(self.current_height, self.grid[row][col])

            self.setGraph()

            sptSet[u] = True

            for v in range(self.V):
                if (
                    self.graph[u][v] >= 0
                    and sptSet[v] == False
                    and dist[v] > dist[u] + self.graph[u][v]
                ):
                    dist[v] = dist[u] + self.graph[u][v]
        return dist


    def setGraph(self):
        distances = []
        for s_row in range(self.m):
            for s_col in range(self.n):
                v_distances = [float("inf")] * self.m * self.n
                for (d_row, d_col) in [
                    (s_row + 1, s_col),
                    (s_row, s_col + 1),
                    (s_row - 1, s_col),
                    (s_row, s_col - 1),
                ]:
                    if 0 <= d_row < self.m and 0 <= d_col < self.n:
                        v_distances[d_row * self.m + d_col] = max(
                            self.grid[d_row][d_col] - max(self.grid[s_row][s_col], self.current_height), 0
                        )
                distances.append(v_distances)
        self.graph = distances

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        g = Graph(grid)
        

        # print(distances)
        # g.graph = distances
        farthest_jumps = g.dijkstra(0, grid[0][0])

        return farthest_jumps[-1]


answer = Solution().swimInWater(
    [
        [0, 1, 2, 3, 4],
        [24, 23, 22, 21, 5],
        [12, 13, 14, 15, 16],
        [11, 17, 18, 19, 20],
        [10, 9, 8, 7, 6],
    ]
    # [[3,2],[0,1]]
    # [
    #     [10, 12, 4, 6], 
    #     [9, 11, 3, 5], 
    #     [1, 7, 13, 8], 
    #     [2, 0, 15, 14]]
)

print(answer)
print("Expected: ", 14)

