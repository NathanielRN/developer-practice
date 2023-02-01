import heapq
from typing import List

class Node:
    def __init__(self, val):
        self.children = []
        self.val = val
    
    def getChildren(self):
        return self.children

class Graph:
    def __init__(self):
        self.nodes = {}
    
    def getNode(self, val: int):
        return self.nodes[val]
    
    def addNode(self, nodeVal: int):
        self.nodes[nodeVal] = Node(nodeVal)
    
    def addEdge(self, sourceVal: int, destinationVal: int, weight: int):
        self.nodes[sourceVal].children.append((weight, self.nodes[destinationVal]))

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = Graph()
        
        kToDestinations = []
        
        # O(V)
        for i in range(1, n + 1):
            kToDestinations.append((float('inf'), i))
            graph.addNode(i)
        
        for edge in times:
            sourceVal, destinationVal, weight = edge
            graph.addEdge(sourceVal, destinationVal, weight)
        
        kToDestinations.pop(k - 1)
        kToDestinations.insert(0, (0, k))
        
        visited = {}
        bestDistances = {}
        
        # O(ElogV)
        while kToDestinations:
            # Must also count distance from current
            currentTime, current = heapq.heappop(kToDestinations)
            
            if current in visited:
                continue

            for child in graph.getNode(current).getChildren():
                destinationAddedWeight, destinationNode = child
                if destinationNode.val in visited:
                    continue
                    
                timeToDestination = currentTime + destinationAddedWeight
                
                if destinationNode.val in bestDistances and bestDistances[destinationNode.val] < timeToDestination:
                    continue
                
                heapq.heappush(kToDestinations, (timeToDestination, destinationNode.val))
                bestDistances[destinationNode.val] = timeToDestination
            
            visited[current] = currentTime
        
        return max(visited.values()) if len(visited) == n else -1

sln = Solution()

sln.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)

# Heap (Almost Djikstra)
# class Solution:
#     def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
#         dic = collections.defaultdict(list)
#         for u,v,w in times:
#             dic[u].append((v,w))
#         q =  [(0,K)]
#         dist = {}
#         while q:
#             d, curr = heapq.heappop(q)
#             if curr in dist: continue
#             dist[curr] = d
#             if len(dist) == N: return d
#             for target, time in dic[curr]:
#                 if target not in dist:
#                     heapq.heappush(q,(time + d,target))
#         return -1
# Queue (Short Path Fast Algorithm)
# class Solution:
#     def networkDelayTime(self, times, N, K):
#         t, graph, q = [0] + [float("inf")] * N, collections.defaultdict(list), collections.deque([(0, K)])
#         for u, v, w in times:
#             graph[u].append((v, w))
#         while q:
#             time, node = q.popleft()
#             if time < t[node]:
#                 t[node] = time
#                 for v, w in graph[node]:
#                     q.append((time + w, v))
#         mx = max(t)
#         return mx if mx < float("inf") else -1