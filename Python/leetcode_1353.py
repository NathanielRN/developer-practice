from typing import List
import sys
import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[0])
        attended = 0
        attending = []
        day = 1
        for start, end in events + [[sys.maxsize, 0]]:
            while day < start and attending:
                finish = heapq.heappop(attending)
                if day <= finish:
                    attended += 1
                    day += 1

            day = start
            heapq.heappush(attending, end)
        return attended
