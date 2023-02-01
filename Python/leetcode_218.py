from typing import List
from heapq import heappush, heappop


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = [(s, -h, e) for s, e, h in buildings]
        events += list(set((e, 0, 0) for _, e, _ in buildings))
        events.sort()
        maxHeap = [(0, float("inf"))]
        res = [[0, 0]]
        for start, height, end in events:
            while maxHeap and maxHeap[0][1] <= start:
                heappop(maxHeap)
            if height:
                heappush(maxHeap, (height, end))
            if res[-1][1] != -maxHeap[0][0]:
                res.append([start, -maxHeap[0][0]])
        return res[1:]

answer = Solution().getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]])

print(answer)