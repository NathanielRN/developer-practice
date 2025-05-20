from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        adj = [[] for _ in range(n)]
        for a, b, p in flights:
            
            adj[a].append((b, p))

        q = [(src, 0)]
        minCost = [float("inf") for _ in range(n)]
        stops = 0

        while q and stops <= k:
            size = len(q)
            for i,  in range(size):
                currNode, cost = q.pop(0)
                for neighbour, price in adj[currNode]:
                    if price + cost >= minCost[neighbour]:
                        continue
                    minCost[neighbour] = price + cost
                    q.append((neighbour, minCost[neighbour]))
            stops += 1

        return -1 if minCost[dst] == float("inf") else minCost[dst]


# a = Solution()
# output = a.findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1)
# assert output == 700

# a = Solution()
# output = a.findCheapestPrice(5, [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]], 2, 1, 1)
# assert output == -1

# a = Solution()
# output = a.findCheapestPrice(4, [[0,1,1],[0,2,5],[1,2,1],[2,3,1]], 0, 3, 1)
# assert output == 6

a = Solution()
output = a.findCheapestPrice(
    5,
    [
        [11, 12, 74],
        [1, 8, 91],
        [4, 6, 13],
        [7, 6, 39],
        [5, 12, 8],
        [0, 12, 54],
        [8, 4, 32],
        [0, 11, 4],
        [4, 0, 91],
        [11, 7, 64],
        [6, 3, 88],
        [8, 5, 80],
        [11, 10, 91],
        [10, 0, 60],
        [8, 7, 92],
        [12, 6, 78],
        [6, 2, 8],
        [4, 3, 54],
        [3, 11, 76],
        [3, 12, 23],
        [11, 6, 79],
        [6, 12, 36],
        [2, 11, 100],
        [2, 5, 49],
        [7, 0, 17],
        [5, 8, 95],
        [3, 9, 98],
        [8, 10, 61],
        [2, 12, 38],
        [5, 7, 58],
        [9, 4, 37],
        [8, 6, 79],
        [9, 0, 1],
        [2, 3, 12],
        [7, 10, 7],
        [12, 10, 52],
        [7, 2, 68],
        [12, 2, 100],
        [6, 9, 53],
        [7, 4, 90],
        [0, 5, 43],
        [11, 2, 52],
        [11, 8, 50],
        [12, 4, 38],
        [7, 9, 94],
        [2, 7, 38],
        [3, 7, 88],
        [9, 12, 20],
        [12, 0, 26],
        [10, 5, 38],
        [12, 8, 50],
        [0, 2, 77],
        [11, 0, 13],
        [9, 10, 76],
        [2, 6, 67],
        [5, 6, 34],
        [9, 7, 62],
        [5, 3, 67],
    ],
    2,
    1,
    1,
)
assert output == -1

"""
Djikstra's solution online

# Returns shortest distances from src to all other vertices
def dijkstra(V, edges, src):
    # Create adjacency list
    adj = constructAdj(edges, V)

    # Create a priority queue to store vertices that
    # are being preprocessed.
    pq = []
    
    # Create a list for distances and initialize all
    # distances as infinite
    dist = [sys.maxsize] * V

    # Insert source itself in priority queue and initialize
    # its distance as 0.
    heapq.heappush(pq, [0, src])
    dist[src] = 0

    # Looping till priority queue becomes empty (or all
    # distances are not finalized) 
    while pq:
        # The first vertex in pair is the minimum distance
        # vertex, extract it from priority queue.
        u = heapq.heappop(pq)[1]

        # Get all adjacent of u.
        for x in adj[u]:
            # Get vertex label and weight of current
            # adjacent of u.
            v, weight = x[0], x[1]

            # If there is shorter path to v through u.
            if dist[v] > dist[u] + weight:
                # Updating distance of v
                dist[v] = dist[u] + weight
                heapq.heappush(pq, [dist[v], v])

    # Return the shortest distance array
    return dist
"""

"""
Discussion on graph representation.
[
    [0, 1, 100],
    [1, 2, 100],
    [2, 0, 100],
    [1, 3, 600],
    [2, 3, 200]
]
[
     # 0 1 2 3 4 5
 # 0   X X O X X (Cost)
 # 1   O O X O X
 # 2   
 # 3 
 # 4 
 # 5 
]
{
  0: [(1,100), (4, 300), (5, 50)}
}
"""

""""
Discussion on Djkstra's
                20
        A --------------- Z
  1   / | \               |
     B  C  D              |
40  / \99\  \             | 1
   E   F  G  H            |
 6  \  2 /   /  10        |
       I ---/-------------|
    3  | /
       J
   100 |
       K
"""


# Nathan's O(nlogn) solution that is too slow!
#
# from typing import List

# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         src_price_and_jumps = {src: [(0, 0)]}
        

#         adj_matrix = self.convertToAdjacencyMatrix(flights)


#         while True:
#             visit_src = None
#             min_price = None
#             visit_i = None

#             for potential_next, next_flight_infos in src_price_and_jumps.items():
#                 for i, next_flight_info in enumerate(next_flight_infos):
#                     price, jumps = next_flight_info

#                     if not min_price or price < min_price:
#                         min_price = price
#                         visit_src = potential_next
#                         visit_i = i

#             if visit_src is None:
#                 break

#             if visit_src == dst:
#                 return src_price_and_jumps[visit_src][visit_i][0]

#             if visit_src not in adj_matrix:
#                 src_price_and_jumps[visit_src].pop(visit_i)
#                 continue

#             for visit_next, visit_next_price in adj_matrix[visit_src]:
#                 visit_price, visit_jumps = src_price_and_jumps[visit_src][visit_i]

#                 if visit_next not in src_price_and_jumps:
#                     src_price_and_jumps[visit_next] = []
                
#                 if visit_jumps + 1 != k + 2:
#                     new_to_add = (visit_price + visit_next_price, visit_jumps + 1)
#                     if new_to_add in src_price_and_jumps[visit_next]:
#                         print('hi')
#                         pass
#                     src_price_and_jumps[visit_next].append(new_to_add)

#             src_price_and_jumps[visit_src].pop(visit_i)

#         return -1
    
#     def convertToAdjacencyMatrix(self, flights: List[List[int]]):
#         adj_m = {}

#         for src, dst, price in flights:
#             if src not in adj_m:
#                 adj_m[src] = []

#             adj_m[src].append((dst, price))

#         return adj_m